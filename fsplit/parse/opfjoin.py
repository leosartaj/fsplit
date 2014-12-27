#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import argparse # parsing the options
import parent_parser

def parse_args():
    """
    Parses the arguments
    """
    parent = parent_parser.gen_parent_parser()
    parser = argparse.ArgumentParser(parents=[parent], description='Split files into small chunks')

    help = "The target directory to be joined"
    parser.add_argument('target', type=str, help=help)

    help = "Output destination. Defaults to None."
    parser.add_argument('--dest', '-d', type=str, help=help, default='')

    args = parser.parse_args()

    return args
