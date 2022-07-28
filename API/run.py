from flask import Flask, jsonify, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        model = pickle.load(open('../models/'))
        user_input = request.form.get('variable_1')
        model.predict([[user_input]])
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)