from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__, static_url_path = '')

photos = UploadSet('photos', IMAGES)

txt = ""

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
configure_uploads(app, photos)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def upload():
    if 'photo' in request.files:
        print request.files['photo']
        photos.save(request.files['photo'], 'uploads', 'filename_test.png')
    return render_template('main.html')


@app.route('/upload2', methods=['POST'])        
def upload2():
    #print request.form['txt']
    txt = request.form['txt']
    
    print txt
    return render_template('main.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
