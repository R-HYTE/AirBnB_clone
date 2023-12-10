#!/usr/bin/env python3
'''
Module with the FileStorage class
'''
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:
    '''
    Serialize instances to JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store instances.
    '''
    __file_path = "file.json"
    __objects = {}

    # Mapping class names to actual classes
    CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        '''
        Return a dictionary containing all stored instances.

        Returns:
            dict: A dictionary with instance keys and corresponding objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Add a new instance to the storage.

        Args:
            obj: The instance to be added.
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialize stored instances and save them to the JSON file.
        '''
        serialized_objects = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        '''
        Deserialize instances from the JSON file and add them to the storage.
        If the file does not exist, do nothing.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)

            for key, obj_data in obj_dict.items():
                class_name = obj_data["__class__"]
                del obj_data["__class__"]

                if class_name in FileStorage.CLASSES:
                    obj_instance = FileStorage.CLASSES[class_name](**obj_data)
                    self.new(obj_instance)
        except FileNotFoundError:
            return
