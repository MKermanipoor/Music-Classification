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
    note_mode = notes % 12
    hit, bins = np.histogram(note_mode, bins=range(0, 12))
    feature.extend(hit)
    octav = np.ceil(notes / 12)
    hit, bins = np.histogram(octav, bins=range(0, 10))
    feature.extend(hit)
    return feature

def get_more_data(notes, extend):
    note_length = len(notes)
    more_data = []
    min_note_length = 300
    for i in range(0, extend):
        rand_length = np.random.randint(min_note_length, note_length)
        start_index = np.random.randint(0, note_length-rand_length)
        more_data.append(notes[start_index:rand_length + start_index])
    return more_data


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
                notes = get_note(MidiFile(path))
                for more_date in get_more_data(notes, 500):
                    feature = get_feature(more_date)
                    feature.append(label)
                    feature.append(name)
                    features.append(feature)
            except:
                print(name)
    with open(data_source_path + 'features-v2.csv', 'w', newline='') as output:
        wr = csv.writer(output, quoting=csv.QUOTE_ALL)
        wr.writerows(features)
