import re
from subprocess import Popen, PIPE
from typing import List, Tuple, Union


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


VIRTUALENV_PATTERN = r"^(?P<env>[0-9a-zA-z-.]+)..created.+versions.(?P<version>.+).$"
EXCLUDE_VERSION_PATTERN = r"[0-9a-zA-Z.]+/.+/.+"
EXCLUDE_VIRTUALENV_PATTERN = r"^.+/envs/"

versions = get_pyenv_output('pyenv versions')
virtualenvs = get_pyenv_output('pyenv virtualenvs')

print(versions)
print(virtualenvs)
