from deepface import DeepFace
import cv2
import numpy as np
import os

path = os.getcwd() + str("\media\static\STUDENTS PAGE\images")
array = np.zeros((len(os.listdir(path)), len(os.listdir(path))))
i, j = 0, 0
for file in os.listdir(path):
    current_img = file
    for image in os.listdir(path):
        recognition = DeepFace.verify(img1_path=os.path.join(path, file), img2_path=os.path.join(path, image))
        distance = recognition['distance']
        array[i, j] = distance
        j += 1
    i += 1
print(array)
