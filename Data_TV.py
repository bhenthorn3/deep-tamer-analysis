import csv
import numpy as np
from numpy import *

subs = [21, 22, 23, 24, 25, 26, 27, 28]

ratios = []
array_lengths = []

for i in subs:
	i_str = str(i)
	file_name = ("run_.-tag-Human_feedback-sub" + i_str + "TV.csv")

	print('This is subject {0}s Vanilla Tetris data:'.format(i_str) )

	f = open(file_name)

	csv_f = csv.reader(f)

	pos_feed = []
	neg_feed = []

	for row in csv_f:
		pos_feed.append(row[2] > '0')
		pos = len(list(filter(None, pos_feed)))

		neg_feed.append(row[2] < '0')
		neg = len(list(filter(None, neg_feed)))

	array_lengths.append(len(pos_feed))

	signals = pos - neg
	num = float(pos/neg)

	if signals > 0: 
		print ('%d more positive feedback signal(s) were given than negative' % (signals))

	if signals < 0:
		print ('%d more negative feedback signal(s) were given than positive' % (signals))

	if signals == 0:
		print ('An equal number of positive and negative feedback signals were given')

	print ('The ratio of positive to negative feedback signals: %1.5f \n' % (num))

	ratios.append(num)
	avgTV = sum(ratios)/len(ratios)

xTV = max(array_lengths) - 1

step_size = int(xTV/10)

print(step_size)

print(array_lengths)

print(xTV)

print(avgTV)
pos_feed = []
pos_step = []

for i in subs:
	i_str = str(i)
	file_name = ("run_.-tag-Human_feedback-sub" + i_str + "TV.csv")
#	print('This is subject {0}s Vanilla Tetris data:'.format(i_str) )
	f = open(file_name)
	csv_f = csv.reader(f)
	for row in csv_f:
		pos_feed.append(row[2] > '0')
	del pos_feed[0]
	if len(pos_feed) < xTV:
		extra = [False] * (xTV - len(pos_feed))
		pos_feed = pos_feed + extra
	while not pos_feed == 0:
		pos_list = []
#		print (len(pos_feed))
		if len(pos_feed) < step_size:
			extra = [False] * (step_size - len(pos_feed))
			pos_feed = pos_feed + extra
#			print(len(pos_feed))
			for j in range(0, step_size):	
				a = pos_feed[j]
				pos_list.append(a)
			del pos_feed[0:step_size]
#			print(len(pos_list))
		if len(pos_feed) == 0:
			break
		else:
			for j in range(0, step_size):	
				a = pos_feed[j]
				pos_list.append(a)
			del pos_feed[0:step_size]
#			print(len(pos_list))
		
		pos = len(list(filter(None, pos_list)))
		pos_step.append(pos)

#print(pos_step)


neg_feed = []
neg_step = []

for i in subs:
	i_str = str(i)
	file_name = ("run_.-tag-Human_feedback-sub" + i_str + "TV.csv")
#	print('This is subject {0}s Vanilla Tetris data:'.format(i_str) )
	f = open(file_name)
	csv_f = csv.reader(f)		
	for row in csv_f:
		neg_feed.append(row[2] < '0')
	del neg_feed[0]	
	if len(neg_feed) < xTV:
		extra = [False] * (xTV - len(neg_feed))
		neg_feed = neg_feed + extra
	while not neg_feed == 0:
		neg_list = []
#		print (len(neg_feed))
		if len(neg_feed) < step_size:
			extra = [False] * (step_size - len(neg_feed))
			neg_feed = neg_feed + extra
#			print(len(neg_feed))
			for j in range(0, step_size):	
				b = neg_feed[j]
				neg_list.append(b)
			del neg_feed[0:step_size]
#			print(len(neg_list))
		if len(neg_feed) == 0:
			break
		else:
			for j in range(0, step_size):	
				b = neg_feed[j]
				neg_list.append(b)
			del neg_feed[0:step_size]
#			print(len(neg_list))
			
		neg = len(list(filter(None, neg_list)))
		neg_step.append(neg)

#print(neg_step)

dataP = np.array(pos_step)
dataN = np.array(neg_step)

shape = (len(subs), 10)

dataP_TV = reshape(dataP, shape)
dataN_TV = reshape(dataN, shape)

print(dataP_TV)
print(dataN_TV)


f.close()





