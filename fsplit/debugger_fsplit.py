#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
For debugging fsplit
"""

import os, sys
from parse import opfsplit
import main

if __name__ == '__main__':
    args = opfsplit.parse_args()

    target = args.target
    if not os.path.exists(target):
        print 'file \'%s\' does not exist.' %(target)
        sys.exit()
    elif not os.path.isfile(target):
        print 'target \'%s\' should be a file' %(target)
        sys.exit()

    dest = args.dest
    if not os.path.exists(dest):
        print 'directory \'%s\' does not exist.' %(dest)
        sys.exit()
    elif not os.path.isdir(dest):
            print 'ouptut destination \'%s\' should be a directory' %(dest)
        sys.exit()

    parts = args.num

    main.split(target, num=parts, dest=dest) # now split it
