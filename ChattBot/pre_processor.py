import nltk
from nltk import sent_tokenize, word_tokenize

with open("corpus.txt", "r") as corpus:
    text = corpus.read().lower()
    text_sent_token = sent_tokenize(text)
    text_word_token = word_tokenize(text)
    print(text_sent_token[0:2])
    print(text_word_token[0:2])

