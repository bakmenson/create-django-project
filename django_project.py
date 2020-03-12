from sys import argv


def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def set_project_var(input_message: str) -> str:
    print_message(input_message)
    project_var: str = input(">>> ")

    while True:
        if not project_var:
            print("You did not set var. Try again.")
            project_var = input(">>> ")
        else:
            break

    return project_var.replace(' ', '_')


# TODO add .vim/coc-setting.json for pyenv and coc.nvim
# using commands: pyenv which python
# and write output like /home/solus/.pyenv/versions/django-ecommerce/bin/python
# in .vim/coc-setting.json

DJANGO_PROJECT_ARGV: str = str()

try:
    DJANGO_PROJECT_ARGV = argv[1]
except IndexError as e:
    print_message("Missed project argument ('-c' or '-d')")

VIRTUALENV_PATTERN = r"^([a-zA-Z0-9.-]+)..created.+versions.(.+).$"
VERSION_PATTERN = r"^[a-zA-Z0-9.-]+$|^[a-zA-Z0-9.-]+\s"

if DJANGO_PROJECT_ARGV == '-c':

    project_dir: str = set_project_var("Input project dir.")
    #virtual_env: str = set_project_var("Input virtual env.")
    #python_version: str = set_project_var("Input Python version (e.g. 3.8.0).")
    print(project_dir)

elif DJANGO_PROJECT_ARGV == '-d':
    pass
else:
    if DJANGO_PROJECT_ARGV:
        print_message("Wrong command.")
