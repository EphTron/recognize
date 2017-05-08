from .Dataset import Dataset
from os import path, listdir
from skimage import io
import numpy as np


def load_datasets(directory, size_exponent):
    """
    loads datasets from directory with a given size exponent
    :param directory: specifies the directory where the samples are stored
    :param size_exponent: size to load the sample images (preferably 2**n)
    :return: list of datasets, set of targets
    """
    # get dataset folders in base dir
    basedir = [d for d in listdir(directory) if not path.isfile(d)]

    # load files
    sets = []
    targets = []
    for folder in basedir:
        # create path
        dataset_path = path.join(directory, folder)
        d = Dataset(data_path=dataset_path,
                    target=folder,
                    size_exponent=size_exponent)
        targets.append(folder)

        d.load()
        sets.append(d)

    return sets, list(set(targets))


def ndarray2image(array, path, filename):
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

    ## saves the image
    io.imsave(path + filename, array)


def qimage2ndarray(image):
    """
    converts a qimage to numpy ndarray
    :param image:
    :return:
    """

    # get width and height of image
    width = image.width()
    height = image.height()

    # get pointer to image data
    ptr = image.constBits()
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data

    return arr
