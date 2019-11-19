from flask import Flask,jsonify
import re
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


CORS(app, origins="http://127.0.0.1:5000", allow_headers=[
    "Content-Type","Access-Control-Allow-Origin"])

@app.route('/searchword/<keyword>',methods=['GET'])
def search_keyword(keyword):
    out = re.sub('[^A-Za-z]+', ' ', keyword)
    list_ = ['topmost relevant document','second relevant document','third relevant document']
    if out:
        return jsonify({'out': list_})

if __name__ == '__main__':
    app.run(debug=True)