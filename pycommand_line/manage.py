#!/usr/bin/env python
import sys

from .command_line.command_line import CommandLine


def main(command_line=CommandLine):
    cl = command_line(
        argv=sys.argv
    )
    cl.run()
