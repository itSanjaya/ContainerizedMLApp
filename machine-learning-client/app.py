from flask import request, Flask, render_template, jsonify
from tensorflow.keras.models import load_model
from quickdraw import *

model, classes = initialize()

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/puzzle')
def puzzle():
    return getObject(classes)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    return jsonify({ 'result': predict(model, classes, data['image'], data['category']) })

if __name__ == '__main__':
	app.run(debug=True)
