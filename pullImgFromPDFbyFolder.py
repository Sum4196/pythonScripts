import sys
import os
import argparse
# Maybe look into using ghostscript in this project in order to handle pdf files created in the postscript format.
# Currently, postscript formatted pdf files give the "No Stream Found" error since this program can't find the "stream".
# Ghostscript may or may not be able to handle all pdf files, will have to look into it and test different formats.

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Input file path')
parser.add_argument('-o', help='Output file path')
args = parser.parse_args()

errors = []

def pullImage(filepath):
    with open(filepath, "rb") as file:
        pdf = file.read()

    filepathname, filename = os.path.split(filepath)
    #remove the following line to use filepathname variable in pullImage function.
    del filepathname

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            errors.append("No Stream Found Error: " + filename)
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            errors.append("Stream Error: " + filename)
            #print("Didn't find end of stream! - " + filename)
            break
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            errors.append("JPG Error: " + filename)
            #print("Didn't find end of JPG! - " + filename)
            break

        istart += startfix
        iend += endfix
        print("JPG %d from %d to %d" % (njpg, istart, iend))
        jpg = pdf[istart:iend]

        if(args.o):
            with open(os.path.join(args.o, filename[:-4] + "-%d.jpg" % njpg), "wb") as jpgfile:
                jpgfile.write(jpg)
        elif(args.o is None):
            with open(os.path.join(args.i, filename[:-4] + "-%d.jpg" % njpg), "wb") as jpgfile:
                jpgfile.write(jpg)
        else:
            print("There was a problem with saving the file(s).")
            input("Press any key to close program.")
            sys.exit()

        njpg += 1
        i = iend


filepaths = []
pdfFileCount = 0

for file in os.listdir(args.i):
    if file.endswith(".pdf"):
        filepaths.append(os.path.join(args.i, file))
        pdfFileCount += 1

print("%d PDF files found." % pdfFileCount)

for filepath in filepaths:
    pullImage(filepath)

if( len(errors) > 0 ):
    print("\nErrors:\n")
    for i in range(len(errors)):
        print(errors[i])
else:
    print("No errors found!")