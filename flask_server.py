from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mysocial')
def mysocial():
    return 'Welcome to mysocial'

if __name__ == '__main__':
    app.run(port=5001)