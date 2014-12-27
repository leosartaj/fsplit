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

import tarfile, os
import oswrapper as osw
import exce

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

def createTarAll(dire=osw.pDir(), dest=None):
    """
    Creates tar of all the files in a directory
    removes the files
    """
    if not osw.dirExists(dire):
        raise OSError('directory \'%s\' does not exist' %(dire))
    for file in os.listdir(dire):
        path = osw.getpath(dire, file)
        createTar(path, dest)
        os.remove(path)

def extractTar(tarname, dest=None):
    """
    Extracts a tarfile to the destination
    """
    basename, dirname = osw.basename(tarname), osw.dirname(tarname)
    if not osw.fileExists(basename, dirname):
        raise OSError('file \'%s\' does not exist' %(tarname))
    if not isTar(tarname):
        raise exce.NotTarError("Not a valid tarfile \'%s\'" %(tarname))
    if not dest:
        dest = osw.getpath(dirname, '')
    with tarfile.open(tarname, 'r|gz') as tar:
        tar.extractall(dest)

def extractTarAll(dire=osw.pDir(), dest=None):
    """
    Extracts all tarfiles to the destination
    removes the tarfiles
    """
    status = False
    if not osw.dirExists(dire):
        raise OSError('directory \'%s\' does not exist' %(dire))
    for file in os.listdir(dire):
        path = osw.getpath(dire, file)
        if isTar(path):
            status = True
            extractTar(path, dest)
            os.remove(path)
    return status
