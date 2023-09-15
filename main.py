import cv2
import argparse

def main():
    parser = argparse.ArgumentParser(description="OpenCV Stream Image Split")

    # Add arguments to the parser
    parser.add_argument('-s', '--source', default=0, help="Your webcam input or video", required=True)
    parser.add_argument('-f', '--frame', help="Capture every specified frame", type=int, required=True)
    parser.add_argument('-n', '--name', help="Generated image name", type=str, required=False)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the parsed arguments
    sourceArg = args.source
    frameArg = args.frame
    nameArg = args.name


    cam = cv2.VideoCapture(sourceArg)
    frameNum = 0
    # i = 0
    j = 0
    isCaptured = True
    while True:
        isCapture, frame = cam.read()

        # print(isCapture)

        print(frameNum)
        if not isCapture:
            # no more frame, exit loop
            break

        if frameNum == frameArg: 
            j = j+1

            generatedImageName = "image"
            if nameArg is not None:
                generatedImageName = nameArg
            fileName = f"{generatedImageName}"
            fileName = fileName + '-{:d}.jpg'.format(j)
            cv2.imwrite(filename=fileName,img=frame)
            frameNum = 0

        frameNum = frameNum + 1

        
        # fileName = 'img{:d}.jpg'.format(frameNum)
        # cv2.imwrite(filename=fileName,img=frame)
if __name__== '__main__':
    main()