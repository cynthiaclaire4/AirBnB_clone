#!/usr/bin/python3
"""Testing the BaseModel class"""

from models.base_model import BaseModel
import unittest
import sys
import datetime
from io import StringIO


class TestBase(unittest.TestCase):
    """Testing the BaseModel class"""

    def setUp(self):
        """setup"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """teardown"""
        sys.stdout = self.backup

    def test_init(self):
        """test init"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)

    def test_str(self):
        """test str"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))

    def test_save(self):
        """test save"""
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(my_model.updated_at, datetime.datetime.now())

    def test_to_dict(self):
        """test to_dict"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['name'], my_model.name)
        self.assertEqual(my_model_dict['my_number'], my_model.my_number)
