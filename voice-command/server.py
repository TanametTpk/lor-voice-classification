from flask import Flask, request, jsonify, render_template
from commander import contextSelection

app = Flask(__name__)

@app.route('/actions', methods=["POST"])
def makeActions():
    content = request.json
    print(content["msg"])
    if "msg" in content:
        contextSelection(content["msg"])
    return jsonify({"status": 200})

@app.route('/webhooks', methods=["POST"])
def webhooks():
    contents = request.json
    print(contents)
    for content in contents:
        if "message" in content:
            contextSelection(content["message"])
    return jsonify({"status": 200})

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)