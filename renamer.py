#Written in Python 3.7

import os
import csv

bilder = r"C:\Users\henmil\Documents\GitHub\Picture-Renamer\SATS.csv"    #Path to the CSV file
mappe = r"C:\Users\henmil\Documents\GitHub\Picture-Renamer\Bilder"       #Path to the image directory


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
    os.rename(result[i][0],"".join(result[i][1]))
    i += 1
