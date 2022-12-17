from flask import Flask , request , render_template
from chatbot import Vennote_Bot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(Vennote_Bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)