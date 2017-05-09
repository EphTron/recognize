import operator
import math
import numpy as np
from skimage import io
from enum import Enum
import matplotlib.pyplot as plt


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

    def open_gpl_file(self, file_name):
        result = [line.rstrip('\n') for line in open(file_name)]
        print(result)
        return result

    def prepare_lines(self, lines):
        ret = []
        for line in lines:
            ret.append([float(x) for x in line.split(' ')])
        print(ret)
        return ret

    def convert_gpl_to_pointlist(self, path, file_name):

        points = self.prepare_lines(self.open_gpl_file(path + file_name))

        point_list = [Point(p[0], p[1]) for p in points]
        print(point_list)
        return point_list

    def convert_point_list_to_scaled_image_array(self, point_list):
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
        image = [[0 for j in range(0,self.img_dim)] for i in range(0,self.img_dim)]

        p_x = 0
        p_y = 0
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
                        image[row_idx][col_idx] = 255

        # cast image to np array and return
        # plt.figure(1)
        plt.imshow(image)
        plt.show()
        return np.asarray(image)


    def save_array_as_image(self, array, path, filename):
        """
        saves the input array to the given destination
        :param array: numpy nd array
        :param path: local path to save the image
        :param filename: name of the file including extension
        :return:
        """

        # if there is no slash at the end of the destination
        if path[-1] != "/":
            path = path + "/"
        print(path + filename)
        ## saves the image
        io.imsave(path + filename, array)


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
