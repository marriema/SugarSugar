from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__, static_url_path = '')

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
configure_uploads(app, photos)


@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        print request.files['photo']
        photos.save(request.files['photo'], 'subfolder_test', 'filename_test.png')

    return render_template('main.html')




if __name__ == "__main__":

    app.debug = True
    app.run()


