#!/usr/bin/python3
""" This odule contains class Base """
import json
import os.path
import csv
import turtle


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
        """ Save From File csv """
        try:
            data_list = [x.to_dictionary() for x in list_objs]
        except TypeError:
            data_list = '[]'
        keys = data_list[0].keys()
        with open(cls.__name__ + '.csv', 'w') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(data_list)

    @staticmethod
def draw(list_of_rectangles, list_of_squares):
    """ Draw Rectangles and Squares using turtle """
    turt = turtle.Turtle()
    turt.screen.bgcolor("#b7312c")
    turt.pensize(3)
    turt.shape("turtle")

    turt.color("#ffffff")
    for rect in list_of_rectangles:
        turt.showturtle()
        turt.up()
        turt.goto(rect.x, rect.y)
        turt.down()
        for _ in range(2):
            turt.forward(rect.width)
            turt.left(90)
            turt.forward(rect.height)
            turt.left(90)
        turt.hideturtle()

    turt.color("#b5e3d8")
    for sq in list_of_squares:
        turt.showturtle()
        turt.up()
        turt.goto(sq.x, sq.y)
        turt.down()
        for _ in range(2):
            turt.forward(sq.width)
            turt.left(90)
            turt.forward(sq.height)
            turt.left(90)
        turt.hideturtle()

    turtle.exitonclick()

