from tqdm import tqdm
import csv

label_path = 'Data/testLabels.txt'
output_path = 'Data/testLabels.csv'

file = open(label_path, 'r')
data = [['name', 'label']]
for line in tqdm(file):
    index = line.rfind(',')
    name = line[0:index]
    label = line[index + 1: -1]
    data.append([name, label])

with open(output_path, 'w',  newline='') as output:
    wr = csv.writer(output, quoting=csv.QUOTE_ALL)
    wr.writerows(data)
