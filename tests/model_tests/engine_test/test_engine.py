#!/usr/bin/python3
"""Test the file storage engine"""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import time


class TestFileStorage(unittest.TestCase):
    """Testing File storage class"""

    def setUp(self):
        """Set up"""
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("model_file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all"""
        self.assertEqual(self.storage.all(), {})
    
    def test_new(self):
        """Test new"""
        self.storage.new(self.my_model)
        self.assertEqual(self.storage.all()[self.my_model.id], self.my_model)
    
    def test_save(self):
        """Test save"""
        self.storage.save()
        with open("model_file.json", 'r') as f:
            my_dict = json.load(f)
        self.assertEqual(my_dict[self.my_model.id], self.my_model.to_dict())
    
    def test_reload(self):
        """Test reload"""
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all()[self.my_model.id], self.my_model)
    
    def test_count(self):
        """Test count"""
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.count(), 1)
