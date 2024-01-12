import cv2 as cv
import ultralytics
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import numpy as np
import pyrealsense2 as rs



model = YOLO('best.pt')
names = model.names
# annotator = Annotator(img)
# boxes = result.boxes
# for box in boxes:
#     # Getting the xy coordinates of the top left and bottom right bounds of the box
#     b = box.xyxy[0]
#     c = box.cls
#     # Prints all of the names of the classes that were detected
#     print(names[int(c)])
#     # feeds in the class and the box coordinate tuple
#     # if int(c) == 0 or int(c) == 7:
#     annotator.box_label(b, names[int(c)])

# frame = annotator.result()

video = "2023-12-05 17-38-44.mp4"

results = model(video, conf=.5, verbose=False, show=True)


vid = cv.VideoCapture(video)