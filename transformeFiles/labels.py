import pandas as pd
from tqdm import tqdm
import csv

label_path = 'Data/trainLabels.txt'
output_path = 'Data/trainLabels.csv'

file = open(label_path, 'r')
data = []
for line in tqdm(file):
    index = line.rfind(',')
    name = line[0:index]
    label = line[index + 1: -1]
    data.append([name, label])

with open(output_path, 'w',  newline='') as output:
    wr = csv.writer(output, quoting=csv.QUOTE_ALL)
    wr.writerows(data)
