import requests
import cv2
import djitellopy
import time
from time import sleep
from threading import Thread



URL = "http://192.168.88.3:5000/stream/1"

hunters = [True]


'''def hunt():
    while hunters[0]:
       
        Hunter2.move_forward(300)
        Hunter2.rotate_counter_clockwise(90)
        sleep(1)
        Hunter2.move_forward(200)
        Hunter2.rotate_counter_clockwise(90)
        sleep(1)
        Hunter2.move_forward(300)
        Hunter2.rotate_counter_clockwise(90)
        sleep(1)
        Hunter2.move_forward(200)
        Hunter2.rotate_counter_clockwise(90)
        sleep(1)
        '''
        
        
def stream():
    while True:
        cap = Hunter2.get_frame_read().frame
        if cap is None:
            print("No image")
            continue
        
        cap = cv2.cvtColor(cap, cv2.COLOR_RGB2BGR)
        _, img_encoded = cv2.imencode('.jpg', cap)
        
        try:
            response = requests.post(URL, data=img_encoded.tobytes())
        
            res_data = response.json()
            if res_data["land"]:
                Hunter2.streamoff()
                Hunter2.land()
            elif res_data['action2']:
                Hunter2.move_up(100)
                Hunter2.flip_forward()
                Hunter2.land()
        except Exception:
            print("no server")

        time.sleep(0.1)

#t1 = Thread(target=hunt)
t2= Thread(target=stream)

Hunter2 = djitellopy.Tello()
Hunter2.connect()
Hunter2.streamon()
#Hunter2.takeoff()
#Hunter2.move_up(170)
#Hunter2.set_speed(50)
#t1.start()
t2.start()
#t1.join()
t2.join()
