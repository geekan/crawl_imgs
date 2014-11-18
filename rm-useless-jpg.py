import os
import cv2
import numpy as np

def parse(filename):
    img = cv2.imread(filename)
    if img is None:
        os.remove(filename)
        print filename, 'is none'
        return

    return
    lower_color = np.array([250, 250, 250])
    upper_color = np.array([255, 255, 255])

    print filename
    print img.size
    dst = cv2.inRange(img, lower_color, upper_color)

    #cv2.imshow('img', img)
    #cv2.imshow('dst', dst)

    print cv2.countNonZero(dst)

    #cv2.waitKey(0)

files = os.listdir('./imgs')
def main():
    for f in files:
        parse('imgs/' + f)
    return

if __name__ == '__main__':
    main()
