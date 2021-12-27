import os;
import sqlite3;
import json
from io import BytesIO

from flask import Flask, send_file, send_from_directory, safe_join, abort
from PIL import Image
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/images/<string:type>/<int:id>', methods=['GET'])
def add_activity(type, id):
    dir = 'images/'+type+'/'
    image_list = os.listdir(dir)

    im = Image.open(dir + image_list[id])
    new_image_size = (int(im.size[0] /(im.size[1] / 1080)), 1080)
    im = im.resize(new_image_size)

    img_io = BytesIO()

    im.save(img_io, 'JPEG', quality=20)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
