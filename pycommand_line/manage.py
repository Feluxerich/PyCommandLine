#!/usr/bin/env python
import sys

from . import conf
from .command_line.command_line import CommandLine


def main():
    if conf.USED_COMMAND_LINE:
        cl = conf.USED_COMMAND_LINE(
            argv=sys.argv
        )
        cl.run()
    else:
        cl = CommandLine(
            argv=sys.argv
        )
        cl.run()
