import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
count = 0
timetemp = 0
upCount = 0
prevUpCount = 69
dict = {"1":"a",
        "2":"b",
        "3":"c",
        "4":"d",
        "5":"e",
        "6":"f",
        "7":"g",
        "8":"h",
        "9":"i",
        "10":"j",
        "11":"k",
        "12":"l",
        "13":"m",
        "14":"n",
        "15":"o",
        "16":"p",
        "17":"q",
        "18":"r",
        "19":"s",
        "20":"t",
        "21":"u",
        "22":"v",
        "23":"w",
        "24":"x",
        "25":"y",
        "26":"z",

        
        
        
        
        
        }

        
        
while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                upCount = 0
            if fingerup == [0, 1, 0, 0, 0]:
                upCount = 1
            if fingerup == [0, 1, 1, 0, 0]:
                upCount = 2
            if fingerup == [0, 1, 1, 1, 0]:
                upCount = 3
            if fingerup == [0, 1, 1, 1, 1]:
                upCount = 4
            if fingerup == [1, 1, 1, 1, 1]:
                upCount = 5
            if fingerup == [1, 0, 0, 0, 0]:
                upCount = 6
            if fingerup == [1, 1, 0, 0, 0]:
                upCount = 7
            if fingerup == [1, 1, 1, 0, 0]:
                upCount = 8
            if fingerup == [1, 1, 1, 1, 0]:
                upCount = 9
            cv2.putText(img, str(upCount), (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (0,255,0), 12)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.2)
    timetemp += 0.2
    
    if(upCount != 0 and prevUpCount!= upCount):
        count += upCount
        prevUpCount = upCount
        if(count>26):
            count-=26
        print(dict[str(count)])
    elif(upCount == 0):
        count = 0
        timetemp = 0
        

video.release()
cv2.destroyAllWindows()
