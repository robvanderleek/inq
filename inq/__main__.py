from typing import Annotated

import typer
from inquirer_textual import prompts

cli = typer.Typer(no_args_is_help=True, add_completion=False)


@cli.command()
def checkbox(message: Annotated[str, typer.Option("-m", help='The prompt message to display')],
             choices: Annotated[list[str], typer.Option("-c", help='A list of choices to present to the user')]):
    answer = prompts.checkbox(message, choices, clear=True)
    for item in answer:
        print(item)


@cli.command()
def confirm(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.confirm(message, clear=True)
    print(answer)


@cli.command()
def text(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
    answer = prompts.text(message, clear=True)
    print(answer)


if __name__ == "__main__":
    cli()
