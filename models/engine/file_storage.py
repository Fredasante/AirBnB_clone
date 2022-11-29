#!/usr/bin/python3


"""File Storage Module
Enables the  serialization of instances to a JSON file and
deserialization of JSON file to instances
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances
    Private class attributes:
        - __file_path: string - path to the JSON file
        - __objects: dictionary - empty but will store all objects by
        <class name>.id
    Public instance methods:
        - def all(self)
        - def new(self, obj)
        - def save(self)
        - def reload(self)
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            - obj: instance of BaseModel
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(objects_dict, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                objects_dict = json.load(f)
            for key, value in objects_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
