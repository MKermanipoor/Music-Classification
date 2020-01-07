from mido import MidiFile
import matplotlib.pyplot as plt
import numpy as np
import visualize.midi as vm
from tqdm import tqdm
import os
import pandas as pd
import csv


def get_note(midi_file):
    notes = []
    for track in midi_file.tracks:
        for msg in track:
            if hasattr(msg, 'note') and hasattr(msg, 'velocity'):
                if msg.velocity != 0:
                    notes.append(msg.note)
    return np.array(notes)


def get_feature(notes):
    feature = [notes.min(), notes.max(), notes.mean(), np.median(notes)]
    hit, bins = np.histogram(notes, bins=range(0, 128))
    feature.extend(hit)
    return feature


if __name__ == '__main__':
    data_source_path = 'Data/MIDI_Genres/train_set/'

    features = []
    labels = pd.read_csv('Data/trainLabels.csv')
    labels = labels.set_index('name')

    for name, label in tqdm(labels.iterrows()):
        label = label['label']
        path = data_source_path + name
        if os.path.exists(path):
            try:
                feature = get_feature(get_note(MidiFile(path)))
                feature.append(label)
                feature.append(name)
                features.append(feature)
            except:
                print(name)
    with open(data_source_path + 'features.csv', 'w', newline='') as output:
        wr = csv.writer(output, quoting=csv.QUOTE_ALL)
        wr.writerows(features)
