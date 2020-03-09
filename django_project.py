import re
from subprocess import Popen, PIPE
from typing import List, Tuple, Union


def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def get_pyenv_output(command: str, pattern: str) -> List[str]:
    output_list: List[str] = []

    console_output: Tuple[Union[str, bytes], Union[str, bytes]] = Popen(
        [command], shell=True, stdout=PIPE, encoding='utf-8'
    ).communicate()

    console_output_string: str = str(
        console_output[0]
    ).replace('\n', '').replace('*', ' ').strip()

    for string in console_output_string.split('  '):
        match = re.findall(pattern, string)
        if not match:
            if ' ' in string:
                string = string[0:string.index(' ')]
            output_list.append(string)

    return output_list


VIRTUALENV_PATTERN = r"^(?P<env>[^//])..created.+versions.(?P<version>.+).$"
EXCLUDE_VERSION_PATTERN = r"[0-9a-zA-Z.]+/.+/.+"
EXCLUDE_VIRTUALENV_PATTERN = r"^.+/envs/"

versions = get_pyenv_output('pyenv versions', EXCLUDE_VERSION_PATTERN)
virtualenvs = get_pyenv_output('pyenv virtualenvs', EXCLUDE_VIRTUALENV_PATTERN)

print(versions)
print(virtualenvs)
