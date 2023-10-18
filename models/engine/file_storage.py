#!/usr/bin/env python3
from models.review import Review
from models.base_model import BaseModel
import json


class FileStorage(object):
    """
        a class FileStorage that serializes instances to a JSON
        file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with
            key <obj class name>.id
        """

        dic = self.__objects
        name = obj.__class__.__name__
        id = obj.id
        string = "{}.{}".format(name, id)
        dic.update({string: obj})

    def save(self):
        """
            serializes __objects to the
            JSON file (path: __file_path)
        """

        dic = self.__objects
        path = self.__file_path
        json_dict = {}
        for key, value in dic.items():
            json_dict[key] = value.to_dict()
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing.
            If the file doesn�~@~Yt exist,
            no exception should be raised)
        """

        path = self.__file_path
        obj = self.__objects
        json_dict = {}
        try:
            with open(path, mode='r', encoding='utf-8') as file:
                json_dict.update(json.loads(file.read()))
            for key, value in json_dict.items():
                obj[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
