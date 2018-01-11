from flask import Flask, request
app = Flask(__name__)

@app.route("/android", methods=["GET", "POST"])
def android():
    postData = request.args['input']
    return "Hello " + postData

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
