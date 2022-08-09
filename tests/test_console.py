#!/usr/bin/python3
"""Test the console"""


import unittest
import models
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setup(self):
        """setup"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def teardown(self):
        """teardown"""
        sys.stdout = self.backup

    def create(self):
        return HBNBCommand()

    def test_create(self):
        """test create"""
        hbnb = self.create()
        self.assertIsInstance(hbnb, HBNBCommand)

    def test_do_quit(self):
        """test do quit"""
        hbnb = self.create()
        hbnb.do_quit('')
        self.assertEqual(hbnb.do_quit(''), None)

    def test_do_EOF(self):
        """test do EOF"""
        hbnb = self.create()
        hbnb.do_EOF('')
        self.assertEqual(hbnb.do_EOF(''), None)

    def test_do_create(self):
        """test do create"""
        hbnb = self.create()
        hbnb.do_create("BaseModel")
        self.assertEqual(hbnb.do_create("BaseModel"), None)

    def test_do_show(self):
        """test do show"""
        hbnb = self.create()
        hbnb.do_create("BaseModel")
        hbnb.do_show("BaseModel.1")
        self.assertEqual(hbnb.do_show("BaseModel.1"), None)

    def test_do_destroy(self):
        """test do destroy"""
        hbnb = self.create()
        hbnb.do_create("BaseModel")
        hbnb.do_destroy("BaseModel.1")
        self.assertEqual(hbnb.do_destroy("BaseModel.1"), None)

    def test_do_all(self):
        """test do all"""
        hbnb = self.create()
        hbnb.do_create("BaseModel")
        hbnb.do_all("BaseModel")
        self.assertEqual(hbnb.do_all("BaseModel"), None)

    def test_do_update(self):
        """test do update"""
        hbnb = self.create()
        hbnb.do_create("BaseModel")
        hbnb.do_update("BaseModel.1", "name", "Holberton")
        self.assertEqual(hbnb.do_update("BaseModel.1", "name", "Holberton"), None)

    def test_do_count(self):
        """test do count"""
        hbnb = self.create()
        hbnb.do_count("BaseModel")
        self.assertEqual(hbnb.do_count("BaseModel"), None)

    def test_do_show_count(self):
        """test do show count"""
        hbnb = self.create()
        hbnb.do_show_count("BaseModel")
        self.assertEqual(hbnb.do_show_count("BaseModel"), None)
