# --- Section 1: Basic Text Normalization ---
sentence = "Foundation models are massive pre-trained AI Models"
# Convert string to lowercase for case-insensitive processing
sentence_lower_case = sentence.lower()
print(sentence_lower_case)

# --- Section 2: Stopword Removal Setup ---
# Defining a block of text to be cleaned
sentence = """
Foundation models are massive pre-trained AI Models that serve as a common basis for a wide variety of 
application, these models are trained on vast, diverse datasets such as texts, images, code or audio 
allowing them to develop a deep, generalized understanding of patterns and structures 
Example – GPT, BERT, Claude
"""
import nltk
# Download NLTK's English stopword list (words like 'the', 'is', 'a' that add little semantic meaning)
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load the predefined list of English stopwords
en_stopwords = stopwords.words('english')
print(en_stopwords)

# --- Section 3: Applying Standard Stopword Removal ---
# Split the sentence into individual words, filter out those in the stopword list, and join them back
sentence_no_stopwords = ' '.join(word for word in sentence.split() if word not in en_stopwords)
print(sentence_no_stopwords)

# --- Section 4: Customizing the Stopword List ---
# Modifying the existing stopword list: removing 'did' (so it's no longer considered a stopword)
# and adding 'allowing' (so it will now be treated as a stopword)
en_stopwords.remove('did')
en_stopwords.append('allowing')

# Applying the customized filter to the original text
sentence_no_stopwords_custom = ' '.join(word for word in sentence.split() if word not in en_stopwords)
print(sentence_no_stopwords_custom)