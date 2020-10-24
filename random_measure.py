import math
import numpy as np
import matplotlib.pyplot as plt
import random as r
import statistics as stat

rows, cols = 2, 5
fig, ax = plt.subplots(rows, cols,
                       sharex='col', 
                       sharey='row',
                       figsize=(14,7))

totalrolls = []
ot = 0

while (ot < 100):
    t = 0
    time = []
    rolls = []
    while (t < 1000):
        x = r.randint(1,10)
        rolls.append(x)
        time.append(t)
        t += 1
    count = 1
    
    while count < 11:
        totalrolls.append(rolls.count(count))
        count += 1
    ot += 1

for row in range(2):
    for col in range(5):   
        #graph results of rolls
        ax[row, col].scatter(range(100), totalrolls[(row * 5 + col)::10], s = 0.5,
                          c = 'black')
        #graphs mean
        ax[row, col].plot(range(100), [stat.mean(totalrolls[(row * 5 + col)::10])]*100,
                          c = 'orange')
        #graphs standard deviation top
        ax[row, col].plot(range(100), [stat.stdev(totalrolls[(row * 5 + col)::10]) + stat.mean(totalrolls[(row * 5 + col)::10])]*100, 
                          dashes=[5,5],
                          c = 'blue')
         #graphs standard deviation bottom
        ax[row, col].plot(range(100), [stat.mean(totalrolls[(row * 5 + col)::10]) - stat.stdev(totalrolls[(row * 5 + col)::10])]*100,
                          dashes=[5,5],
                          c = 'blue')
        #adds mean text
        ax[row, col].text(15, stat.mean(totalrolls[(row * 5 + col)::10]) + 2, 
                          'Mean: ' + str(stat.mean(totalrolls[(row * 5 + col)::10])) + '±' + str(round(stat.stdev(totalrolls[(row * 5 + col)::10]), 2)),
                          color="black",
                          fontsize=10)

        ax[row, col].set_title('For a roll of ' + str(row * 5 + col + 1))
        ax[row, col].set_xlabel('Trial #')
        ax[row, col].set_ylabel('Total Hits')
 
plt.show()
