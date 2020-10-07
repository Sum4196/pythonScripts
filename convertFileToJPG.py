from PIL import Image
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True, help="Input file")
    parser.add_argument("-o", "--output", dest="output", required=True, help="Output file location")
    args = parser.parse_args()
	
    Image.MAX_IMAGE_PIXELS = 10000000000
    inputImage = Image.open(args.input)
    newImage = inputImage.convert('RGB')
    newImage.save(args.output)

if(__name__ == '__main__'):
    main()
