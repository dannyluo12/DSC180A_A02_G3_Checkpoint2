'''
We utilized this script as an alternative method to process our ".bag" files. This script converts the contents in
the ".bag" file into ".csv" format.

This script saves each topic in a bagfile as a csv.
Accepts a filename as an optional argument. Operates on all bagfiles in current directory if no argument provided
Usage1 (for one bag file):
	python bag2csv.py filename.bag
Usage 2 (for all bag files in current directory):
	python bag2csv.py

Credit:
Written by Nick Speal in May 2013 at McGill University's Aerospace Mechatronics Laboratory. Bugfixed by Marc Hanheide June 2016.
https://urldefense.com/v3/__http://www.speal.ca__;!!Mih3wA!SCgWuMoBCMEO0A1uIJDrHecSr0nkZNB-TT5AvXzA1bw92OmxgX6J2rjPDtLOG8A6$ 
Supervised by Professor Inna Sharf, Professor Meyer Nahon
'''

import rosbag, sys, csv
import time
import string
import os #for file management make directory
import shutil #for file management, copy file

#verify correct input arguments: 1 or 2
if (len(sys.argv) > 2):
	print("invalid number of arguments:   " + str(len(sys.argv)))
	print("should be 2: 'bag2csv.py' and 'bagName'")
	print("or just 1  : 'bag2csv.py'")
	sys.exit(1)
elif (len(sys.argv) == 2):
	listOfBagFiles = [sys.argv[1]]
	numberOfFiles = 1
	print ("reading only 1 bagfile: " + str(listOfBagFiles[0]))
elif (len(sys.argv) == 1):
	listOfBagFiles = [f for f in os.listdir(".") if f[-4:] == ".bag"]	#get list of only bag files in current dir.
	numberOfFiles = str(len(listOfBagFiles))
	print ("reading all " + numberOfFiles + " bagfiles in current directory: \n")
	for f in listOfBagFiles:
		print (f)
	print ("\n press ctrl+c in the next 10 seconds to cancel \n")
	time.sleep(10)
else:
	print ("bad argument(s): " + str(sys.argv))	#shouldnt really come up
	sys.exit(1)

count = 0
for bagFile in listOfBagFiles:
	count += 1
	print ("reading file " + str(count) + " of  " + str(numberOfFiles) + ": " + bagFile)
	#access bag
	bag = rosbag.Bag(bagFile)
	bagContents = bag.read_messages()
	bagName = bag.filename


	#create a new directory
	folder = string.rstrip(bagName, ".bag")
	try:	#else already exists
		os.makedirs(folder)
	except:
		pass
	shutil.copyfile(bagName, folder + '/' + bagName)


	#get list of topics from the bag
	listOfTopics = []
	for topic, msg, t in bagContents:
		if topic not in listOfTopics:
			listOfTopics.append(topic)


	for topicName in listOfTopics:
		#Create a new CSV file for each topic
		filename = folder + '/' + string.replace(topicName, '/', '_slash_') + '.csv'
		with open(filename, 'w+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter = ',')
			firstIteration = True	#allows header row
			for subtopic, msg, t in bag.read_messages(topicName):	# for each instant in time that has data for topicName
				#parse data from this instant, which is of the form of multiple lines of "Name: value\n"
				#	- put it in the form of a list of 2-element lists
				msgString = str(msg)
				msgList = string.split(msgString, '\n')
				instantaneousListOfData = []
				for nameValuePair in msgList:
					splitPair = string.split(nameValuePair, ':')
					for i in range(len(splitPair)):	#should be 0 to 1
						splitPair[i] = string.strip(splitPair[i])
					instantaneousListOfData.append(splitPair)
				#write the first row from the first element of each pair
				if firstIteration:	# header
					headers = ["rosbagTimestamp"]	#first column header
					for pair in instantaneousListOfData:
						headers.append(pair[0])
					filewriter.writerow(headers)
					firstIteration = False
				# write the value from each pair to the file
				values = [str(t)]	#first column will have rosbag timestamp
				for pair in instantaneousListOfData:
					if len(pair)>1:
						values.append(pair[1])
				filewriter.writerow(values)
	bag.close()
print ("Done reading all " + str(numberOfFiles) + " bag files.")
