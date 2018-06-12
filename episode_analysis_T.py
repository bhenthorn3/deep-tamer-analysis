## Collecting data from both the feedback files and the episode data files 
##
## GAME -- Tetris

import pandas as pd
import numpy as np
from numpy import *
from Data_T import added_T
import statistics as st
import math
import csv

scores = []
subs = [21, 22, 23, 24, 25, 26, 27, 28]

for i in range(0, len(subs)):
	i_str = str(subs[i])
	file_name = ("run_.-tag-Per_Episode_episode_reward-" + i_str + "T.csv")
	f = open(file_name)
	csv_f = csv.reader(f)
	score = []	
	for j in csv_f:
		if j[2] == 'Value':
			hi = 1
		else:
			score.append(float(j[2]))
	
	scores.append(score[-1])

scr_avg = st.mean(scores)
print (scores)
print ('The average game score was', (scr_avg))
print ('The lowest game score was', (min(scores)))
print ('The largest game score was', (max(scores)))

amt_feed = np.sum(added_T, axis=1)
feed_avg = st.mean(amt_feed)
print (amt_feed)
print ('The average amount of feedback given was', (feed_avg))
print ('The lowest amonut of feedback given was', (min(amt_feed)))
print ('The largest amount of feedback given was', (max(amt_feed)))

f.close()
