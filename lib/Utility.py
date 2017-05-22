#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 10.05.17 12:02
@author: ephtron
"""

import numpy as np
from os import listdir, path
from PyQt5 import QtGui

from lib.Dataset import Dataset


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


def qimage_to_image_array(qimage):
    # using code from https://github.com/hmeine/qimage2ndarray
    from qimage2ndarray import qimage2ndarray
    ndarray_img = qimage2ndarray.rgb_view(qimage)
    ndarray_color_to_grey(ndarray_img)
    return ndarray_img

def ndarray_color_to_grey(ndarray):
    grey_ndarray = np.zeros((ndarray.shape[0],ndarray.shape[1]))
    print(print(ndarray[0:5, 0:5]))
    for r in range(ndarray.shape[0]):
        for c in range(ndarray.shape[1]):
            if np.array_equal(ndarray[r, c], [255, 255, 255]):
                grey_ndarray[r, c] = 255

    print(grey_ndarray[0:5, 0:5])
    return grey_ndarray


