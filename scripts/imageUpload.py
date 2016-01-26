import requests
import base64

def uploadImage(url, fileName, code):
    with open(fileName) as img_file:
        img_data = base64.b64encode( img_file.read() )
    data = {'filename':fileName, 'img_data':img_data, 'code':code}

    r = requests.post(url, data=data)
    return r.status_code
