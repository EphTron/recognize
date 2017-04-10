import operator
import math
import numpy as np
from enum import Enum


class Point:
    instances = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = Point.instances

        Point.instances += 1

    def __str__(self):
        return "<Point id: " + str(self.id) + " _x: " + str(self.x) + " y: " + str(self.y) + ">"


class ScaleMode(Enum):
    NO_SCALE = 1
    SCALE_MAX = 2


class GestureParser:
    def __init__(self, SCALE_MODE, IMAGE_DIMENSION):
        """
        c'tor
        :param POINT_LIST:
        :param SCALE_MODE:
        :param IMAGE_DIMENSION:
        """
        self.scale_mode = SCALE_MODE
        self.img_dim = IMAGE_DIMENSION

    def convert_point_list_to_image(self, point_list):
        """
        parse image from point list to numpy nd array
        :return: ndarray
        """

        # create dict containing x and y values
        x_dict, y_dict = {}, {}
        for p in point_list:
            x_dict[p.id] = p.x
            y_dict[p.id] = p.y

        # get indices of min and max x values
        min_x_idx = min(x_dict.items(), key=operator.itemgetter(1))[0]
        max_x_idx = max(x_dict.items(), key=operator.itemgetter(1))[0]

        # get min and max x values; calculate maximum distance
        min_x = x_dict[min_x_idx]
        max_x = x_dict[max_x_idx]
        max_distance_x = math.fabs(min_x) + math.fabs(max_x)

        # get indices of min and max x values
        min_y_idx = min(y_dict.items(), key=operator.itemgetter(1))[0]
        max_y_idx = max(y_dict.items(), key=operator.itemgetter(1))[0]

        # get min and max x values; calculate maximum distance
        min_y = y_dict[min_y_idx]
        max_y = y_dict[max_y_idx]
        max_distance_y = math.fabs(min_y) + math.fabs(max_y)

        # create new internet (aka image)
        image = [[0 for j in range(0, self.img_dim)] for i in range(0, self.img_dim)]

        p_x, p_y = 0
        for row_idx in range(len(image)):
            for col_idx in range(len(image[0])):
                for p in point_list:

                    # scale the points to the maximum
                    if self.scale_mode == ScaleMode.SCALE_MAX:

                        p_x = int(map_to(p.x, min_x, max_x, 0, self.img_dim))
                        p_y = int(map_to(p.y, min_y, max_y, 0, self.img_dim))

                    # keep image dimensions and align the detected gesture to the left hand side
                    elif self.scale_mode == ScaleMode.NO_SCALE:

                        if max_distance_x > max_distance_y:
                            ratio = (max_distance_y * 100) / max_distance_x
                            p_x = int(map_to(p.x, min_x, max_x, 0, self.img_dim))
                            p_y = int(map_to(p.y, min_y, max_y, 0, self.img_dim) * ratio / 100)
                        else:
                            ratio = (max_distance_x * 100) / max_distance_y
                            p_x = int(map_to(p.x, min_x, max_x, 0, self.img_dim) * ratio / 100)
                            p_y = int(map_to(p.y, min_y, max_y, 0, self.img_dim))

                    # write black pixel if the indices match
                    if (p_x == row_idx and p_y == col_idx):
                        image[row_idx][col_idx] = 16

        # cast image to np array and return
        return np.asarray(image)


def map_to(value, from_min, from_max, to_min, to_max):
    """
    maps the given value from base range to new range
    :param value:
    :param from_min:
    :param from_max:
    :param to_min:
    :param to_max:
    :return:
    """
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min
