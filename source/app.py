import os
import uuid
from flask import Flask, flash, request, redirect

# UPLOAD_FOLDER = '/c/Users/Anjali/Documents/interactionLab/web-speech-recorder/source/files'
# UPLOAD_FOLDER = 'c\Users\Anjali\Documents\interactionLab\web-speech-recorder\source\files'
UPLOAD_FOLDER = 'files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.chmod(UPLOAD_FOLDER, 0o444) 


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    # file.save(f"{UPLOAD_FOLDER}/{file_name}")
    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run()
