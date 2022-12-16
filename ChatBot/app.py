from flask import Flask , request , render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainers, ChatterBotCorpusTrainer


app = Flask()


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)