from matplotlib import pyplot as plt
from lib.GestureParser import GestureParser, Point, ScaleMode


def main():
    path = "gestures/"
    fileprefix = "myfile"

    # load file and create point list
    points = parse_files(open_file(path + fileprefix + str(2)))
    point_list = [Point(p[0], p[1]) for p in points]

    # magic happens here
    gp = GestureParser(ScaleMode.NO_SCALE, 32)
    image = gp.convert_point_list_to_image(point_list)

    # show array
    plt.imshow(image)
    plt.show()


def open_file(name):
    """
    open file by name
    :param name:
    :return:
    """
    return [line.rstrip('\n') for line in open(name)]


def parse_files(lines):
    """
    parse files
    :param lines:
    :return:
    """
    ret = []
    for line in lines:
        ret.append([float(x) for x in line.split(' ')])
    return ret


if __name__ == '__main__':
    main()
