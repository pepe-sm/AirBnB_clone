#!/usr/bin/python3
"""
    This is the test_file_storage module
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_FileStorage(unittest.TestCase):
    """ This Tests for FileStorage class """

    def test_jsonfile_path(self):
        """ This check __file_path attribute """
        fs1 = FileStorage()
        self.assertEqual(fs1._FileStorage__file_path, "file.json")

    def test_objects(self):
        """ Is the check __objects attribute """
        fs2 = FileStorage()
        self.assertIsInstance(fs2._FileStorage__objects, dict)

    def test_all_method(self):
        """ Is the check all methods the instance has """
        fs3 = FileStorage()
        base1 = BaseModel()
        fs3.new(base1)
        all_objs = fs3.all()
        self.assertIn(base1, all_objs.values())
        fs3.reload()
        all_objs_reloaded = fs3.all()
        self.assertIn(base1, all_objs_reloaded.values())

    def test_save_fs(self):
        """ Is the check save() method """
        base2 = BaseModel()
        first_version = base2.updated_at
        base2.save()
        last_version = base2.updated_at
        self.assertNotEqual(first_version, last_version)

    def test_reload_method(self):
        """ Is the check reload() method """
        fs4 = FileStorage()
        base3 = BaseModel()
        base4 = BaseModel()
        fs4.save()
        fs4.reload()
        all_objs = fs4.all()
        self.assertIn(base3, all_objs.values())
        self.assertIn(base4, all_objs.values())


if __name__ == '__main__':
    unittest.main()
