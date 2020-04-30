import numpy as np
class hsvHandler:
    def __init__(self):
        self.json = {
            "hmin":0,
            "hmax":180,
            "smin":0,
            "smax":255,
            "vmin":0,
            "vmax":255,
            "erode": False,
            "dilate": False,

        }
    
    def update(self,data):
        self.json = data
    
    def getlower(self):
        return np.array([self.json["hmin"],self.json["smin"],self.json["vmin"]])

    def getupper(self):
        return np.array([self.json["hmax"],self.json["smax"],self.json["vmax"]])

    def erode(self):
        return self.json["erode"]

    def dilate (self):
        return self.json["dilate"]