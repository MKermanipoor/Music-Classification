from mido import MidiFile
import matplotlib.pyplot as plt
import numpy as np
import visualize.midi as vm


def get_note(midi_file):
    notes = []
    for track in midi_file.tracks:
        for msg in track:
            if hasattr(msg, 'note') and hasattr(msg, 'velocity'):
                if msg.velocity != 0:
                    notes.append(msg.note)
    # plt.plot(notes, 'r--')
    # plt.show()
    return np.array(notes)


def get_feature(notes):
    feature = []
    # feature.append(notes.min())
    # feature.append(notes.max())
    # feature.append(notes.mean())
    # feature.append(np.median(notes))
    hit, bins = np.histogram(notes, bins=range(0, 128))
    return feature


if __name__ == '__main__':
    notes = get_note(MidiFile('Data/MIDI_Genres/train_set/7thst.mid'))
    print(get_feature(notes))
    vm.draw(notes)
    vm.draw_histogram(notes)
