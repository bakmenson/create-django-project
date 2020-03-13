from sys import argv, exit
from pyenv import get_command_output, install_python, create_virtualenv, \
    set_virtualenv


def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def print_help() -> None:
    print('-' * 55)
    print('''
  First arg:
    -h: print help
    -c: create django project
    -d: delete django project

  Second arg:
    project directory to be created

  Third arg:
    virtual env to be created or set for project

  Fourth arg:
    python version to be installed or set for project
          ''')
    print('-' * 55)


def get_argv(argv_num: int, is_except: bool = True) -> str:
    project_argv: str = str()
    try:
        project_argv = argv[argv_num]
    except IndexError:
        if is_except:
            print_message("Missed project argument.")
            exit()

    return project_argv


# TODO add .vim/coc-setting.json for pyenv and coc.nvim
# using commands: pyenv which python
# and write output like /home/solus/.pyenv/versions/django-ecommerce/bin/python
# in .vim/coc-setting.json

project_action: str = get_argv(1)

if project_action == "-h":
    print_help()
    exit()

project_dir: str = get_argv(2)
virtual_env: str = get_argv(3)
python_version: str = get_argv(4, False)

VIRTUALENV_PATTERN = r"^([a-zA-Z0-9.-]+)..created.+versions.(.+).$"
VERSION_PATTERN = r"^[a-zA-Z0-9.-]+$|^[a-zA-Z0-9.-]+\s"

if project_action == '-c':

    versions = get_command_output("pyenv versions", VERSION_PATTERN)
    virtualenvs = get_command_output("pyenv virtualenvs", VIRTUALENV_PATTERN)

    print(versions)
    print(virtualenvs)

elif project_action == '-d':
    pass
else:
    if project_action:
        print_help()
