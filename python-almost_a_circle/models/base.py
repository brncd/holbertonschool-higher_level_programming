#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        import json
        filename = "{}.json".format(list_objs[0].__class__.__name__)
        arg = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            if arg is None or arg == [] or len(arg) == 0:
                f.write("[]")
            else:
                f.write(Base.to_json_string(arg))
