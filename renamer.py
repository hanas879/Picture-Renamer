#Written in Python 3.7

import os
import csv

#Path to the CSV file
bilder = r"C:\Users\henmil\Documents\GitHub\Picture-Renamer\SATS.csv"
#Path to the image directory
mappe = r"C:\Users\henmil\Documents\GitHub\Picture-Renamer\Bilder"
#Specify the fileformat to use
fileformat = ".jpg"



result = []

#Reading and storing CSV to array
with open(bilder) as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        result.append(row)



print(result)
#Renames the files
#i = 0
#os.chdir(mappe)
#while i < len(result):
#    os.rename(result[i][0]+fileformat,"".join(result[i][1])+fileformat)
#    i += 1
