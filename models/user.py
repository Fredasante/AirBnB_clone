#!/usr/bin/python3

"""User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class to inherit from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
