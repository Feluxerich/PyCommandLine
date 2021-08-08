#!/usr/bin/env python
import sys

from . import conf


def main():
    cl = conf.USED_COMMAND_LINE(
        argv=sys.argv
    )
    cl.run()
