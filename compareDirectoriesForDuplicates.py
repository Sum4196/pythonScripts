import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-diff', help='Get differences instead of duplicates', action='store_true')
parser.add_argument('-dup', help='Get duplicates instead of differences', action='store_true')
parser.add_argument('--first', help='First file/folder location')
parser.add_argument('--second', help='Second file/folder location')
parser.add_argument('-o', help='Output file location')
args = parser.parse_args()

first = []
second = []

for root, dirs, files in os.walk(args.first):
    for filename in files:
        first.append(filename.upper())

for root, dirs, files in os.walk(args.second):
    for filename in files:
        second.append(filename.upper())

if(args.diff is True):
    results = [file for file in first if file not in second]
elif(args.dup is True):
    results = [file for file in first if file in second]


if(args.o is None):
    print(results)
else:
    path = os.path.dirname(args.o)
    if(os.path.isdir(path) is True):
        with open(args.o, 'w') as outFile:
            for result in results:
                outFile.write(result+'\n')
    else:
        with open(os.path.join(os.getcwd() + "\\" + args.o), 'w') as outFile:
            for result in results:
                outFile.write(result+'\n')
