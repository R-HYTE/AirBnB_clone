#!/usr/bin/env python3
'''
Module with the BaseModel class
'''
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    '''
    Base class that defines common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance is created.
        updated_at (datetime): Date and time when the instance is last updated.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        '''
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # If kwargs is not empty, update instance attributes
        for key, value in kwargs.items():
            if key in ("created_at", "updated_at"):
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key == "__class__":
                # Get the class type from the class name
                value = models.storage.CLASSES[value]
            setattr(self, key, value)

        # Add the new instance to the storage
        models.storage.new(self)

    def __str__(self):
        '''
        Return the string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Updates `updated_at` with the current datetime and save the instance.
        '''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all keys/values of the instance.
        '''
        modified_instance_dict = self.__dict__.copy()

        # Add __class__ key with the class name of the object
        modified_instance_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to string in ISO format
        modified_instance_dict['created_at'] = self.created_at.isoformat()
        modified_instance_dict['updated_at'] = self.updated_at.isoformat()

        return modified_instance_dict
