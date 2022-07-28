from flask import Flask, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    model = pickle.load(open('../models/'))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)