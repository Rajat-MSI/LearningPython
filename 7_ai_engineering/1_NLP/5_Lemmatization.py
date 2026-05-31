import nltk
nltk.download('wordnet')
from nltk.stem import  WordNetLemmatizer
lemma = WordNetLemmatizer()

connect_tokens = ['connecting','connect','connectivity','connected','connects']

for x in connect_tokens:
    print(x, ": ", lemma.lemmatize(x))

learn_token = ['learned','learning','learns','learner','learn','learners']

for x in learn_token:
    print(x, ": ",lemma.lemmatize(x))

likes_token = ['likes','better','worse']

for x in likes_token:
    print(x,": ", lemma.lemmatize(x))