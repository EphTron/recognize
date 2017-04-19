from sklearn import svm, metrics
import numpy as np


class ShapeDetector:
    def __init__(self, datasets):
        """
        c'tor
        :param datasets:
        """
        # create classifier
        self.classifier = svm.SVC(gamma=0.001)

        # initialize
        self.initialize(datasets)

    def initialize(self, datasets):
        """
        initialize shape detector, shaping the data, learning according to input datasets
        :param datasets:
        :return:
        """
        self.datasets = datasets
        images = join_datasets([d.images for d in datasets])
        targets = join_datasets([d.targets for d in datasets])

        # determine number of samples
        n_samples = len(images)

        # reshape data
        data = images.reshape((n_samples, -1))

        # learn from dataset
        self.classifier.fit(data, targets)

    def predict(self, targets):
        """
        predict input targets using svc's predict function
        :param targets:
        :return:
        """
        return self.classifier.predict(targets)

    def report(self, targets, results):
        """
        returns the classifier and a generated classification report
        :param targets: input list of targets to predict (need to be learned first)
        :param results: input list of predicted elements
        :return:
        """
        report = metrics.classification_report(targets, results)
        return self.classifier, report


def join_datasets(datasets):
    """
    join datasets into one
    :param datasets:
    :return:
    """
    first = datasets[0]
    for i in range(1, len(datasets)):
        first += datasets[i]
    return np.asarray(first)
