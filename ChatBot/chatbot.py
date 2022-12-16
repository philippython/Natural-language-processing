from chatterbot import ChatBot
from chatterbot.trainers import ListTrainers, ChatterBotCorpusTrainer

# creating chatbot instance
Vennote_Bot = ChatBot("VennoteBot", )


# Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

list_trainer = ListTrainers(Vennote_Bot)
list_trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(Vennote_Bot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 