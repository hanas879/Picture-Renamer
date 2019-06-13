#Written in Python 3.7

import os
import csv

SATS = "/home/hanas879/Documents/Coding/Picture-Renamer/SATS.csv"    #Path to the CSV file
dir = "/home/hanas879/Documents/Coding/Picture-Renamer/Bilder"       #Path to the image directory
os.chdir(dir)

result = []

#Reading and storing CSV to array
with open(SATS) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        result.append(row)


#Renames the files
i = 0

while i < len(result):
    os.rename(result[i][0],"".join(result[i][1]))
    i += 1
