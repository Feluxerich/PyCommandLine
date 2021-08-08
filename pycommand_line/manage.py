#!/usr/bin/env python
import sys

if __name__ == '__main__':
    from .utils.command_line import CommandLine
else:
    from pycommand_line.utils.command_line import CommandLine


def main():
    cl = CommandLine(
        argv=sys.argv
    )
    cl.run()
