#Written in Python 3.7

import os
import csv


#Path to the CSV file
bilder = os.getcwd() + "/SATS.csv"
#Path to the image directory
mappe = os.getcwd() + "/Bilder"
#Specify the fileformat to use
fileformat = ".docx"



result = []

#Reading and storing CSV to array
with open(bilder) as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        result.append(row)


print(result)
print(bilder)
print(mappe)

#Renames the files
#i = 0
#os.chdir(mappe)
#while i < len(result):
#    os.rename(result[i][0]+fileformat,"".join(result[i][1])+fileformat)
#    i += 1
