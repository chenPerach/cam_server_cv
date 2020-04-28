from threading import Thread
import cv2
import os

class stream:
    """
    an object responsible for streaming the
    on a seperate thread
    """
    def __init__(self,src = 0,name = "webcamStream"):
        self.stream = camera(src)
        self.name = name
        self.stopped = False
        self.frame = None
        self.grabbedFrame = None
        self.grabbedFrame,self.frame = self.stream.read()


    def update(self):
        """
        runs preiodicly and updates the frame
        """
        while True:
            if self.stopped:
                return
            if not stream.isOpened():
                self.frame = cv2.imread(os.getcwd() +  "/static/resources/camnt.png")
            else:
                _,self.frame = self.stream.read()
    def start(self):
        """
        starts a simple thread for the camera that updates the current frame
        """
        t = Thread(target=self.update,name=self.name,args=())
        t.daemon = True
        t.start()
        return self
    
    def read(self):
        """ 
        returns the current frame of the camera
        """
        return self.frame
    def is_open(self):
        """
        true if the camera is open and false else
        """
        return self.stream.isOpened()
    def stop(self):
        """ 
        stops the stream 
        """
        self.stopped = True

class camera(cv2.VideoCapture):
    """
    this object wraps the opencv VideoCapture class
    and allows easy  settings controles
    """

    def __init__(self,src = 0):
        super().__init__(src)

    def loadSetting():
        """
         this function automatically loads the settings for the camera from a json file 
        """
        pass

class setting:
    """
    a simple json hendler for the camera settings
    """
    
            