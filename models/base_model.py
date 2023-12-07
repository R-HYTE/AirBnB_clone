#!/usr/bin/env python3
'''
Module with the BaseModel class
'''
from datetime import datetime
import uuid


class BaseModel():
    ''' Class that defines all common attributes/methods '''
    def __init__(self, *args, **kwargs):
        ''' Common attributes '''
        if kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = self._convert_to_datetime(
                    kwargs.get('created_at', datetime.now().isoformat())
            )
            self.updated_at = self._convert_to_datetime(
                    kwargs.get('updated_at', datetime.now().isoformat())
            )

            for key, value in kwargs.items():
                if key not in ('id', 'created_at', 'updated_at', '__class__'):
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def _convert_to_datetime(self, date_str):
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        ''' String representation of an object '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' Updates `updated_at` with the current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of `__dict__`
        of the instance but modified to include more fields of our own'''
        modified_instance_dict = self.__dict__.copy()

        # Add __class__ key with the class name of the object
        modified_instance_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to string in ISO format
        modified_instance_dict['created_at'] = self.created_at.isoformat()
        modified_instance_dict['updated_at'] = self.updated_at.isoformat()

        return modified_instance_dict
