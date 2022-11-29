#!/usr/bin/python3


"""Contains class defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class Details"""
  
    def __init__(self, *args, **kwargs):
        """initialize attributes of BaseModel class"""
    
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
    
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, iso_format)
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """prints in the form [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
  
    def save(self):
        """updates public instance attr 'updated_at' with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
