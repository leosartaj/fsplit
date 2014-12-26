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
    tests the cdir function in oswrapper module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_cdir_new_directory(self):
        dirname = os.path.join(self.dire, 'try')
        self.assertFalse(os.path.isdir(dirname))
        osw.cdir(dirname)
        self.assertTrue(os.path.isdir(dirname))
        shutil.rmtree(dirname)

    def test_cdir_directory_exits(self):
        dirname = os.path.join(self.dire, 'try')
        os.mkdir(dirname)
        self.assertTrue(os.path.isdir(dirname))
        self.assertRaises(OSError, osw.cdir, dirname)
        shutil.rmtree(dirname)
