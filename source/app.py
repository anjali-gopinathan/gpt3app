import os
import uuid
import whisper

from flask import Flask, flash, request, redirect, render_template, url_for

UPLOAD_FOLDER = 'files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# mp3_file_name = ''
# success = False
model = whisper.load_model("base") # base or large
print("Loaded base whisper model")

@app.route('/', methods=['GET', 'POST'])
def index():
    maintext = 'hello world'
    # if request.method == 'POST':
    #     maintext = get_text()
    return render_template('index.html', maintext=maintext)


@app.route('/save-record', methods=['GET','POST'])
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
    mp3_file_name = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file_name)
    file.save(mp3_file_name)
    print(f"Successfully saved file {mp3_file_name}")
    # return '<h1>Success</h1>'
    # success = True
    # result = f"Successfully saved file {mp3_file_name}\n"
    userSpeech = get_text(mp3_file_name)
    result = "You:\t" + userSpeech
    return result

def get_text(mp3_file_name):
    result = model.transcribe(mp3_file_name)   
    # print(f"You said:\t{result['text']}")
    return result


if __name__ == '__main__':
    app.run(debug=True)
