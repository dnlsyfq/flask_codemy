from flask import Flask, render_template
from helper2 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)