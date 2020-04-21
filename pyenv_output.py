from typing import List
from re import sub
from subprocess import Popen, PIPE


class PyenvOutput:
    def __init__(self, command: str, regex_pattern: str):
        """
        :param command: pyenv command like "pyenv versions"
        "pyenv virtualenvs", "pyenv install --list"
        :param regex_pattern: regex expression pattern
        """
        self._command = command
        self._regex_pattern = regex_pattern

    def _command_output(self) -> str:
        """
        :return: pyenv command output from terminal as string
        """
        return Popen(
            [self._command], shell=True, stdout=PIPE, encoding='utf-8'
        ).communicate()[0]

    def _regex_command_output(self) -> str:
        """
        Method removing from output string unnecessary parts (*, \n, (...))
        and left only information about python versions or exists
        virtualenvs or available pyenv install list
        :return: edited command output
        """
        edited_str: str = str()

        pattern_match = sub(self._regex_pattern, "", self._command_output())
        if pattern_match:
            edited_str = pattern_match.replace("\n", "").replace("*", "")

        return edited_str

    @property
    def output(self) -> List[str]:
        """
        :return: edited command output string as list
        """
        return list(filter(None, self._regex_command_output().split(" ")))

    def __str__(self):
        return f"Command: {self._command}, Regex: {self._regex_pattern}"
