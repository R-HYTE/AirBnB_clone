#!/usr/bin/python3
'''
This module defines the City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a City.

    Attributes:
    - state_id (str): The state ID associated with the City.
    - name (str): The name of the City.
    """
    state_id = ""
    name = ""
