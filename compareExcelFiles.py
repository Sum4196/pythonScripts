import pandas as pd
import xlsxwriter
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--diff', help='Get differences instead of duplicates', action='store_true')
parser.add_argument('--dup', help='Get duplicates instead of differences', action='store_true')
parser.add_argument('--first', help='First file location')
parser.add_argument('--second', help='Second file location')
parser.add_argument('--removeFromFirst', help='Remove rows in first file compared to second file.  If neither -diff or -dup are given, all rows in first file matching rows in second file will be deleted.', action='store_true')
parser.add_argument('--removeFromSecond', help='Remove rows in second file compared to first file.  If neither -diff or -dup are given, all rows in second file matching rows in first file will be deleted.', action='store_true')
parser.add_argument('-o', help='Output file location')
parser.add_argument('-oExcel', help='Output file(Excel) location')
args = parser.parse_args()


df1 = pd.read_excel(args.first).sort_index()
npfirst = df1.values
first = npfirst.tolist()

df2 = pd.read_excel(args.second).sort_index()
npsecond = df2.values
second = npsecond.tolist()

# Gets list of just filenames from second array
temp = [x[0] for x in second]

matches = []
differences = []

# Get matches and differences lists
for i in range(len(first)):
    if(first[i][0] in temp):
        matches.append(first[i])
    else:
        differences.append(first[i])
		
# Gets list of just filenames from first array
tempSecond = [x[0] for x in first]

matchesSecond = []
differencesSecond = []

# Get matches and differences lists
for i in range(len(second)):
    if(second[i][0] in tempSecond):
        matchesSecond.append(second[i])
    else:
        differencesSecond.append(second[i])


def writeToExcel(pandas_dataframe, file, sheet_name="Sheet1", index=False, first_column='A:A', second_column='B:B', first_column_width=None, second_column_width=None):
    """Format Excel output data column to wrap text."""
    newdf = pandas_dataframe
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    newdf.to_excel(writer, sheet_name=sheet_name, index=index)
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    center_format = workbook.add_format()
    center_format.set_align('left')
    center_format.set_align('vcenter')
    worksheet.set_column(first_column, first_column_width, center_format)
    wrap_format = workbook.add_format({'text_wrap': True})
    worksheet.set_column(second_column, second_column_width, wrap_format)
    writer.save()

def removeFromFirst():
    """Remove lines from first file compared to second file."""
    if((args.removeFromFirst is True and args.diff is False and args.dup is False) or (args.removeFromFirst is True and args.diff is True and args.dup is False)):
        results = matches
        writeToExcel(pd.DataFrame(results, columns=["FileName", "FileLocation"]), args.first, first_column_width=60, second_column_width=200)
    elif(args.removeFromFirst is True and args.diff is False and args.dup is True):
        results = differences
        writeToExcel(pd.DataFrame(results, columns=["FileName", "FileLocation"]), args.first, first_column_width=60, second_column_width=200)
    else:
        print("Please select either diff or dup or neither(this will choose diff by default), Not both.")

def removeFromSecond():
    """Remove lines from second file compared to first file."""
    if((args.removeFromSecond is True and args.diff is False and args.dup is False) or (args.removeFromSecond is True and args.diff is True and args.dup is False)):
        results = matchesSecond
        writeToExcel(pd.DataFrame(results, columns=["FileName", "FileLocation"]), args.second, first_column_width=60, second_column_width=200)
    elif(args.removeFromSecond is True and args.diff is False and args.dup is True):
        results = differencesSecond
        writeToExcel(pd.DataFrame(results, columns=["FileName", "FileLocation"]), args.second, first_column_width=60, second_column_width=200)
    else:
        print("Please select either diff or dup or neither(this will choose diff by default), Not both.")

# Compares the two excel files for differencs
if(args.diff is True):
    results = differences
# Compares the two excel files for duplicates
if(args.dup is True):
    results = matches
# Compares the two excel files for difference and duplicates and removes the data in-place
if(args.removeFromFirst is True):
    removeFromFirst()
# Compares the two excel files for difference and duplicates and removes the data in-place
if(args.removeFromSecond is True):
    removeFromSecond()

# Creates output file of the list
if(args.oExcel):
	writeToExcel(pd.DataFrame(results, columns=["FileName", "FileLocation"]), args.oExcel, first_column_width=60, second_column_width=200)
else:
	if(args.o is None):
		print(results)
	else:
		path = os.path.dirname(args.o)
		if(os.path.isdir(path) is True):
			with open(args.o, 'w') as outFile:
				for result in results:
					outFile.write(str(result)+'\n')
		else:
			with open(os.path.join(os.getcwd() + "\\" + args.o), 'w') as outFile:
				for result in results:
					outFile.write(str(result)+'\n')