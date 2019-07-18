import cv2
import numpy as np


def main():
    # window_name="Cam feed"
    # cv2.namedWindow(window_name)
    cap = cv2.VideoCapture("Watch- CCTV footage of Orly airport attack.mp4")

    # filename = 'F:\sample.avi'
    # codec=cv2.VideoWriter_fourcc('X','V','I','D')
    # framerate=30
    # resolution = (500,500)

    #  VideoFileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)

    if cap.isOpened():

        ret, frame = cap.read()

    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while ret:
        ret, frame = cap.read()
        # VideoFileOutput.write(frame)

        d = cv2.absdiff(frame1, frame2)

        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=3)
        contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        font =cv2.FONT_HERSHEY_SIMPLEX


        cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        # cv2.imshow("win1",frame2)
        cv2.imshow("inter", frame1)

        if cv2.waitKey(40) == 27:
            break
        frame1 = frame2
        ret, frame2 = cap.read()
    cv2.destroyAllWindows()
    # VideoFileOutput.release()
    cap.release()


main()
