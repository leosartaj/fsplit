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
import oswrapper as osw
import main, tar, exce

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

    verbose = args.verbose
    if target.endswith('/'):
        target = target[:-1]
    base = osw.basename(target)
    path = osw.getpath(dest, base[:-7])
    try:
        if verbose:
            print 'Joining \'%s\' into \'%s\'' %(target, path)
            print 'Looking for tarfiles'
        status = tar.extractTarAll(target)
        if verbose:
            if status:
                print 'Tarfiles extracted'
            else:
                print 'No tarfile found'
            print 'Starting join'
        main.join(target, dest)
        if verbose:
            print 'Joined into \'%s\'' %(path)
            print 'Joining Complete'
    except Exception, e:
        print e
        if os.path.isfile(path):
            os.remove(path)
    finally:
        print 'Exiting Now'
