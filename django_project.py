from subprocess import Popen, PIPE
from typing import List, Tuple, Union
from re import match, compile
from sys import argv


def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def get_pyenv_output(command: str) -> List[str]:
    console_output: Tuple[Union[str, bytes], Union[str, bytes]] = Popen(
        [command], shell=True, stdout=PIPE, encoding='utf-8'
    ).communicate()

    console_output_string: str = str(
        console_output[0]
    ).replace('\n', '').replace('*', ' ').strip()

    output_list: List[str] = console_output_string.split('  ')

    return output_list


def set_project_var(input_message: str) -> str:
    print_message(input_message)
    project_var: str = input(">>> ")

    while True:
        if not project_var:
            print("You did not set var. Try again.")
            project_var = input(">>> ")
        else:
            break

    return project_var.replace(' ', '_')


def get_pyenv_regex(pyenv_output: List[str], regex_pattern: str):
    result: List[Union[str, List[str]]] = []
    regex_group_count: int = compile(regex_pattern).groups

    for string in pyenv_output:
        pattern_match = match(regex_pattern, string)
        if pattern_match:
            if regex_group_count == 1:
                result.append(string)
            elif regex_group_count > 1:
                groups_list: List[str] = []
                for number in range(1, regex_group_count + 1):
                    groups_list.append(pattern_match.group(number))
                result.append(groups_list)
            else:
                raise ValueError("Regex group count cannot be less 1.")

    return result


# TODO add .vim/coc-setting.json for pyenv and coc.nvim
# using commands: pyenv which python
# and write output like /home/solus/.pyenv/versions/django-ecommerce/bin/python
# in .vim/coc-setting.json

DJANGO_PROJECT_ARGV: str = str()

try:
    DJANGO_PROJECT_ARGV = argv[1]
except IndexError as e:
    print_message("Missed project argument ('-c' or '-d')")

VIRTUALENV_PATTERN = r"^([a-zA-Z0-9.-]+)..created.+versions.(.+).$"
VERSION_PATTERN = r"^([a-zA-Z0-9.-]+)$"

VERSIONS_OUTPUT = get_pyenv_output('pyenv versions')
VIRTUALENVS_OUTPUT = get_pyenv_output('pyenv virtualenvs')

for string in VERSIONS_OUTPUT:
    if ' ' in string:
        space_index = VERSIONS_OUTPUT.index(string)
        VERSIONS_OUTPUT[space_index] = string[0:string.index(' ')]

versions: List[Union[str, List[str]]] = get_pyenv_regex(
    VERSIONS_OUTPUT, VERSION_PATTERN
)

virtual_envs: List[Union[str, List[str]]] = get_pyenv_regex(
    VIRTUALENVS_OUTPUT, VIRTUALENV_PATTERN
)

if DJANGO_PROJECT_ARGV == '-c':

    project_dir: str = set_project_var("Input project dir.")
    #virtual_env: str = set_project_var("Input virtual env.")
    #python_version: str = set_project_var("Input Python version (e.g. 3.8.0).")
    print(project_dir)

elif DJANGO_PROJECT_ARGV == '-d':
    pass
else:
    if DJANGO_PROJECT_ARGV:
        print_message("Wrong command.")
