from nltk.tokenize import sent_tokenize , word_tokenize


text = """Muad'Dib learned rapidly because his first training was in how to learn.
        And the first lesson of all was the basic trust that he could learn.
        It's shocking to find how many people do not believe they can learn,\
        and how many more believe learning to be difficult
        """

print(sent_tokenize(text))
print(word_tokenize(text))