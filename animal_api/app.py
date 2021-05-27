from flask import Flask,request
import random
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

# animal generator route here
@app.route('/get_animal',methods=['GET'])
def get_animal():
    return random.choice(['cow', 'pig','horse'])

# animal noise generator route here
@app.route('/get_noise', methods=['POST'])
def get_noise():
    noises = {
        "cow" : "mooo",
        "pig" : "oink",
        "horse" : "neigh"
    }
    return noises[requests.data.decode('utf-8')]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)