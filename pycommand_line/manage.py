#!/usr/bin/env python
import sys

# if __name__ == '__main__':
#     from . import conf
# else:
#     from pycommand_line import conf

from . import conf


def main():
    cl = conf.USED_COMMAND_LINE(
        argv=sys.argv
    )
    cl.run()
