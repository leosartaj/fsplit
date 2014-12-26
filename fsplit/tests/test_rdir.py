#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
import os, shutil
from fsplit import oswrapper as osw

class Testcdir(unittest.TestCase):
    """
    tests the rdir function in oswrapper module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_rdir_directory_does_not_exists(self):
        dirname = os.path.join(self.dire, 'try')
        self.assertFalse(os.path.isdir(dirname))
        self.assertRaises(OSError, osw.rdir, dirname)

    def test_rdir_directory_exists(self):
        dirname = os.path.join(self.dire, 'try')
        os.mkdir(dirname)
        self.assertTrue(os.path.isdir(dirname))
        osw.rdir(dirname)
        self.assertFalse(os.path.isdir(dirname))
