from typing import Annotated, Optional

import typer
from inquirer_textual import prompts
from inquirer_textual.common.PromptSettings import PromptSettings

from inq.utils import choices_wrapper

cli = typer.Typer(no_args_is_help=True, add_completion=False)


@cli.command(help='Multiple selections from a list of choices')
def checkbox(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Select options:',
             choices: Annotated[
                 Optional[list[str]], typer.Option("-c", help='A list of choices to present to the user')] = None):
    choices = choices_wrapper(choices)
    answer = prompts.checkbox(message, choices, settings=PromptSettings(clear=True))
    for item in answer.value:
        print(item)


@cli.command(help='Confirm or reject')
def confirm(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Are you sure?'):
    answer = prompts.confirm(message, settings=PromptSettings(clear=True))
    print(answer)


# @cli.command(help='External editor')
# def editor(message: Annotated[str, typer.Option("-m", help='The prompt message to display')]):
#     answer = prompts.editor(message, clear=True)
#     print(answer)

@cli.command(help='Select from a list of choices with fuzzy filtering')
def fuzzy(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Select an option:',
          choices: Annotated[
              Optional[list[str]], typer.Option("-c", help='A list of choices to present to the user')] = None):
    choices = choices_wrapper(choices)
    answer = prompts.fuzzy(message, choices, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help='Input a numerical value')
def number(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Enter a value:'):
    answer = prompts.number(message, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help='Enter a file path')
def path(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Enter a value:'):
    answer = prompts.path(message, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help='Select from a list of choices with pattern filtering')
def pattern(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Select an option:',
            choices: Annotated[
                Optional[list[str]], typer.Option("-c", help='A list of choices to present to the user')] = None):
    choices = choices_wrapper(choices)
    answer = prompts.pattern(message, choices, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help='Enter a secret value (e.g., password)')
def secret(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Enter a value:'):
    answer = prompts.secret(message, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help='Select from a list of choices')
def select(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Select an option:',
           choices: Annotated[
               Optional[list[str]], typer.Option("-c", help='A list of choices to present to the user')] = None):
    choices = choices_wrapper(choices)
    answer = prompts.select(message, choices, settings=PromptSettings(clear=True))
    print(answer)


@cli.command(help="Enter a string")
def text(message: Annotated[str, typer.Option("-m", help='The prompt message to display')] = 'Enter a value:'):
    answer = prompts.text(message, settings=PromptSettings(clear=True))
    print(answer)


if __name__ == "__main__":
    cli()
