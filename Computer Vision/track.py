import cv2 as cv
import ultralytics
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import numpy as np
import pyrealsense2 as rs


#pyrealsense2 is for a intel realsense camera. Unneeded if using any other camera
target_location = ()

def set_object():
    bruh = 0



def main():
    while True:
        
        if cv.waitKey(10) == 27:
            cv.destroyAllWindows()
            break