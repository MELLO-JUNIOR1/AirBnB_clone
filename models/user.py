#!/usr/bin/env python3
"""Module for a class called User"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
