#!/usr/bin/python3
'''
This module defines the Place class
'''
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class representing a Place.

    Attributes:
    - city_id (str): The ID of the City associated with the Place.
    - user_id (str): The ID of the User associated with the Place.
    - name (str): The name of the Place.
    - description (str): A description of the Place.
    - number_rooms (int): The number of rooms in the Place.
    - number_bathrooms (int): The number of bathrooms in the Place.
    - max_guest (int): The maximum number of guests the Place can accommodate.
    - price_by_night (int): The price per night for staying at the Place.
    - latitude (float): The latitude coordinate of the Place's location.
    - longitude (float): The longitude coordinate of the Place's location.
    - amenity_ids (list): list of IDs that rep amenities
                        associated with the Place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
