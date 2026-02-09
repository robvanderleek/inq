from typing import Annotated

import typer
from inquirer_textual import prompts

cli = typer.Typer(no_args_is_help=True, add_completion=False)


@cli.command(help='Multiple selections from a list of choices')
def checkbox(message: Annotated[str, typer.Option("-m", help='The prompt message to display')],
             choices: Annotated[list[str], typer.Option("-c", help='A list of choices to present to the user')]):
    answer = prompts.checkbox(message, choices, clear=True)
    for item in answer:
        print(item)


@cli.command(help='Confirm or reject')
def confirm(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.confirm(message, clear=True)
    print(answer)


# @cli.command(help='External editor')
# def editor(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
#     answer = prompts.editor(message, clear=True)
#     print(answer)


@cli.command(help='Input a numerical value')
def number(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.number(message, clear=True)
    print(answer)


@cli.command(help='Enter a file path')
def path(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.path(message, clear=True)
    print(answer)


@cli.command(help='Select from a list of choices with pattern filtering')
def pattern(message: Annotated[str, typer.Option("-m", help='The prompt message to display')],
            choices: Annotated[list[str], typer.Option("-c", help='A list of choices to present to the user')]):
    answer = prompts.pattern(message, choices, clear=True)
    print(answer)


@cli.command(help='Enter a secret value (e.g., password)')
def secret(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.secret(message, clear=True)
    print(answer)


@cli.command(help='Select from a list of choices')
def select(message: Annotated[str, typer.Option("-m", help='The prompt message to display')],
           choices: Annotated[list[str], typer.Option("-c", help='A list of choices to present to the user')]):
    answer = prompts.select(message, choices, clear=True)
    print(answer)


@cli.command(help="Enter a string")
def text(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.text(message, clear=True)
    print(answer)


if __name__ == "__main__":
    cli()
