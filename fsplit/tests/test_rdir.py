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
from fsplit import main

class Testcdir(unittest.TestCase):
    """
    tests the rdir function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_rdir_directory_does_not_exists(self):
        dirname = os.path.join(self.dire, 'try')
        self.assertFalse(os.path.isdir(dirname))
        self.assertRaises(OSError, main.rdir, dirname)

    def test_rdir_directory_exists(self):
        dirname = os.path.join(self.dire, 'try')
        os.mkdir(dirname)
        self.assertTrue(os.path.isdir(dirname))
        main.rdir(dirname)
        self.assertFalse(os.path.isdir(dirname))
