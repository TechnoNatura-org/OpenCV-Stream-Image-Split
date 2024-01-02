import cv2
import argparse
from PIL import Image
from glob import glob as g
import os

def main():
    parser = argparse.ArgumentParser(description="OpenCV Stream Image Split")

    # Add arguments to the parser
    parser.add_argument('-f', '--frame', type=int, help="Capture every specified frame", required=True)
    parser.add_argument('-v', '--videoformat', type=str, help="Video format (mp4, mov).", required=True)
    parser.add_argument("--xoff", type=int, default=250, help="offset left")
    parser.add_argument("--yoff", type=int, default=0, help="offset right")

    args = parser.parse_args()

    x = args.xoff
    y = args.yoff

    left = x
    top = y
    right = left + 640
    bottom = top + 640

    # Parse the command-line arguments

    # Access the values of the parsed arguments
    frameArg = args.frame
    videoFormatArg = args.videoformat


    frameNum = 0
    # i = 0
    j = 0

    videoFormatPath = "*" + "." + videoFormatArg

    print(videoFormatPath)
    for gile in g(videoFormatPath):
        gfile = gile
        # print(gile)
        cam = cv2.VideoCapture(gfile)
        n_path = str(gfile)[0:][:-4]
        path = n_path + "/"

        # print(isCapture)
        os.makedirs(path, exist_ok=True)
        frameNum = 0
        # i = 0
        j = 0
        
        while True:
            isCapture, frame = cam.read()

            # print(isCapture)
            if not isCapture:
                # no more frame, exit loop
                break

            if frameNum == frameArg: 
                j = j+1

                generatedImageName = "image"

                fileName = f"{generatedImageName}"

                fileName = path+n_path + '-{:d}.jpg'.format(j)
                # print(fileName)
                cv2.imwrite(filename=fileName,img=frame)
                frameNum = 0

            frameNum = frameNum + 1

        im_count = 0
        # print(n_path)
        for file in g(path + "*.jpg"):
            # print(file)
            nfile = str(file)
            # print(nfile)
            #imposter.open(nfile).resize([4320, 2880], 1)
            Image.open(nfile).crop((left, top, right, bottom)).save(nfile) #left, top, right, bottom
            if im_count < 12:
                im_count+=1
            else:
                print("seventh done")
                im_count = 0

        
        # fileName = 'img{:d}.jpg'.format(frameNum)
        # cv2.imwrite(filename=fileName,img=frame)
if __name__== '__main__':
    main()
