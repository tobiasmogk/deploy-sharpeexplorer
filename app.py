from flask import Flask
app = Flask(__name__)

@app.route('/tobi')
def hello_tobi():
    return 'Hello, Tobi!'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

