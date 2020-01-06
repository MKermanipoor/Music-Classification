import matplotlib.pyplot as plt
import numpy as np


def draw(notes):
    plt.plot(notes)
    plt.show()


def draw_histogram(notes):
    hit, bins = np.histogram(notes, bins=range(0, 128))
    plt.plot(bins[0:-1], hit)
    plt.show()
