#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Contains helper functions for parsing arguments
"""

import argparse # parsing the options

try:
    from fsplit import __desc__ # try to get version number
except ImportError:
    __desc__ = 'UNKNOWN'

def gen_parent_parser():
    """
    Parses the arguments
    """
    parser = argparse.ArgumentParser(add_help=False, conflict_handler='resolve')

    help = "Current version of fsplit"
    parser.add_argument('--version', '-v',  action='version', help=help, version=__desc__)

    help = "For Verbose Output."
    parser.add_argument('--verbose', '-v',  action='store_true', help=help, dest='verbose')

    return parser
