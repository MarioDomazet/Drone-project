from threading import Thread
from time import sleep
from djitellopy import TelloSwarm
import cv2
import numpy as np
from ultralytics import Yolo

All=TelloSwarm.fromIps([

])


Hunter=TelloSwarm.fromIps([

])
Hunter1=TelloSwarm.fromIps([

])
Hunter2=TelloSwarm.fromIps([

])

Prey1=TelloSwarm.fromIps([

])

Prey2=TelloSwarm.fromIps([

])

Prey3=TelloSwarm.fromIps([

])

Prey4=TelloSwarm.fromIps([

])

Prey5=TelloSwarm.fromIps([

])

def get_detections_xyxy(detections):
    ret = []
    for det in detections:
        xyxy = det.boxes.xyxy.to("cpu")
        xyxy = xyxy.numpy()
        xyxy = xyxy.astype("int32").squeeze()
        
        ret.append(xyxy)

    return ret


def hunt():
    Hunter.move_forward(300)
    Hunter.rotate_counter_clockwise(90)
    sleep(1)
    Hunter.move_forward(200)
    Hunter.rotate_counter_clockwise(90)
    sleep(1)
    Hunter.move_forward(300)
    Hunter.rotate_counter_clockwise(90)
    sleep(1)
    Hunter.move_forward(200)
    Hunter.rotate_counter_clockwise(90)
    sleep(1)

def p1():
    Prey1.curve_xyz_speed(50,50,0,100,0,0,60)
    Prey1.curve_xyz_speed(-50,-50,0,-100,0,0,60)

def p2():
    Prey2.move_forward(50)
    Prey2.rotate_counter_clockwise(90)
    sleep(1)
    Prey2.move_forward(50)
    Prey2.rotate_counter_clockwise(90)
    sleep(1)
    Prey2.move_forward(50)
    Prey2.rotate_counter_clockwise(90)
    sleep(1)
    Prey2.move_forward(50)
    Prey2.rotate_counter_clockwise(90)

def p3():
    Prey3.move_up(100)
    sleep(1)
    Prey3.move_down(100)
    sleep(1)

def p4():
    Prey4.move_forward(100)
    Prey4.rotate_clockwise(120)
    sleep(1)
    Prey4.move_forward(100)
    Prey4.rotate_clockwise(120)
    sleep(1)
    Prey4.move_forward(100)
    Prey4.rotate_clockwise(120)
    sleep(1)

def p5():
    Prey5.curve_xyz_speed(0,50,50,0,0,100,60)
    Prey5.curve_xyz_speed(0,-50,-50,0,0,-100,60)

t1=Thread(target=hunt)
t2=Thread(target=p1)
t3=Thread(target=p2)
t4=Thread(target=p3)
t5=Thread(target=p4)
t6=Thread(target=p5)

All.connect()
All.takeoff()
Hunter.move_up(50)
Hunter1.streamon()
Hunter2.streamon()
h1=0
h2=0



while h1<3 and h2<3:
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

model=Yolo()

while True:
    frame1= Hunter1.get_frame_read().frame
    frame2= Hunter2.get_frame_read().frame
    frame3 = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
    frame4 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)

    detections1 = model.predict(frame3)
    detections2 = model.predict(frame4)
    coords1= get_detections_xyxy(detections1)
    coords2= get_detections_xyxy(detections2)

    for cord in coords1:
        cv2.rectangle(frame3, cord[:2], cord[2:], (255, 0, 0), 2)
       

    for cord in coords2:
        cv2.rectangle(frame4, cord[:2], cord[2:], (255, 0, 0), 2)
        

    cv2.imshow("Hunter1", frame3)
    cv2.imshow("Hunter2", frame4)
    cv2.waitKey(0)


