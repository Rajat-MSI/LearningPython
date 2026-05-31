import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Her cat's name is luna, Her dog's name is max"
tokenize_sentence = sent_tokenize(sentence,'english')
print(tokenize_sentence)

tokenize_words = word_tokenize(sentence,"english")
print(tokenize_words)

sentence_lower = sentence.lower()
tokenize_sentence_lower = word_tokenize(sentence_lower,"english")
print(tokenize_sentence_lower)