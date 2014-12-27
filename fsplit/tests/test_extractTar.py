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
from fsplit import exce

class TestextractTar(unittest.TestCase):
    """
    tests the extractTar function in tar module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_extractTar_file_exists_valid_tar(self):
        tarname = os.path.join(self.dire, 'testData/test.py.tar.gz')
        self.assertTrue(os.path.isfile(tarname))
        self.assertTrue(tar.isTar(tarname))
        tar.extractTar(tarname, self.dire)
        filename = os.path.join(self.dire, 'test.py')
        self.assertTrue(os.path.isfile(tarname))
        self.assertFalse(tar.isTar(tarname))
        os.remove(filename)

    def test_extractTar_file_exists_invalid_tar(self):
        filename = os.path.join(self.dire, 'testData/test.py')
        self.assertTrue(os.path.isfile(filename))
        self.assertRaises(exce.NotTarError, tar.extractTar, filename)

    def test_extractTar_file_exists_valid_tar(self):
        filename = os.path.join(self.dire, 'try')
        self.assertFalse(os.path.isfile(filename))
        self.assertRaises(OSError, tar.extractTar, filename)
