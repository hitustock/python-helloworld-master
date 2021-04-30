"""Top-level implementation of the helloworld program."""

import argparse
import sys
import win32api
import helloworld


parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any arguments.
    # This just checks for the special --version and --help arguments and
    # ensures the user hasn't passed any other unrecognized arguments.
    parser.parse_args(argv[1:])

    print("Hello, world")
	win32api.MessageBox(0, 'hello', 'title')
	win32api.MessageBox(0, 'hello', 'title', 0x00001000) 

    return 0
