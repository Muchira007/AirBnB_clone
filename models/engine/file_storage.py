import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing).
        If the file doesn’t exist, no exception should be raised.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Assume class_name is a valid class
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
