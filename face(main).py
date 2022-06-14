import time

import cv2
import cv2 as t
import sys
import keyboard
import os
import time as y1

print("To exit hold Q")

def v():
    c = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cascPath = "haarcascade_frontalface_default.xml"


    while (True):
        global a
        a = 's'
        if keyboard.is_pressed('q'):
            a = 'q'
            break
        ret, frame = c.read()
        # Create the haar cascade
        t.imwrite("me.png", frame)
        faceCascade = cv2.CascadeClassifier(cascPath)
        # Read the image
        image = cv2.imread('me.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # print(len(faces))
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            coords = [x, y, w, h]
        #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if len(coords)==4:
                image = image[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]

        # cv2.imshow("Faces found", image)
        # if len(coords)==4:
        #     roi_img = image[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]

        # print(type(faces))
        cv2.waitKey(1) & 0xFF
        if len(faces) != 0:
            cv2.imwrite('D:\FD\Suspect.png',image )
            # check()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cascPath = "mouth.xml"
            mouthCascade = cv2.CascadeClassifier(cascPath)
            mouth = mouthCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in mouth:
                 cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cascPath = "haarcascade_mcs_nose1.xml"
            noseCascade = cv2.CascadeClassifier(cascPath)
            nose = noseCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=15,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            s = y1.strftime("%H_%M_%S")
            for (x, y, w, h) in nose:
                 cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if len(mouth) == len(nose) | (len(nose)>len(mouth)):
                cv2.imwrite(f'D:\FD\confirmed\confirmed{s}.png', image)
            elif len(nose)!=0 and len(mouth)==0:
                cv2.imwrite(f'D:\FD\Improper\Improper{s}.png', image)
            break
        else:
            continue
        cv2.waitKey(1) & 0xFF
    c.release()
    t.destroyAllWindows()


os.system('mkdir D:\FD')
os.system("mkdir D:\FD\confirmed")
os.system('mkdir D:\FD\Improper')
time.sleep(5)
while True:
    v()

    if keyboard.is_pressed('q'):
        print("pressed")
        break
    if a == 'q':
        break
