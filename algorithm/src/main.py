from os import path
import os
import cv2 as cv
from imageops import *
import time
from pathlib import Path
import androidoperations as andr
import numpy as np
start = time.time()
import atexit

#CREATE SETUP SHELL I NEED TO FIND A WAY TO MAKE IT ACTUALLY TAP BEFORE PASSING 

def exithandler():
    end= time.time()
    print(f"time elapsed:\n\t{end-start}")
    showImages([testerimg])

atexit.register(exithandler)
R,G,B = 53,152,219

BLOCK_WIDTH, BLOCK_HEIGHT=35, 35

SCOUNT = 6
DIFF= 4

testerimg = np.zeros((2340,1080,3), np.uint8)
while 1==1:
    ptempdir = path.join( Path(os.getcwd()).parent, 'temporary/')
    trimemdtime = str(time.time()).split('.')[0]
    dir = andr.getScreenshotAndSave(ptempdir, trimemdtime)
    #dir = '/home/cavej/repositories/blumbot/algorithm/temporary/1721064732.png'
    img = cv.imread(dir)
    row, col, _ = img.shape
    selections = splitImages(img, SCOUNT)
    savedir = path.join(ptempdir, "pixeldetections/"+trimemdtime+".png")
    detectedPxs = loopThroughImage(selections[DIFF], R, G, B, ogimsize=row,show=False, save=True, dir=savedir, bw=BLOCK_WIDTH, bh=BLOCK_HEIGHT)
    for _, pxc in enumerate(detectedPxs):
        #andr.sendAndroidTap(pxc[1], (pxc[0]+DIFF * int(row/SCOUNT)) + 40)
        testerimg[pxc[0]+DIFF*int(row/SCOUNT), pxc[1]+15] = [0,0,255]






cv.destroyAllWindows()
