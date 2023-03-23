from flask import Flask, render_template, request, send_file
from PIL import Image
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test_upload.html') #แสดงผลหน้าหลัก

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    image = Image.open(file)
    # processed_image = image
    # processed_image.save('static/output1.png')
    return render_template('upload_completed.html') #ไปหน้า complete
    



if __name__ == '__main__':
    app.run(debug=True)