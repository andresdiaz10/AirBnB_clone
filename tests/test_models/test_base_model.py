#!/usr/bin/python3
"""this module tests the cases of BaseModel"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest
import os
import models


class TestBaseModel(unittest.TestCase):
    """"Tests cases"""
    def set_up(self):
        """creating object of BaseModel."""
        self.object = BaseModel()
        self.object1 = BaseModel()

    def tear_down(self):
        """Test teardown."""
        del self.object
        del self.object1
        if os.path.exists("file.json"):
            os.remove()

    def setUp(self):
        """creating object of BaseModel"""
        self.Model = BaseModel()

    def exist_BaseModel(self):
        """test of exist the class BaseModel"""
        self.assertEqual('[BaseModel]' in str(self.Model), True)

    def test_type(self):
        """test type of Model"""
        self.assertEqual(type(self.Model), BaseModel)

    def test_Model_id(self):
        """test id for BaseModel"""
        self.assertEqual(type(self.Model.id), str)
        self.assertTrue(hasattr(self.Model, "id"))

    def test_Model_created(self):
        """test created_ad for BaseModel"""
        self.assertEqual(type(self.Model.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.Model, "created_at"))

    def test_Model_update(self):
        """test update_at for BaseModel"""
        self.assertEqual(type(self.Model.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.Model, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.Model)), str)

    def testInstanceBaseModel(self):
        """Test if a object is from the class BaseModel"""
        test_object = BaseModel()
        self.assertIsInstance(test_object, BaseModel)

    def testObjectId(self):
        """Test if a class generate unique id"""
        test_object = BaseModel()
        test_object1 = BaseModel()
        self.assertNotEqual(test_object.id, test_object1.id)

    def testObjectSave(self):
        """Test to check if the method save is working"""
        test_object = BaseModel()
        first_date = test_object.updated_at
        test_object.save()
        second_date = test_object.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_to_dict(self):
        """Check if dic works"""
        test_object = BaseModel()
        test_dict = test_object.to_dict()
        self.assertIsInstance(test_dict, dict)
        for key, value in test_dict.items():
            aux = 0
            if test_dict["__class__"] == "BaseModel":
                aux += 1
            self.assertTrue(aux == 1)
        for key, value in test_dict.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)


if __name__ == "__main__":
    unittest.main()
