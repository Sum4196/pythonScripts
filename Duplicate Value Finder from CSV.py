from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv
import collections

filenameList = []

######
#Ask User what CSV file to open using File Dialog box.
######
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
filename = filename.replace("/","\\")
filename = filename.replace(".csv","")

######
#User selects what row the filename data is in. Also gives a message.
######
print("******\nPlease note that you must remove file name extensions from the file name column in your CSV file.\nIt is recommended to use a text editor for replacing filenames and viewing results.\nExcel formats data to its liking and results may be invalid as such.\n******\n")
column = 0
column = input("Please enter what column contains your filenames: ")
print("\n")

######
#Open the CSV file containing data to extract duplicates from.
#Appends filename data to a list and closes the file.
######
open_filename = str(filename + ".csv")
with open(open_filename, 'rb') as list_file:
    lyst = csv.reader(list_file, dialect='excel', delimiter=',')
    for row in lyst:
        filenameList.append(row[column-1])
list_file.close()

######
#Sorts the list.
######

new_filenameList = sorted(filenameList, key=len)

######
#If a value in the given dataset appears more than once, it is flagged and added to the duplicate file list.
######

y = collections.Counter(new_filenameList)
w = [i for i in y if y[i]>1]
print(str(len(w))+" duplicate files were found.\n")

######
#Formats the data for better viewing as a CSV and creates the output CSV file containing duplicates.
######

rows = zip(w)
out_filename = str(filename+"_output"+".csv")
out_filename = out_filename.replace("\\","\\\\")
with open(out_filename, 'wb') as resultFile:
    writer = csv.writer(resultFile)
    for row in rows:
        writer.writerow(row)
resultFile.close()
print_out_filename = out_filename.replace("\\\\","\\")
print("Your new CSV with duplicate files listed within is located here: \n" + print_out_filename)
print("\n")
raw_input("Press any key to close this window.")
