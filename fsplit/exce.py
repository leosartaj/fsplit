#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Exceptions
"""

class InvalidDirError(Exception):
    """
    Raised when directory not a valid fsplit directory
    """
    pass

class NotTarError(Exception):
    """
    raised when file is not a valid tarfile
    """
    pass
