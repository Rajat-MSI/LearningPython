from nltk.stem import PorterStemmer

ps = PorterStemmer()

connect_tokens = ['connecting','connect','connectivity','connected','connects']

for x in connect_tokens:
    print(x, ": ", ps.stem(x))

learn_token = ['learned','learning','learns','learner','learn','learners']

for x in learn_token:
    print(x, ": ",ps.stem(x))

likes_token = ['likes','better','worse']

for x in likes_token:
    print(x,": ", ps.stem(x))