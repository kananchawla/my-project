

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevSecOps! The server is fully functional!"


@app.route('/health')
    return jsonify({
        "uptime": 999,
        "version": "1.0"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
