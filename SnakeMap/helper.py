import matplotlib.pyplot as plt
from IPython import display
import csv
import numpy as np

temp_list = []
temp_list2 = []
with open('2h,-12,+10,h256,r1000.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp_list = np.array(row)
with open('2h,-15,+8,h256,r1000.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp_list2 = np.array(row)

new_list = [float(x) for x in temp_list]
new_list2 = [float(x) for x in temp_list2]

                

plt.ion()

def plot(scores, mean_scores):
    with open('2h,-12,+12,h128,r1000.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(mean_scores)
    
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.plot(new_list)
    plt.plot(new_list2)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)