# Picture-Renamer
A tool for changing name on files from a .cvc file
<br>
<br>
<b>NB!:</b>
<br>
 This has been made specificly for Storhamar VGS but feel free to tweak it for you'r needs.  
<br>
The concept of this script is that you have a folder with pictures, where you would like to rename all the files inside. In our case it's from school portraits from students that we take, but the file name is saved with a unique ID that connects to a database. We want to rename them to the name of the student. Soooo I made a script.

<b>This is still in a "Work in progress" so it's important to have all the pictures with the ID's in the .csv file. If the .csv file contains an ID that does not exist in the picture folder it will output an error</b>
<br>


# Python to .exe
<b>Install pyinstaller</b>
```
pip install pyinstaller
```
<br>

<b>Convert .py to .exe</b>
<br>
```
pyinstaller -w -F yourprogram.py
```
