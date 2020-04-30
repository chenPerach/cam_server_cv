from threading import Thread
import cv2
import os
import numpy as np
from camera.reader import hsvHandler


class stream:
    """
    an object responsible for streaming the
    on a seperate thread
    """
    def __init__(self,src = 0,name = "webcamStream"):
        self.stream = cv2.VideoCapture(src)
        self.name = name
        self.stopped  = False

        self.dilate = False
        self.erode = False

        self.frame = None
        self.masked = None

        _,self.frame = self.stream.read()
        self.json = hsvHandler()

    def update_json(self,data):
        self.json.update(data)
    def update(self):
        """
        runs preiodicly and updates the frame
        """
        while True:
            if self.stopped:
                return
            
            # if the camera is not open
            if not self.is_open():
                self.frame = cv2.imread(os.getcwd() + "/static/resources/camnt.png",cv2.IMREAD_COLOR)
                self.masked = self.frame
            
            #if the camera is not open
            else:
                _,self.frame = self.stream.read()
                self.pipeline(self.frame)

    def start(self):
        """ starts a simple thread for the camera that updates the current frame """
        t = Thread(target=self.update,name=self.name,args=()) 
        t.daemon = True 
        t.start() 
        return self 
    def read(self): 
        """ returns the current frame of the camera """ 
        return self.frame 
    def is_open(self): 
        """ true if the camera is open and false else """ 
        return self.stream.isOpened() 
    def stop(self): 
        """ stops the stream """ 
        self.stopped = True

    def pipeline(self,frame):
        """ a simple pip line """
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img,self.json.getlower(),self.json.getupper())

        self.erode = self.json.erode()
        self.dilate = self.json.dilate()
        kernal = np.ones((5,5),np.uint8)
        if self.dilate:
            mask = cv2.dilate(mask,kernal)
        if self.erode:
            mask = cv2.erode(mask,kernal)

        self.masked = mask


