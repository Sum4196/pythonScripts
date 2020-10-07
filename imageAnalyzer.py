import sys
from PIL import Image

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

try:
    image = Image.open(str(sys.argv[1]))
    px = image.load()
    width, height = image.size
    imagenew = Image.new("RGB", (width, height))
    newpx = imagenew.load()
    for x in range(image.width):
        progress(x, int(len(range(image.width))), status='Working...')
        for y in range(image.height):
            #curPixel = image.getpixel((x,y))
            #curValue = curPixel[0] + curPixel[1] + curPixel[2]
            #if(curValue < 200):
            #    imagenew.putpixel((x,y), (210,210,210))
            curValue = px[x,y][0] + px[x,y][1] + px[x,y][2]
            if(curValue < 200):
                newpx[x,y] = (210, 210, 210)
    imagenew.save("C:\\Users\\mmendenh\\Desktop\\test.jpg")
except ValueError:
    print("Please provide a file to work on.")
