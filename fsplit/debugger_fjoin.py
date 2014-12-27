#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
For debugging fjoin
"""

import os, sys
from parse import opfjoin
import main
import tar
import exce

if __name__ == '__main__':
    args = opfjoin.parse_args()

    target = args.target
    if not os.path.exists(target):
        print 'directory \'%s\' does not exist.' %(target)
        sys.exit()
    elif not os.path.isdir(target):
        print 'target \'%s\' should be a directory' %(target)
        sys.exit()

    dest = args.dest
    if dest:
        if not os.path.exists(dest):
            print 'directory \'%s\' does not exist.' %(dest)
            sys.exit()
        elif not os.path.isdir(dest):
            print 'ouptut destination \'%s\' should be a directory' %(dest)
            sys.exit()

    try:
        tar.extractTarAll(target)
        main.join(target, dest)
    except Exception, e:
        print e
