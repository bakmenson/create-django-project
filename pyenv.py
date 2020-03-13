from subprocess import Popen, PIPE, call
from re import findall
from typing import List, Tuple, Union


def get_console_output(command) -> List[str]:
    console_output: Tuple[Union[str, bytes], Union[str, bytes]] = Popen(
        [command], shell=True, stdout=PIPE, encoding='utf-8'
    ).communicate()

    console_output_string: str = str(
        console_output[0]
    ).replace('\n', '').replace('*', ' ').strip()

    output_list: List[str] = console_output_string.split('  ')

    return output_list


def get_regex_console_output(
        pyenv_output: List[str], regex_pattern: str
) -> List[Union[str, Tuple[str]]]:

    result: List[Union[str, Tuple[str]]] = []

    for line in pyenv_output:
        pattern_match = findall(regex_pattern, line)
        if pattern_match:
            result.append(*pattern_match)

    for string in result:
        if isinstance(string, str):
            result[result.index(string)] = string.rstrip()

    return result


def get_command_output(
        command: str, regex_pattern: str
) -> List[Union[str, Tuple[str]]]:
    return get_regex_console_output(
        get_console_output(command),
        regex_pattern
    )


def install_python(python_version) -> None:
    call("pyenv install " + python_version, shell=True)


def create_virtualenv(python_version, env_name) -> None:
    call("pyenv virtualenv " + python_version + " " + env_name, shell=True)


def set_virtualenv(env_name) -> None:
    call("pyenv local " + env_name, shell=True)
