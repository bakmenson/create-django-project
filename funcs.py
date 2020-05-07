def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def print_help() -> None:
    print("-" * 35)
    print("""
  Arguments:
    --help: print help
    -c: create django project
    -d: delete django project
          """)
    print("-" * 35)


def set_project_arg(input_descr: str, is_empty: bool = False) -> str:
    project_arg: str = input(input_descr + ": >>> ")

    if not is_empty:
        while True:
            if not project_arg:
                print("Missed project variable. Try again.")
                project_arg = input(input_descr + ": >>> ")
                continue
            break

    return project_arg


def do_action(question) -> bool:
    answer: str = input(f"{question}? (y/n)\n>>> ")

    while True:
        if answer.lower() != "y" \
                and answer != "" \
                and answer.lower() != "n":
            answer = input(">>> ")

        elif answer == "n":
            return False

        else:
            return True


if __name__ == "__main__":
    print(do_action("delete"))
