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

versions_output = get_pyenv_output('pyenv versions')
virtualenvs_output = get_pyenv_output('pyenv virtualenvs')

versions: List[str] = []

for string in versions_output:
    exlude_match = re.findall(EXCLUDE_VERSION_PATTERN, string)
    if not exlude_match:
        if ' ' in string:
            string = string[0:string.index(' ')]
        versions.append(string)

virtualenvs: List[Tuple[str, str]] = []

for string in virtualenvs_output:
    virtualenvs_match = re.match(VIRTUALENV_PATTERN, string)
    if virtualenvs_match:
        virtualenvs.append((virtualenvs_match.group(1),
                            virtualenvs_match.group(2)))

print()
print(versions)
print()
print(virtualenvs)
