import os
import argparse

'''
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True, help="Input file")
    parser.add_argument("-o", "--output", dest="output", required=True, help="Output file location")
    args = parser.parse_args()

    inputDirName = args.input

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(inputDirName)

    with open(args.output, 'w') as output_file:
        for elem in listOfFiles:
            output_file.write(elem + "\n")

if(__name__ == '__main__'):
    main()
