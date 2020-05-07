from subprocess import call, Popen, PIPE
from re import findall


class PyenvAction:
    def __init__(self, virtualenv_name: str, python_version: str = ""):
        """
        :param virtualenv_name: virtualenv name for project
        :param python_version: python version for project
        """
        self._virtualenv_name = virtualenv_name
        self._python_version = python_version

    def install_python(self) -> None:
        """
        install python version
        """
        call("pyenv install " + self._python_version, shell=True)

    def create_virtualenv(self) -> None:
        """
        create new virtualenv
        """
        call("pyenv virtualenv " + self._python_version + " "
             + self._virtualenv_name, shell=True)

    def set_virtualenv(self) -> None:
        """
        set virtualenv for project dir
        """
        call("pyenv local " + self._virtualenv_name, shell=True)

    def __str__(self):
        return f"Virtualenv name: {self._virtualenv_name}," \
               f" Python version: {self._python_version}."


class PyenvOutput:
    def __init__(self, command: str, regex_pattern: str = ""):
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

    def _regex_command_output(self) -> list:
        """
        lefts only python versions or envs name and python versions
        from string pyenv command output
        :return: pattern match
        """
        pattern_match = findall(self._regex_pattern, self._command_output())
        return list(set(pattern_match))

    @property
    def output(self) -> list:
        """
        :return: edited pyenv command from terminal
        """
        if self._regex_pattern:
            return self._regex_command_output()

        return list(filter(
            None, self._command_output().replace("\n", "").split(" ")))

    def __str__(self):
        return f"Command: {self._command}, Regex: {self._regex_pattern}"
