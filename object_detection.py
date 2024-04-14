import random
import cv2
import numpy as np
from ultralytics import YOLO
import serial
import time

bluetooth=serial.Serial("/dev/rfcomm4",38400)
a = "0"
string='X{0}'.format(a)
bluetooth.write(string.encode("utf-8"))

# Opening the file in read mode
my_file = open("utils/coco.txt", "r")
# Reading the file
data = my_file.read()
# Replacing and splitting the text when newline ('\n') is seen
class_list = data.split("\n")
my_file.close()

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# Load a pretrained YOLOv8n model
model = YOLO("weights/yolov8n.pt", "v8")

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480

# Open webcam
cap = cv2.VideoCapture(0)  # 0 for the default webcam, you can change it if needed

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # If frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Resize the frame | small frame optimizes the run
    frame = cv2.resize(frame, (frame_wid, frame_hyt))

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()

    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
            
            if class_list[int(clsID)] == 'stop sign':            #code for specifying the sign or object and transmit bluetooth signal upon detection
                a = "1"
                string='X{0}'.format(a)
                bluetooth.write(string.encode("utf-8"))
            

            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()