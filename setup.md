This is the instruction document for getting data from a TensorBoard file

**This is assuming you have already gotten the data and it is visible on TensorBoard**

1. The first thing you will want to do is obtain a CSV file for the data
	- This can be done by enabling downloadable links on the TensorBoard folder and clicking the CSV option under the graph you want
	- The data we will be looking at is the graph of positive and negative feedback signals given by the human trainer

2. When you have downloaded the file, there are 2 things you must be sure to do.
	a) First you must make sure you're in the right folder. Depending on the data you are analyzing, make sure you are in the correct atari game folder. There are four possible options (Bowling [B], MsPacMan [MPM], Tetris [T] and Tetris_Vanilla[TV]). 
	b) Once you are in the correct folder for the data you are collecting, it is important to keep the same naming nomenclature. The names of the files should be as follows: 
			run_.-tag-Human_feedback-sub##<game abb>.csv
		ex. run_.-tag-Human_feedback-sub13B.csv    *for subject #13, Game: Bowling

3. Once you have saved the file, then you must go into the data script for the game you added the file to and add the subject number so the script can analyze that data as well. 
	- The subject numbers are located in the 3rd line of the code in the subs vector.
	- The names of the data scripts are as follows:
		- B_Data.py for Bowling
		- MPM_Data.py for MsPacMan
		- T_Data.py for Tetris
		- TV_Data.py for Tetris_Vanilla
		
4. You should also add the subject numbers to the episode_analysis files. There is a separate file for each game, and when you go to add the subject names, be sure to add the correct number to the right file. You should also follow the correct naming structure for these files as well since the code depends on those names to pull the correct file. The naming system for them is as follows:
	run_.-tag-Per_Episode_episode_reward-##<game abb>.csv
		ex. run_.-tag-Per_Episode_episode_reward-28T.csv	*for subject #28, Game: Tetris
		* The game abbreviations are the same for these episode reward files as were used for the human feedback files
	

The output of these files differ in the type of information it is giving. Some of the files, Data_(B/MPM/T/TV), do not output anything. They are just there to collect and reorganize the data into something that the main algorithms can use. The feedback_analysis.py file outputs the average of the positive to negative feedback for each game individually and then all four games averaged together. It then gives different graphs about the current known relationships of the data. The first couple focus on positive and negative feedback and how they correlate. The next graphs show the relationship of all the feedback given together (without separating positive and negative feedback)

