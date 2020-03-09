import re
from subprocess import Popen, PIPE
from typing import List, Tuple, Union


def separator(number: int) -> None:
    pass


def print_message(message: str, number: int) -> None:
    pass


def get_pyenv_output(command: str) -> List[str]:
    console_output: Tuple[Union[str, bytes], Union[str, bytes]] = Popen(
        [command], shell=True, stdout=PIPE, encoding='utf-8'
    ).communicate()

    console_output_str: str = str(
        console_output[0]
    ).replace('\n', '').replace('*', ' ').strip()

    output_list: List[str] = console_output_str.split('  ')

    return output_list


def get_pyenv(command: str, pattern: str) -> List[str]:
    vers: List = []

    for line in Popen([command], shell=True, stdout=PIPE,
                      encoding='utf-8').communicate():
        line = str(line).replace('\n', '').replace('*', ' ').strip()
        for item in line.split('  '):
            match = re.findall(pattern, item)
            if not match:
                if ' ' in item:
                    item = item[0:item.index(' ')]
                vers.append(item)
    return vers


VIRTUALENV_PATTERN = r"^(?P<env>[^//])..created.+versions.(?P<version>.+).$"
EXCLUDE_VERSION_PATTERN = r"[0-9a-zA-Z.]+/.+/.+"
EXCLUDE_VIRTUALENV_PATTERN = r"^.+/envs/"

pyenv_versions_output = get_pyenv_output('pyenv versions')

pyenv_virtualenvs = get_pyenv_output('pyenv virtualenvs')

pyenv_versions: List = []

for version in pyenv_versions_output:
    m = re.findall(EXCLUDE_VERSION_PATTERN, version)
    if not m:
        if ' ' in version:
            version = version[0:version.index(' ')]
        pyenv_versions.append(version)

# print(pyenv_versions)
# print()
# print(pyenv_versions_output)

v = get_pyenv('pyenv versions', EXCLUDE_VERSION_PATTERN)
v1 = get_pyenv('pyenv virtualenvs', EXCLUDE_VIRTUALENV_PATTERN)

print(v)
print()
print(v1)
