#!/usr/bin/python3
""" This odule contains class Base """
import json
import os.path
import csv


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert python object to JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ JSON to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """makes instance"""
        if cls.__name__ is 'Square':
            newcreate = cls(1)
        if cls.__name__ is 'Rectangle':
            newcreate = cls(1, 1)
        if newcreate:
            newcreate.update(**dictionary)
            return newcreate

    @classmethod
    def load_from_file(cls):
        """ Load From File cls """
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in list_dicts]

    @classmethod
    def load_from_file_csv(cls):
        """ Load From File csv """
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []
        else:
            with open(cls.__name__ + '.csv', 'r') as file:
                reader = csv.DictReader(file)
                csv_data = [row for row in reader]
                for row in csv_data:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except ValueError:
                            pass
            return [cls.create(**dic) for dic in csv_data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save To File csv """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            data_template = [0, 0, 0, 0, 0]
            key_names = ['id', 'width', 'height', 'x', 'y']
        else:
            data_template = ['0', '0', '0', '0']
            key_names = ['id', 'size', 'x', 'y']

        data_matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for index in range(len(key_names)):
                    data_template[index] = obj.to_dictionary()[key_names[index]]
                data_matrix.append(data_template[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(data_matrix)
