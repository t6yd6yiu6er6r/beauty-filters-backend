from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/notify", methods=["GET"])
def notify():
    return jsonify({"message": "Don't forget to save your memories!"})

if __name__ == "__main__":
    app.run(debug=True)
