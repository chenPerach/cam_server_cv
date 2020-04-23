from flask import Flask, render_template,url_for,Response
from camera.camera import stream
frame = None

app = Flask(__name__)
vc = stream(0).start()

def gen():
    while True: 
        #the frame is an opencv mat object
        frame = vc.read()
        # cv2.imshow(vc.name,frame)
        if frame is None:
            continue
        
        flag,encodedImage = cv2.imencode(".jpg",frame)
        if not flag:
            continue
        # k = cv2.waitKey(1)
        # if k == 27:
            # break
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug = True,threaded = True,use_reloader=False)