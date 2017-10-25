from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__, static_url_path = '')

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)


@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        print request.files['photo']
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('main.html')




if __name__ == "__main__":

    app.debug = True
    app.run()


