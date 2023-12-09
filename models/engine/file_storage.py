#!/usr/bin/env python3
'''
Module with the FileStorage class
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    Serialize instances to JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store instances.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Return a dictionary containing all stored instances.

        Returns:
            dict: A dictionary with instance keys and corresponding objects.
        '''
        class_name_objects = {}
        for key, obj in FileStorage.__objects.items():
            class_name = key.split('.')[0]
            if class_name not in class_name_objects:
                class_name_objects[class_name] = {}
            class_name_objects[class_name][key] = obj
        return class_name_objects

    def new(self, obj):
        '''
        Add a new instance to the storage.

        Args:
            obj: The instance to be added.
        '''
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialize stored instances and save them to the JSON file.
        '''
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        '''
        Deserialize instances from the JSON file and add them to the storage.
        If the file does not exist, do nothing.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for obj_data in data.values():
                cls_name = obj_data["__class__"]
                del obj_data["__class__"]
                
                # Dynamically import the class using globals()
                model_class = globals()[cls_name]

                # Create an instance of the class and add it to the storage
                self.new(model_class(**obj_data))
        except FileNotFoundError:
            return
