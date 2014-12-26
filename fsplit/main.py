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

def fwrite(handler, fName, chunk_size=None, MODE='w'):
    """
    Writes in a file
    by reading from another file
    """
    if chunk_size:
        chunk = handler.read(chunk_size)
    else:
        chunk = handler.read()
    if chunk:
        with open(fName, MODE) as f:
            f.write(chunk)

def split(fName, num=2):
    """
    Splits a file to various numbers
    """
    if not fileExists(fName):
        raise OSError('file %s does not exists' %(fName))
    dire, base = os.path.dirname(fName), os.path.basename(fName)

    dirname = base + '.fsplit'
    location = cdir(dirname, dire)

    size = os.path.getsize(fName)
    chunk_size = size / num
    handler = open(fName)
    for cou in range(num):
        filename = str(cou + 1) + '.split'
        path = getpath(location, filename)
        fwrite(handler, path, chunk_size)

    # test this portion after making join
    filename = str(num) + '.split'
    path = getpath(location, filename)
    fwrite(handler, path, chunk_size, 'a') # make sure nothing is left

def olistdir(dire=pDir()):
    """
    Lists file in a directory in an ordered way
    """
    files = []
    for file in os.listdir(dire):
        files.append(file)
    files.sort()
    return files

def join(dire=pDir()):
    """
    Joins all the .split files together systematically
    """
    pass
