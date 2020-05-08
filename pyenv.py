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


def pyenv_output(command: str, regex_pattern: str = "") -> list:
    """
    :param command:
    :param regex_pattern:
    :return command output as list(str, ...)
     or list(tuple(str, str), ...) for virtualenvs:
    """
    command_output = Popen(
        [command], shell=True, stdout=PIPE, encoding='utf-8'
    ).communicate()[0]

    if regex_pattern:
        pattern_match = findall(regex_pattern, command_output)
        if pattern_match:
            return list(set(pattern_match))

    return list(filter(None, command_output.replace("\n", "").split(" ")))
