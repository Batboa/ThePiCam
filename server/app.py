from flask import Flask, jsonify, request, render_template
import base64
from pymongo import MongoClient
import hashlib

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def isValidCode(code):
    hashVal = hashlib.sha256()
    hashVal.update(code)
    value = collection.find_one({'code':hashVal.hexdigest()})
    if value == None:
        return False
    else:
        return value['valid']

app = Flask(__name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=[ 'POST'])
def upload():
    if request.method == 'POST':
	code = request.form['code']
        if not isValidCode(code):
	    raise InvalidUsage('Invalid Code', status_code=401)
        filename = request.form['filename']
	img_data = request.form['img_data']
        img_data = base64.b64decode(img_data)
	
	f = open('uploads/'+ filename, 'w')
	f.write(img_data)
	f.close()
	
    return "Done"

if __name__ == '__main__':
    client = MongoClient()
    db = client['PiCam']
    collection = db['Authentication']
    app.run(host='0.0.0.0')
