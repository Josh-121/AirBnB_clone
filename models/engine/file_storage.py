#!/usr/bin/python3
import json
class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        value = obj.to_dict()
        self.__objects[key] = value
    def save(self):
        path = self.__file_path
        with open(path, 'w') as file:
            json.dump(self.__objects, file)
    def reload(self):
        path = self.__file_path
        try:
            with open(path, 'r') as file:
                self.__objects = json.load(file)
        except:
            pass
