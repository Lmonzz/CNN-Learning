from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'D:\\Python\\deep_learning\\FINAL_TF2_FILES\\TF_2_Notebooks_and_Data\\04-CNNs\ESP32CAM\\captured_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_img', methods=['POST'])
def upload_img():
    if 'imageFile' not in request.files:
        return 'No image file part', 400
    
    file = request.files['imageFile']
    if file.filename == '':
        return 'No selected file', 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return f'File uploaded successfully to {file_path}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)