import pprint

file1 = 'C:\\Users\\mmendenh\\Documents\\CPLWVaultProjectFiles\\readyToDelete-temp.txt'
file2 = 'C:\\Users\\mmendenh\\Documents\\CPLWVaultProjectFiles\\filesToDelete-temp.txt'

with open(file1) as rdt:
    rdtFiles = [file.rstrip('\n') for file in open(file1)]

with open(file2) as tdc:
    tdcFiles = [file.rstrip('\n') for file in open(file2)]

duplicates = [x for x in rdtFiles if x not in tdcFiles]
pp = pprint.PrettyPrinter()
pp.pprint(duplicates)
