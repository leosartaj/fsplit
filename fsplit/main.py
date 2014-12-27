#!/usr/bin/env python2

##
# fsplit # https://github.com/leosartaj/fsplit.git #
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Main module
"""

import os
import oswrapper as osw
import tar
import exce

def split(fName, num=2, dest=None):
    """
    Splits a file into parts
    """
    if not osw.fileExists(fName):
        raise OSError('file \'%s\' does not exists' %(fName))
    base = osw.basename(fName)

    if not dest:
        dest = osw.dirname(fName)
    dirname = base + '.fsplit'
    location = osw.cdir(dirname, dest)

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

def join(dire=osw.pDir(), dest=''):
    """
    Joins all the .split files together systematically
    """
    if not osw.dirExists(dire):
        raise OSError('directory \'%s\' does not exist' %(dire))
    filename = osw.getFname(dire)
    if not filename:
        raise exce.InvalidDirError("Not a valid fsplit directory \'%s\'" %(dire))
    if not dest:
        dest = osw.getpath(dire, '../')
    dest = osw.getpath(dest, filename)
    outputf = open(dest, 'w')
    dire = osw.getpath(dire)
    for part in osw.olistdir(dire):
        partpath = osw.getpath(dire, part)
        with open(partpath) as inputf:
            osw.fwrite(inputf, outputf)
    outputf.close()
