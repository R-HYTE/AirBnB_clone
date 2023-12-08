#!/usr/bin/env python3
'''
Module with the BaseModel class
'''
from datetime import datetime
import uuid
import models


class BaseModel():
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
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all keys/values of the instance.
        '''
        modified_instance_dict = {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": self.__class__.__name__,
        }
        return modified_instance_dict
