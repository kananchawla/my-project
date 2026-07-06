

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevSecOps! The server is fully functional!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
