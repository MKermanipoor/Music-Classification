from sklearn.svm import SVC
import transformeFiles.midi as tm
import pandas as pd
from mido import MidiFile
import os
from tqdm import tqdm

data_source_path = 'Data/MIDI_Genres/train_set/'

features = []

for file in tqdm(os.listdir(data_source_path)):
    if file.endswith('.mid'):
        try:
            feature = tm.get_feature(tm.get_note(MidiFile(os.path.join(data_source_path, file))))
            features.append(features)
        except:
            print(file)
