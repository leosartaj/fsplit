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
from fsplit import tar

class TestcreateTar(unittest.TestCase):
    """
    tests the createTar function in tar module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_createTar_file_exists(self):
        filename = os.path.join(self.dire, 'testData/test.py')
        self.assertTrue(os.path.isfile(filename))
        tar.createTar(filename, self.dire)
        tarname = os.path.join(self.dire, 'test.py.tar.gz')
        self.assertTrue(os.path.isfile(tarname))
        self.assertTrue(tar.isTar(tarname))
        os.remove(tarname)

    def test_createTar_file_does_not_exist(self):
        filename = os.path.join(self.dire, 'try')
        self.assertFalse(os.path.isfile(filename))
        self.assertRaises(OSError, tar.createTar, filename)
