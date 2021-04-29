FishFry v1.44 Readme!



By Michael Evans

contact: evans2md@gmail.com

FishFry is a light-weight python program designed to read electrodermal activity recordings (EDA/SCR/GSR) recorded by Biopac acqKnowledge and output a .csv file. Currently the desktop app is designed only for Mac Os, however the script can be executed on Linux machines via terminal.

FishFry is intended to be used in research studies that measure EDA responses. The expected input is a 2-channel AcqKnowledge file, with one channel containing the SCR raw data, and a second channel denoting trial periods. FishFry outputs a .csv with square root transformed trough-to-peak amplitudes for each trial, for each file (e.g run), for each folder (e.g. subject) within a specified directory.

To run:

- Launch the application

- Select the directory containing the data you wish to analyze

- Set user parameters (can use default values, create a new profile to save preferred parameters, or manually enter at the start of each session)

- Specify name for output file (default will be a timestamp)

- Select where to save output file
- Done! .csv file is saved to the specified directory.



Once excecuted, FishFry goes through the specified directory and collects all subdirectories. It then goes through each of these and computes trough-to-peak analysis of any detected acqknowledge files.

Output is organized by folders (columns), with contained files' output below (rows), with the files name written above each file's data. Multiple files in a folder are all stored in the same column, and can be differentiated by a blank space followed by the new file's name.

Fish fry currently only offers trough-to-peak analysis, meaning it outputs the largest line segment with continuous positive slope within a trial, if any such slope is detected. The output is the square root transformed value of the raw value.



User defined parameters (see accompanying image file):

FishFry allows the user to define parameters regarding the response window as well as criteria for qualifying an SCR.

These are:
  
- Strict Onset: If true, FishFry will ignore any positive slopes whose onset occured prior to the response window.
In most cases it is recommended that this be left as true.
  
- Response Window Start: At what point in  the trial, in seconds, should the response window start.

- Response Window End: At what point in the trial, in seconds, should the response window end.

- Duration: The minimum duration of a slope to qualify as an SCR, in seconds.
  
- Miminum Amplitude: The minimum amplitude of a slope to qualify as an SCR, in microsiemens.


See accompanying image file, FishFry Parameters Figure for reference.

Some things to keep in mind when using Fish Fry:

- FishFry has been designed to be resilient to any file types it may encounter while crawling the specified data directory. Meaning it will ignore nearly all files except those that it can read as  acqKnowledge files. That being said, it is still recommended that directories be prepared for analysis, with unnecessary files removed. 

- FishFry will ignore any folders with "excl" in them - this is intentional, as it  allows the user to create a folder "excl" and place any files they do not wish FishFry to analyze within.

- Several modules are required for the program to run:    	
	+ os
	+ scipy
	+ numpy
	+ csv
	+ datetime
	+ Tkinter
 

- When first instructed to conduct analysis, if there are many files (100+), or many files with errors, there will be a pause before progress is reflected on the GUI ("0/x files analyzed"). 
- If you wish to inspect the source code, it is located under Fishfry.app/Contents/Resources/script
  
	* DO NOT MAKE CHANGES UNLESS YOU ARE AWARE OF WHAT YOU ARE DOING *







-----

FishFry is built using bioread, a python module that reads raw acqKnowledge files

bioread by Nate Vack, https://github.com/njvack/bioread
App 

App compiled using Platypus

Platypus by Sveinbjorn Thordarson, https://sveinbjorn.org/platypus
