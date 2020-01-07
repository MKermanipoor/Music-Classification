from tqdm import tqdm
import csv

label_dic = {'3': 0, '5': 1, '6': 2, '7': 3, '9': 4}

if __name__ == '__main__':
    label_path = 'Data/trainLabels.txt'
    output_path = 'Data/trainLabels.csv'

    file = open(label_path, 'r')
    data = [['name', 'label']]
    for line in tqdm(file):
        index = line.rfind(',')
        name = line[0:index]
        label = label_dic[line[index + 1: -1]]
        data.append([name, label])

    with open(output_path, 'w', newline='') as output:
        wr = csv.writer(output, quoting=csv.QUOTE_ALL)
        wr.writerows(data)
