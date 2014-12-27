#!/usr/bin/env python2
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
For debugging fsplit
"""

import os, sys, shutil
from parse import opfsplit
import oswrapper as osw
import main, tar

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

    parts, istar = args.num, args.tar
    verbose = args.verbose

    base = osw.basename(target)
    path = osw.getpath(dest, base + '.fsplit')
    try:
        if verbose:
            print 'Splitting \'%s\' into \'%d\' parts' %(target, parts)
        main.split(target, num=parts, dest=dest) # now split it
        if istar:
            if verbose:
                print 'Creating Tarfiles'
            tar.createTarAll(path)
            if verbose:
                print 'Tarfiles created'
        if verbose:
            print 'splits saved in \'%s\'' %(path)
            print 'Splitting Complete'
    except Exception, e:
        if os.path.isdir(path):
            shutil.rmtree(path)
        print e
    finally:
        print 'Exiting Now'
