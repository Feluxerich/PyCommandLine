from typing import Callable

from pycommand_line.command_line.command_line import CommandLine

REGISTERED_COMMANDS: list[Callable] = list()
USED_COMMAND_LINE = CommandLine
