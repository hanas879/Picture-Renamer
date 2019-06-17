#Written in Python 3.7

import os
import csv

#IMPORTANT!!!! Specify the fileformat to use, and don't delete the "."
fileformat = ".jpg"



#Gets the current working directory and points to the .csv file
bilder = os.getcwd() + "/SATS.csv"
#Gets the current working directory and points to the image directory
mappe = os.getcwd() + "/Bilder"



result = []

#Reading and storing CSV to array
with open(bilder) as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        result.append(row)



#Renames the files
i = 0
os.chdir(mappe)
while i < len(result):
    os.rename(result[i][0]+fileformat,"".join(result[i][1])+fileformat)
    i += 1
