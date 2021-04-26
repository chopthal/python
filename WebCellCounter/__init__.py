import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware


UPLOAD_FOLDER = './WebCellCounter/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def hello_flask():

    if request.method == 'POST':

        if 'file' not in request.files:

            # flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':

            # flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return f'''<img src = "{app.config['UPLOAD_FOLDER']}/{filename}"></img>
    '''

    # return f'''<h3>uploades_file</h3>
    # <div><img src="{app.config['UPLOAD_FOLDER']}/{filename}"></div>
    # '''

#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     print(app.config['UPLOAD_FOLDER'])
#     print(filename)
#     send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

if __name__ == '__main__':
    app.run()
