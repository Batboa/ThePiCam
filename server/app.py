from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "HELLO WORLD"

@app.route('/upload', methods=[ 'POST'])
def upload():
    if request.method == 'POST':
        filename = request.form['filename']
	img_data = request.form['img_data']
        img_data = base64.b64decode(img_data)
	
	f = open('uploads/'+ filename, 'w')
	f.write(img_data)
	f.close()
	
    return "Done"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
