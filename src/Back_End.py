from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1>Threat Intelligence Platform Home</h1>"

@app.route('/dashboard/')

def OSINT():
    return "<h1>Place OSINT tools here</h1>"


if __name__ == "__main__":
    app.run(debug=True)
