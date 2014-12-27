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

class Testsplitjoin(unittest.TestCase):
    """
    tests the split, join function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_split_file_exists(self):
        filename = os.path.join(self.dire, 'testData/test.py')
        self.assertTrue(os.path.isfile(filename))
        parts = 10
        main.split(filename, num=parts, dest=self.dire)
        dirname = os.path.join(self.dire, 'test.py.fsplit')
        self.assertTrue(os.path.isdir(dirname))
        num = 0
        for f in os.listdir(dirname):
            num += 1
        self.assertEqual(num, parts)
        shutil.rmtree(dirname)

    def test_split_file_does_not_exist(self):
        filename = os.path.join(self.dire, 'try')
        self.assertRaises(OSError, main.split, filename)

    def test_join(self):
        filename = os.path.join(self.dire, 'testData/test.py')
        self.assertTrue(os.path.isfile(filename))
        parts = 10
        main.split(filename, num=parts, dest=self.dire)
        dirname = os.path.join(self.dire, 'test.py.fsplit')
        self.assertTrue(os.path.isdir(dirname))
        main.join(dirname)
        joinname = os.path.join(self.dire, 'test.py')
        self.assertTrue(os.path.isfile(joinname))
        shutil.rmtree(dirname)
        os.remove(joinname)

    def test_join_dir_does_not_exist(self):
        dirname = os.path.join(self.dire, 'try')
        self.assertRaises(OSError, main.join, dirname)

    def test_join_invalid_dir(self):
        dirname = os.path.join(self.dire, 'try')
        self.assertRaises(OSError, main.join, dirname)
