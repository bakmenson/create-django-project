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


DJANGO_PROJECT_ARG: str = argv[1]

VIRTUALENV_PATTERN = r"^(?P<env>[0-9a-zA-z-.]+)..created.+versions." \
                     r"(?P<version>.+).$"
EXCLUDE_VERSION_PATTERN = r"[0-9a-zA-Z.]+/.+/.+"

VERSIONS_OUTPUT = get_pyenv_output('pyenv versions')
VIRTUALENVS_OUTPUT = get_pyenv_output('pyenv virtualenvs')

versions: List[str] = []

for string in VERSIONS_OUTPUT:
    exlude_match = findall(EXCLUDE_VERSION_PATTERN, string)
    if not exlude_match:
        if ' ' in string:
            string = string[0:string.index(' ')]
        versions.append(string)

virtual_envs: List[Tuple[str, str]] = []

for string in VIRTUALENVS_OUTPUT:
    virtualenvs_match = match(VIRTUALENV_PATTERN, string)
    if virtualenvs_match:
        virtual_envs.append((virtualenvs_match.group(1),
                            virtualenvs_match.group(2)))

if DJANGO_PROJECT_ARG == '-c':

    print_message("Input project dir.")
    project_dir: str = input(">>> ")

    print_message("Input virtual env.")
    virtual_env: str = input(">>> ")

    print_message("Input Python version (e.g. 3.8.0).")
    python_version: str = input(">>> ")

elif DJANGO_PROJECT_ARG == '-d':
    pass
else:
    print_message("Wrong command.")
