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

import oswrapper as osw

def split(fName, num=2, dire=None):
    """
    Splits a file to various numbers
    """
    if not osw.fileExists(fName):
        raise OSError('file %s does not exists' %(fName))
    base = osw.basename(fName)

    if not dire:
        dire = osw.dirname(fName)
    dirname = base + '.fsplit'
    location = osw.cdir(dirname, dire)

    size = osw.getsize(fName)
    chunk_size = size / num
    inputf = open(fName)
    for cou in range(num):
        filename = str(cou + 1) + '.split'
        path = osw.getpath(location, filename)
        with open(path, 'w') as outputf:
            osw.fwrite(inputf, outputf, chunk_size)

    filename = str(num) + '.split'
    path = osw.getpath(location, filename)
    with open(path, 'a') as outputf:
        left = size - (chunk_size * num)
        osw.fwrite(inputf, outputf, left)

    inputf.close()

def join(dire=osw.pDir()):
    """
    Joins all the .split files together systematically
    """
    if not osw.dirExists(dire):
        raise OSError('directory %s does not exist' %(dire))
    filename = osw.getFname(dire)
    if not filename:
        raise OSError("Not valid fsplit directory %s" %(dire))
    path = osw.getpath(dire, '../' + filename)
    dire = osw.getpath(dire)
    outputf = open(path, 'w')
    for part in osw.olistdir(dire):
        partpath = osw.getpath(dire, part)
        with open(partpath) as inputf:
            osw.fwrite(inputf, outputf)
    outputf.close()
