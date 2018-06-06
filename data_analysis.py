import csv
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
from Data_B import avgB, xB, dataP_B, dataN_B
from Data_MPM import avgMPM, xMPM, dataP_MPM, dataN_MPM
from Data_T import avgT, xT, dataP_T, dataN_T
from Data_TV import avgTV, xTV, dataP_TV, dataN_TV

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
for j in range(0, 10):
	current2 = dataN_B[:, j]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_B.append(c)
	NegStd_B.append(d)

### Game: MsPacMan

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
for j in range(0, 10):
	current2 = dataN_MPM[:, j]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_MPM.append(c)
	NegStd_MPM.append(d)

### Game: Tetris

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
for j in range(0, 10):
	current2 = dataN_T[:, j]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_T.append(c)
	NegStd_T.append(d)

### Game: Vanilla Tetris

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
for j in range(0, 10):
	current2 = dataN_TV[:, j]
	c = st.mean(current2)
	d = st.stdev(current2)
	Neg_TV.append(c)
	NegStd_TV.append(d)
	

### Stacked Bar Graph setup
N = 10
labels = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, Neg_B, width, yerr=NegStd_B)
p2 = plt.bar(ind, Pos_B, width,
             bottom=Neg_B, yerr=PosStd_B)

plt.xlabel('Time Steps')
plt.ylabel('Number of Feedback Signals')
plt.title('Comparison of Feedback of Atari Games - Bowling')
plt.xticks(ind, labels)
plt.yticks(np.arange(-2, 20, 1))
plt.legend((p1[0], p2[0]), ('Negative', 'Positive'))

plt.show()

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

### Subplot 
f, axarr = plt.subplots(2, 2)
axarr[0, 0].bar(ind, Neg_B, width, yerr=NegStd_B)
axarr[0, 0].bar(ind, Pos_B, width, bottom=Neg_B, yerr=PosStd_B)
axarr[0, 0].legend((p1[0], p2[0]), ('Negative', 'Positive'))
axarr[0, 0].set_title('Bowling')		## Top left


axarr[0, 1].bar(ind, Neg_MPM, width, yerr=NegStd_MPM)
axarr[0, 1].bar(ind, Pos_MPM, width, bottom=Neg_MPM, yerr=PosStd_MPM)
axarr[0, 1].legend((p1[0], p2[0]), ('Negative', 'Positive'))
axarr[0, 1].set_title('MsPacMan')		## Top right


axarr[1, 0].bar(ind, Neg_T, width, yerr=NegStd_T)
axarr[1, 0].bar(ind, Pos_T, width, bottom=Neg_T, yerr=PosStd_T)
axarr[1, 0].legend((p1[0], p2[0]), ('Negative', 'Positive'))
axarr[1, 0].set_title('Tetris')		## Bottom Left


axarr[1, 1].bar(ind, Neg_TV, width, yerr=NegStd_TV)
axarr[1, 1].bar(ind, Pos_TV, width, bottom=Neg_TV, yerr=PosStd_TV)
axarr[1, 1].legend((p1[0], p2[0]), ('Negative', 'Positive'))
axarr[1, 1].set_title('Vanilla Tetris')		## Bottom right

#f.set_xlabel('Time Steps')
#f.set_ylabel('Number of Feedback Signals')

plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)

plt.tight_layout()

plt.show()




