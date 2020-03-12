from subprocess import Popen, PIPE, call
from re import findall
from typing import List, Tuple, Union


class Pyenv:
    def __init__(self, env_name, python_version):
        self._env_name: str = env_name
        self._python_version: str = python_version

    def _get_console_output(self, command) -> List[str]:
        console_output: Tuple[Union[str, bytes], Union[str, bytes]] = Popen(
            [command], shell=True, stdout=PIPE, encoding='utf-8'
        ).communicate()

        console_output_string: str = str(
            console_output[0]
        ).replace('\n', '').replace('*', ' ').strip()

        output_list: List[str] = console_output_string.split('  ')

        return output_list

    def _get_regex_console_output(
        self, pyenv_output: List[str], regex_pattern: str
    ) -> List[Union[str, Tuple[str]]]:

        result: List[Union[str, Tuple[str]]] = []

        for string in pyenv_output:
            pattern_match = findall(regex_pattern, string)
            if pattern_match:
                result.append(*pattern_match)

        for string in result:
            if isinstance(string, str):
                result[result.index(string)] = string.rstrip()

        return result

    def get_command_output(
        self, command: str, regex_pattern: str
    ) -> List[Union[str, Tuple[str]]]:
        return self._get_regex_console_output(
            self._get_console_output(command),
            regex_pattern
        )

    def install_python(self, version) -> None:
        call("pyenv install " + version, shell=True)

    def create_virtualenv(self, python_version, env_name) -> None:
        call("pyenv virtualenv " + python_version + " " + env_name, shell=True)

    def set_virtualenv(self, env_name) -> None:
        call("pyenv local " + env_name, shell=True)
