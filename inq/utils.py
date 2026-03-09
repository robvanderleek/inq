import sys


def choices_wrapper(choices: list[str] | None) -> list[str]:
    if choices is None and not sys.stdin.isatty():
        choices = sys.stdin.read().splitlines()
        if sys.platform == 'win32':
            sys.__stdin__ = open('CON', 'r')
        else:
            sys.__stdin__ = open('/dev/tty', 'r')
    if choices is None or len(choices) == 0:
        print("No choices provided.")
        sys.exit(1)
    return choices
