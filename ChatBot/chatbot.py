from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# creating chatbot instance
Vennote_Bot = ChatBot("VennoteBot",storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',
                    'chatterbot.logic.BestMatch',
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand. I am still learning.',
                        'maximum_similarity_threshold': 0.90
                    }
                ],
                database_uri='sqlite:///database.sqlite3' )

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

list_trainer = ListTrainer(Vennote_Bot)
list_trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(Vennote_Bot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 