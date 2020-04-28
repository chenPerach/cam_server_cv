from flask import Flask, render_template,url_for,Response,request
from camera.camera import stream
import cv2
frame = None

app = Flask(__name__)
vc = stream(0).start()


def gen():
    while True: 
        #the frame is an opencv mat object
        frame = vc.read()
        if frame is None:
            continue
        
        flag,encodedImage = cv2.imencode(".jpg",frame)
        if not flag:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route("/proccesHSV", methods = ["POST"])
def updateHSV():
    if request.method == 'POST':
        data = request.get_json() 
        return "json recived"
    else:
        return "error json not recived"

@app.route("/empty",methods = ['POST'])
def empty():
    if request.method == 'POST':
        return '''
        <script> console.Log("init completed") </script>
        '''
if __name__ == "__main__":
    app.run(debug = True,threaded = True,use_reloader=False)