#!/usr/bin/env python3
"""Module for a class called Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class City that inherits from BaseModel class"""

    place_id = ''
    user_id = ''
    text = ''
