#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import os
import argparse # parsing the options
import parent_parser

def parse_args():
    """
    Parses the arguments
    """
    parent = parent_parser.gen_parent_parser()
    parser = argparse.ArgumentParser(parents=[parent], description='Split files into small chunks')

    help = "The target file to be split"
    parser.add_argument('target', type=str, help=help)

    help = "Output destination. Defaults to cwd."
    parser.add_argument('--dest', '-d', type=str, help=help, default=os.getcwd())

    help = "Number of splits. Defaults to 2."
    parser.add_argument('--num', '-n', type=int, help=help, default=2)

    help = "Use for creating tar of each split. Defaults to False"
    parser.add_argument('--tar', '-t', action='store_true', help=help)

    args = parser.parse_args()

    return args
