import os
import csv

dir = "/home/hanas879/Documents/Coding/Picture-Renamer/Bilder"
os.chdir(dir)


array = []

file = "/home/hanas879/Documents/Coding/Picture-Renamer/SATS.csv"


#Reading the CSV file
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array.append(row)



#Rename of the file


#os.chdir(dir)
#os.rename("1234","Tom")
#print(array[5][0])


#Testing the if/else

SATS = array[0][0]
picture = "1234"

if SATS == picture:
    os.rename(picture, "".join(array[0][1]))
else:
    print("Error!")
