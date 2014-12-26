#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Main module
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

def fileExists(fName, dire=pDir()):
    """
    Check if a file exists
    """
    if os.path.isfile(getpath(dire, fName)):
        return True
    return False

def dirExists(dirname, dire=pDir()):
    """
    Check if a directory exists
    """
    if os.path.isdir(getpath(dire, dirname)):
        return True
    return False

def cdir(dirname, dire=pDir()):
    """
    Create a new directory
    """
    if dirExists(dirname, dire):
        raise OSError('Directory/file already exists')
    path = getpath(dire, dirname)
    os.mkdir(path)
    return path

def rdir(dirname, dire=pDir()):
    """
    Removes a directory
    """
    if not dirExists(dirname, dire):
        raise OSError('Directory/file does not exists')
    path = getpath(dire, dirname)
    shutil.rmtree(path)
    return path

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

def split(fName, num=2, dire=None):
    """
    Splits a file to various numbers
    """
    if not fileExists(fName):
        raise OSError('file %s does not exists' %(fName))
    base = os.path.basename(fName)

    if not dire:
        dire = os.path.dirname(fName)
    dirname = base + '.fsplit'
    location = cdir(dirname, dire)

    size = os.path.getsize(fName)
    chunk_size = size / num
    inputf = open(fName)
    for cou in range(num):
        filename = str(cou + 1) + '.split'
        path = getpath(location, filename)
        with open(path, 'w') as outputf:
            fwrite(inputf, outputf, chunk_size)

    filename = str(num) + '.split'
    path = getpath(location, filename)
    with open(path, 'a') as outputf:
        left = size - (chunk_size * num)
        print left
        fwrite(inputf, outputf, left)

    inputf.close()

def olistdir(dire=pDir(), ext='.split'):
    """
    Lists file in a directory in an ordered way
    """
    num, cou = [], 1
    for file in os.listdir(dire):
        num.append(cou)
        cou += 1
    files = []
    for n in num:
        filename = str(n) + ext
        files.append(filename)
    return files

def getFname(dire):
    """
    Finds out the filename which was split from the directory name
    """
    basename = os.path.basename(dire)
    baseArr = basename.split('.')
    fName = '.'.join(baseArr[:-1])
    return fName

def join(dire=pDir()):
    """
    Joins all the .split files together systematically
    """
    if not dirExists(dire):
        raise OSError('directory %s does not exist' %(dire))
    filename = getFname(dire)
    path = getpath(dire, '../' + filename)
    dire = getpath(dire)
    outputf = open(path, 'w')
    for part in olistdir(dire):
        partpath = getpath(dire, part)
        with open(partpath) as inputf:
            fwrite(inputf, outputf)
    outputf.close()
