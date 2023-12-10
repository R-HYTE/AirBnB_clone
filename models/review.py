#!/usr/bin/python3
'''
This module defines the Review class.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a Review.

    Attributes:
    - place_id (str): The ID of the Place associated with the Review.
    - user_id (str): The ID of the User who wrote the Review.
    - text (str): The text content of the Review.
    """
    place_id = ""
    user_id = ""
    text = ""
