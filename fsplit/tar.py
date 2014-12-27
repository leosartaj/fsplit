#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Tar related functionality
"""

import tarfile
import oswrapper as osw

def isTar(fName):
    """
    checks whether a file is a tarfile or not
    """
    return tarfile.is_tarfile(fName)

def createTar(fName, dest=None):
    """
    Converts a file into tar
    """
    basename, dirname = osw.basename(fName), osw.dirname(fName)
    if not osw.fileExists(basename, dirname):
        raise OSError('file \'%s\' does not exist' %(fName))
    if not dest:
        dest = osw.getpath(dirname, '')
    dest = osw.getpath(dest, basename + '.tar.gz')
    with tarfile.open(dest, 'w:gz') as tar:
        tar.add(fName, arcname=basename)
