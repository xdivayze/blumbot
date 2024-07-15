import cv2 as cv
import math
from numpy import copy
import androidoperations as andp
SCOUNT = 6
DIFF= 3

def splitImages(img, scount):
    h, _ , _ = img.shape
    h /= scount
    selections = []

    for i in range(0,scount):
        selections.append(img[int(h*i):int(h*(i+1)), : , :])

    return selections

def showImages(selections):
    for i in range(0, len(selections) ):
        cv.imshow(str(i), selections[i])
    while 1==1:
            if cv.waitKey(0) == ord('q'):
                break
    cv.destroyAllWindows()

def loopThroughImage(img, r,g,b, bw,ogimsize, bh,show=False, save=False, dir=""):
    rows, cols,_ = img.shape
    detectedPxs = []
    row = 0
    while row < rows:
        col = 0
        while  col < cols:
            try:
                pr = img[row,col,2]
                pg = img[row,col,1]
                pb = img[row,col, 0]
                if pr == r and pb == b and pg == g:
                    detectedPxs.append([row,col])
                    andp.sendAndroidTap(col + 15, row + DIFF*int(ogimsize/SCOUNT))
                    ajout = int(bw/2) if col+int(bw/2)<cols else 1
                    col+=ajout
                    col+=1
                else:
                    col+=1

            except :
                print( "exception occured", row,col)
                raise(NameError)
        ajoutl=int(bh/2) if row+int(bh/2)<rows else 0
        if ajoutl == 0:
            break
        row += ajoutl

    if show or save:
        newImg = copy(img)
        for _, px in enumerate(detectedPxs):
            newImg[px[0], px[1]] = [0,0,255]
        if show:
            showImages([img, newImg]) 
        if save:
            cv.imwrite(dir, newImg)

    return detectedPxs


