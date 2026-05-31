import re

import pandas as pd
import nltk
from nltk.corpus import stopwords

data = pd.read_csv("tripadvisor_hotel_reviews.csv")
print(data.head())
data['review_lowercase'] = data['Review'].str.lower()
en_stopwords = stopwords.words('english')
en_stopwords.remove('not')
data['review_no_stopwords'] = data['review_lowercase'].apply(
    lambda x: ' '.join(word for word in x.split() if word not in en_stopwords)
)
data['review_no_punct'] = data.apply(
    lambda x: re.sub(r"[*]","star",x['review_no_stopwords']), axis=1)
print(data['review_no_punct'][0])