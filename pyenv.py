from subprocess import call, Popen, PIPE
from re import findall


def install_python(python_version: str) -> None:
    """
    install python version
    """
    call("pyenv install " + python_version, shell=True)


def create_virtualenv(python_version: str, virtualenv_name: str) -> None:
    """
    create new virtualenv
    """
    call("pyenv virtualenv " + python_version + " "
         + virtualenv_name, shell=True)


def set_virtualenv(virtualenv_name: str) -> None:
    """
    set virtualenv for project dir
    """
    call("pyenv local " + virtualenv_name, shell=True)


def output(command: str, regex_pattern: str = "") -> list:
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
