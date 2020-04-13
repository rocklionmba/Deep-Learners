from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    # if error return null
    return {
        "result" : 10
    }
