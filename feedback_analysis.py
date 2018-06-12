import csv
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from Data_B import avgB, xB, dataP_B, dataN_B, added_B
from Data_MPM import avgMPM, xMPM, dataP_MPM, dataN_MPM, added_MPM
from Data_T import avgT, xT, dataP_T, dataN_T, added_T
from Data_TV import avgTV, xTV, dataP_TV, dataN_TV, added_TV

print ('The Bowling average was %1.5f' % (avgB))
print ('The MsPacMan average was %1.5f' % (avgMPM))
print ('The Tetris average was %1.5f' % (avgT))
print ('The Vanilla Tetris average was %1.5f \n' % (avgTV))

tot_avg = (avgB + avgMPM + avgT + avgTV)/4
if tot_avg > 1:
	print('The average of the four games (%1.5f) tends towards more positive feedback being given \n' % (tot_avg))

if tot_avg < 1:
	print('The average of the four games (%1.5f) tends towards more negative feedback being given \n' % (tot_avg))

if tot_avg == 1:
	print('The average of the four games indicates an equal number of positive and negative feedback was given \n')


### Getting the means and standard deviations of each game
### Game: Bowling

Tot_LB = []
Both_B = []
Neg_B = []
Pos_B = []
NegStd_B = []
PosStd_B = []
for i in range(0, 10):
	current1 = dataP_B[:, i]	
	a = st.mean(current1)
	b = st.stdev(current1)
	Pos_B.append(a)
	PosStd_B.append(b)
	current2 = dataN_B[:, i]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_B.append(c)
	NegStd_B.append(d)
	current3 = added_B[:, i]
	Both_B.append(current3)
	Tot_LB.append(a+c)

### Game: MsPacMan

Tot_LMPM = []
Both_MPM = []
Neg_MPM = []
Pos_MPM = []
NegStd_MPM = []
PosStd_MPM = []
for i in range(0, 10):
	current1 = dataP_MPM[:, i]	
	a = st.mean(current1)
	b = st.stdev(current1)
	Pos_MPM.append(a)
	PosStd_MPM.append(b)
	current2 = dataN_MPM[:, i]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_MPM.append(c)
	NegStd_MPM.append(d)
	current3 = added_MPM[:, i]
	Both_MPM.append(current3)
	Tot_LMPM.append(a+c)

### Game: Tetris

Tot_LT = []
Both_T = []
Neg_T = []
Pos_T = []
NegStd_T = []
PosStd_T = []
for i in range(0, 10):
	current1 = dataP_T[:, i]	
	a = st.mean(current1)
	b = st.stdev(current1)
	Pos_T.append(a)
	PosStd_T.append(b)
	current2 = dataN_T[:, i]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_T.append(c)
	NegStd_T.append(d)
	current3 = added_T[:, i]
	Both_T.append(current3)
	Tot_LT.append(a+c)

### Game: Vanilla Tetris

Tot_LTV = []
Both_TV = []
Neg_TV = []
Pos_TV = []
NegStd_TV = []
PosStd_TV = []
for i in range(0, 10):
	current1 = dataP_TV[:, i]	
	a = st.mean(current1)
	b = st.stdev(current1)
	Pos_TV.append(a)
	PosStd_TV.append(b)
	current2 = dataN_TV[:, i]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_TV.append(c)
	NegStd_TV.append(d)
	current3 = added_TV[:, i]
	Both_TV.append(current3)
	Tot_LTV.append(a+c)

### Stacked Bar Graph - Bowling
N = 10
labels = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, Neg_B, width, yerr=NegStd_B, color='r', ecolor='crimson', capsize=8)
p2 = plt.bar(ind, Pos_B, width, bottom=Neg_B, yerr=PosStd_B, color='g', ecolor='darkgreen', capsize=8)

plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.title('Comparison of Feedback of Atari Games - Bowling')
plt.xticks(ind, labels)
plt.yticks(np.arange(-2, 20, 1))
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))

plt.show()

### Stacked Bar Graph Subplot 
plt.subplot(221)
plt.bar(ind, Neg_B, width, yerr=NegStd_B, color='r', ecolor='crimson', capsize=8)
plt.bar(ind, Pos_B, width, bottom=Neg_B, yerr=PosStd_B, color='g', ecolor='darkgreen', capsize=8)
plt.xticks(ind, labels)
plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))
plt.title('Bowling')		## Top left

plt.subplot(222)
plt.bar(ind, Neg_MPM, width, yerr=NegStd_MPM, color='r', ecolor='crimson', capsize=8)
plt.bar(ind, Pos_MPM, width, bottom=Neg_MPM, yerr=PosStd_MPM, color='g', ecolor='darkgreen', capsize=8)
plt.xticks(ind, labels)
plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))
plt.title('MsPacMan')		## Top right

plt.subplot(223)
plt.bar(ind, Neg_T, width, yerr=NegStd_T, color='r', ecolor='crimson', capsize=8)
plt.bar(ind, Pos_T, width, bottom=Neg_T, yerr=PosStd_T, color='g', ecolor='darkgreen', capsize=8)
plt.xticks(ind, labels)
plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))
plt.title('Tetris')		## Bottom Left

plt.subplot(224)
plt.bar(ind, Neg_TV, width, yerr=NegStd_TV, color='r', ecolor='crimson', capsize=8)
plt.bar(ind, Pos_TV, width, bottom=Neg_TV, yerr=PosStd_TV, color='g', ecolor='darkgreen', capsize=8)
plt.xticks(ind, labels)
plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))
plt.title('Vanilla Tetris')		## Bottom right

plt.tight_layout()

plt.show()

### Plots of Bowling data
plt.subplot(121)
plt.plot(labels, Both_B)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Bowling (Individuals)')		## Top left

plt.subplot(122)
plt.plot(labels, Tot_LB)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Bowling (Averaged)')		## Top right

plt.show()

### Plots of MsPacMan data
plt.subplot(121)
plt.plot(labels, Both_MPM)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('MsPacMan (Individuals)')		## Top left

plt.subplot(122)
plt.plot(labels, Tot_LMPM)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('MsPacMan (Averaged)')		## Top right

plt.show()

### Plots of Tetris data
plt.subplot(121)
plt.plot(labels, Both_T)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Tetris (Individuals)')		## Top left

plt.subplot(122)
plt.plot(labels, Tot_LT)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Tetris (Averaged)')		## Top right

plt.show()

### Plots of Vanilla Tetris data
plt.subplot(121)
plt.plot(labels, Both_TV)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Vanilla Tetris (Individuals)')		## Top left

plt.subplot(122)
plt.plot(labels, Tot_LTV)
plt.xlabel('Time Steps')
plt.ylabel('Amount of Feedback')
plt.title('Vanilla Tetris (Averaged)')		## Top right

plt.show()
