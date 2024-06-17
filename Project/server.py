from flask import Flask
import os
from flask import Flask, render_template, request, Response
import cv2

from FRvideo import video_stream

#from camera import VideoCamera

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route('/home', methods =['GET'])
def home_page():
    return render_template('home.html', background_image = 'static/images/menu.jpg')

@app.route('/project_details', methods =['GET', 'POST'])
def project_info_page():
    return render_template('project_details.html')
    
@app.route('/project', methods =['GET', 'POST'])
def project_page():
    return render_template('project.html', background_image = 'static/images/proimg.jpeg')

@app.route('/train', methods =['GET', 'POST'])
def train_page():
    return render_template('train.html', background_image = 'static/images/face_recognition_background.jpg')

@app.route('/test', methods =['GET', 'POST'])
def test_page():
    return render_template('test.html')

@app.route('/about_us', methods =['GET', 'POST'])
def aboutus_page():
    return render_template('about_us.html', member1_image = 'static/images/Anand.jpeg', member2_image = 'static/images/Suvarnarao.jpeg')


@app.route('/show', methods =['GET', 'POST'])
def show():
    filename = ''
    for file in os.listdir("../"):
        if file.startswith("upload"):
            filename = file
    #image = cv2.imread(filename)
    file1 = open("../name.txt","r")
    print("Reading name from File")
    name = file1.readlines()[0]
    print("name",name)
    file1.close()
    #return Response(face_rec(filename, name), mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(video_stream(filename,name), mimetype='multipart/x-mixed-replace; boundary=frame')

    #return "hi you are in right path"  

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
