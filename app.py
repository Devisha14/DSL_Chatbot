from flask import Flask, render_template, request, jsonify, send_from_directory
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Serve CSS file from templates folder
@app.route("/style.css")
def style():
    return send_from_directory("templates", "style.css")


# Serve JavaScript file from templates folder
@app.route("/script.js")
def script():
    return send_from_directory("templates", "script.js")


# Chatbot API
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    bot_response = get_response(user_message)

    return jsonify({
        "reply": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)