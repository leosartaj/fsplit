#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Wraps OS module
Gives useful functions
"""

import os
import shutil

def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def getpath(dire=pDir(), fName=''):
    """
    Generate the path
    """
    dire = os.path.expanduser(dire)
    path = os.path.join(dire, fName)
    return path

def basename(path):
    """
    Gives the basename of a path
    """
    return os.path.basename(path)

def getsize(fName):
    """
    Returns the size of a file
    """
    return os.path.getsize(fName)

def dirname(path):
    """
    Gives the dirname of a path
    """
    return os.path.dirname(path)

def fileExists(fName, dire=pDir()):
    """
    Check if a file exists
    """
    if os.path.isfile(getpath(dire, fName)):
        return True
    return False

def dirExists(dirname):
    """
    Check if a directory exists
    """
    if os.path.isdir(getpath(dirname)):
        return True
    return False

def cdir(dirname, dire=pDir()):
    """
    Create a new directory
    """
    path = getpath(dire, dirname)
    if dirExists(path):
        raise OSError('Directory/file already exists')
    os.mkdir(path)
    return path

def rdir(dirname, dire=pDir()):
    """
    Removes a directory
    """
    path = getpath(dire, dirname)
    if not dirExists(path):
        raise OSError('Directory/file does not exists')
    shutil.rmtree(path)
    return path

def olistdir(dire=pDir(), ext='.split'):
    """
    Lists file in a directory in an ordered way
    only files ending with the ext are returned
    """
    num, cou = [], 1
    for file in os.listdir(dire):
        if file.endswith(ext):
            num.append(cou)
            cou += 1
    files = []
    for n in num:
        filename = str(n) + ext
        files.append(filename)
    return files

def fwrite(inputf, outputf, chunk_size=None):
    """
    Writes in a file
    by reading from another file
    """
    if chunk_size:
        chunk = inputf.read(chunk_size)
    else:
        chunk = inputf.read()
    if chunk:
        outputf.write(chunk)

def getFname(dire, suffix='fsplit'):
    """
    Finds out the filename which was split from the directory name
    """
    basename = os.path.basename(dire)
    baseArr = basename.split('.')
    if baseArr[-1] != suffix:
        return None
    fName = '.'.join(baseArr[:-1])
    return fName
