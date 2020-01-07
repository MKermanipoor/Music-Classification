from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data_source_path = 'Data/MIDI_Genres/train_set/features.csv'

dataset = pd.read_csv(data_source_path)
x = dataset.iloc[:, 0:-2].values
y = dataset.iloc[:, -2].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

#%% train
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(x_train, y_train)

# %% validate
y_predict = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_predict)

# %% save
from sklearn.externals import joblib
joblib.dump(classifier, 'learners/svm.sav')
