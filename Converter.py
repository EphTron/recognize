import numpy as np
import operator
from matplotlib import pyplot as plt

IMAGE_DIMENSIONS = (255, 255)


def main():
    path = "gestures/"
    fileprefix = "myfile"

    # parse points
    points = parse_files(open_file(path + fileprefix + str(1)))
    point_list = [Point(p[0], p[1]) for p in points]

    # create dict containing x and y values
    x_dict, y_dict = {}, {}
    for p in point_list:
        x_dict[p.id] = p.x
        y_dict[p.id] = p.y

    # get min and max values
    min_x = min(x_dict.items(), key=operator.itemgetter(1))[0]
    max_x = max(x_dict.items(), key=operator.itemgetter(1))[0]

    print(x_dict[12])
    foo = map_to(x_dict[12], min_x, max_x, 1, 255)
    print(foo)

    min_y = min(y_dict.items(), key=operator.itemgetter(1))[0]
    max_y = max(y_dict.items(), key=operator.itemgetter(1))[0]


def map_to(value, in_start, in_end, out_start, out_end):
    return out_start - ((out_end - out_start) / (in_end - in_start)) * (value - in_start)


def open_file(name):
    return [line.rstrip('\n') for line in open(name)]


def parse_files(lines):
    ret = []
    for line in lines:
        ret.append([float(x) for x in line.split(' ')])
    return ret


class Point:
    instances = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = Point.instances

        Point.instances += 1

    def __str__(self):
        return "<Point id: " + str(self.id) + " _x: " + str(self.x) + " y: " + str(self.y) + ">"


if __name__ == '__main__':
    main()


