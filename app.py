from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
import organize_files

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        flash('File uploaded successfully')
        return redirect(url_for('index'))


@app.route('/organize', methods=['POST'])
def organize():
    organize_files.organize_files(UPLOAD_FOLDER)
    flash('Files organized successfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
