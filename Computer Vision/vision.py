import cv2 as cv
import ultralytics
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import numpy as np
import pyrealsense2 as rs

class ArmVision:
    global model; model = YOLO('yolov8l.pt')
    global target_class
    global target_list
    
    def __init__(self) : # -> None:
        pass

    def find_center_point(width, height):
        return (width/2, height/2)

    def discover_cams():
        """Returns a list of the ids of all cameras connected via USB."""
        ctx = rs.context()
        ctx_devs = list(ctx.query_devices())
        cam_ids = []
        for i in range(ctx.devices.size()):
            cam_ids.append(ctx_devs[i].get_info(rs.camera_info.serial_number))
        return cam_ids

    def select_cam(cam_list):
        if len(cam_list) == 0:
            cam = cv.VideoCapture(0)
        else:
            pipe = rs.pipeline()
            profile = pipe.start()
            try:
                for i in range(0,100):
                    frames = pipe.wait_for_frames()
                    for f in frames:
                        print(f.profile)
            finally:
                pipe.stop()

    def draw_boxes(result,img):
        names = model.names
        annotator = Annotator(img)
        boxes = result.boxes
        for box in boxes:
            # Getting the xy coordinates of the top left and bottom right bounds of the box
            b = box.xyxy[0]
            c = box.cls
            # Prints all of the names of the classes that were detected
            print(names[int(c)])
            # feeds in the class and the box coordinate tuple
            # if int(c) == 0 or int(c) == 7:
            annotator.box_label(b, names[int(c)])
        frame = annotator.result()
        return frame

    def print_instructions():
        global target_class
        print("This is a YOLOv8 test algorithm. It allows the user to target a COCO class (custom classes to come)!!\n")
        print("To target a specific class please enter a valid class name, or index\n")
        print("Classes to choose from for now (these are not in numerical order, instead they show index of relevant test classes):\n")
        print("0 : person \n41: cup \n42: fork \n43: knife \n44: spoon \n62: tv \n63: laptop \n64: mouse  \n65: remote \n66: keyboard \n67: cell phone \n")
        class_index = input("Enter a Class index to target for tracking: ")
        # self.target_class(class_index)
    
    # def target_class(class_index):
        # class_index = int(class_index)
        # match class_index:
        #     case '0':
        #         # Need to set up logic as selecting the target class
        #         target_class = 0
        #         print("Selected: person")
        #     case "41":
        #         target_class = 41
        #         print("Selected: cup")
        #     case '42':
        #         target_class = 42
        #         print("Selected: fork")
        #     case '43':
        #         target_class = 43
        #         print("Selected: knife")
        #     case '44':
        #         target_class = 44
        #         print("Selected: spoon")
        #     case '62':
        #         target_class = 62
        #         print("Selected: tv")
        #     case '63':
        #         target_class = 63
        #         print("Selected: laptop")
        #     case '64':
        #         target_class = 64
        #         print("Selected: mouse")
        #     case '65':
        #         target_class = 65
        #         print("Selected: remote")
        #     case '66':
        #         target_class = 66
        #         print("Selected: keyboard")
        #     case '67':
        #         target_class = 67
        #         print("Selected: cell phone")

    
    def offset_from_target(class_index):
        bruh = 0

    def find_boxes_of_target(result):
        global model
        global target_class
        global target_list
        names = model.names
        boxes = result.boxes
        for box in boxes:
            c = box.cls
            b = box.xyxy[0]
            if int(c) == target_class:
                target_list.append(box)
    
    def select_target_object():
        """This will select a single object to target out of the targeted class of objects. 
        It will then store the last coordinates 87 """
        global model
        global target_list
        for box in target_list:
            bruh = 0

    def test_prediction():
        test_img = cv.imread('./protesters-rallying-against-racism-and-hate-make-their-way-up-14th-street-in-washington-dc-on-their-way-to-lafayette-park-to-protest-the-alt-right-PK5AK9.jpg')
        test_img2 = cv.imread('./dog.jpg')
        results2 = model.predict(test_img2, show=True)
        results = model.predict(test_img, show=True)
        print("Length of results",len(results))
        result = results[0]

    ultralytics.checks()
    test_prediction()
    print_instructions()
    cam = cv.VideoCapture(0)
    _, reference_frame = cam.read()
    height, width, channels = reference_frame.shape
    print("Width:", width, "Height:", height)
    cv.namedWindow('Prediction Output')
    cv.imshow('Prediction Output', reference_frame)
    while True:
        ret, frame = cam.read()
        results = model(frame, conf=.5, verbose=False, show=True)
        result = results[0]
        # prediction_frame = draw_boxes(result, frame)

        # cv.imshow('Prediction Output', prediction_frame)

        if cv.waitKey(10) == 27:
            cv.destroyAllWindows()
            break
