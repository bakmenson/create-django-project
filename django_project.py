from subprocess import Popen, PIPE
from typing import List, Tuple, Union
from re import findall, match
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


# TODO add .vim/coc-setting.json for pyenv and coc.nvim
# using commands: pyenv which python
# and write output like /home/solus/.pyenv/versions/django-ecommerce/bin/python
# in .vim/coc-setting.json

DJANGO_PROJECT_ARGV: str = str()

try:
    DJANGO_PROJECT_ARGV = argv[1]
except IndexError as e:
    print_message("Missed project argument ('-c' or '-d')")

VIRTUALENV_PATTERN = r"^(?P<env>[0-9a-zA-z-.]+)..created.+versions." \
                     r"(?P<version>.+).$"
VERSION_PATTERN = r"^[a-zA-Z0-9.-]+$"

VERSIONS_OUTPUT = get_pyenv_output('pyenv versions')
VIRTUALENVS_OUTPUT = get_pyenv_output('pyenv virtualenvs')

versions: List[str] = []

for string in VERSIONS_OUTPUT:
    version_match = findall(VERSION_PATTERN, string)
    if version_match:
        if ' ' in string:
            string = string[0:string.index(' ')]
        versions.append(string)

virtual_envs: List[Tuple[str, str]] = []

for string in VIRTUALENVS_OUTPUT:
    virtualenvs_match = match(VIRTUALENV_PATTERN, string)
    if virtualenvs_match:
        virtual_envs.append((virtualenvs_match.group(1),
                             virtualenvs_match.group(2)))

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
