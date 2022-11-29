#!/usr/bin/python3
"""Module TestHBNBCommand"""

import models
import unittest
import sys
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):
    def test_do_create(self):
        """Tests create for all classes."""
        for classname in self.classes():
            self.help_test_do_create(classname)

    def help_test_do_create(self, classname):
        """Helper method to test the create commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

    def test_do_create_error(self):
        """Tests create command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create doesnotexist")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")

    def test_do_show(self):
        """Tests show for all classes."""
        for classname in self.classes():
            self.help_test_do_show(classname)

    def help_test_do_show(self, classname):
        """Helps test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        value = f.getvalue()[:-1]
        self.assertTrue(uid in value)

    def test_do_show_error(self):
        """Tests show command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** no instance found **")

    def test_do_destroy(self):
        """Tests destroy for all classes."""
        for classname in self.classes():
            self.help_test_do_destroy(classname)

    def help_test_do_destroy(self, classname):
        """Helps test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
        value = f.getvalue()[:-1]
        self.assertTrue(len(value) == 0)

    def test_do_destroy_error(self):
        """Tests destroy command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** no instance found **")

    def test_do_all(self):
        """Tests all for all classes."""
        for classname, cls in self.classes().items():
            self.help_test_do_all(classname)

    def help_test_do_all(self, classname):
        """Helps test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        value = f.getvalue()[:-1]
        self.assertTrue(len(value) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        value = f.getvalue()[:-1]
        self.assertTrue(len(value) > 0)

    def test_do_all_error(self):
        """Tests all command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")

    def test_do_update(self):
        """Tests update for all classes."""
        pass

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

if __name__ == "__main__":
    unittest.main()
