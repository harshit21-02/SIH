import cv2
import deepface
from deepface import DeepFace
import os
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'authenticate'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT image FROM student_studata')
myresult = mycursor.fetchall()
os.chdir('static/Test')
def video_reader():
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cam.read()
        cv2.imshow("img", img)
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code detected-->", data)
            break
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    print(os.getcwd())
    while True:
        _, img = cam.read()
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("s"):
            cv2.imwrite('image.png',img)
            for i in myresult:
                result = DeepFace.verify(img1_path=r"e:\SIH\SIH\SIH\webapp\betterbots\static\Test\image", img2_path=i)
                if result['verified']==True:
                    print('matched')
                    break
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()
    return data,i
video_reader()
