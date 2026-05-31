import re

# --- Section 1: String Handling ---
# Standard string: backslashes must be escaped
file_path = "C:\\desktop\notes"
print(file_path)

# Raw string (r""): Treats backslashes literally, which is critical for Regex and file paths
new_file_path = r"C:\\desktop\notes"
print(new_file_path)

# --- Section 2: Basic Pattern Matching ---
# re.search scans the string for the first location where the regex pattern produces a match
search_result1 = re.search("pattern",r"string to contain the pattern")
print(search_result1)

search_result2 = re.search("pattern",r"the phrase isn't present in the string")
print(search_result2) # Returns None if no match is found

# --- Section 3: Text Substitution ---
# re.sub finds the pattern in the string and replaces it with the specified replacement
sentence = "Text Classification – Assigning Predefined labels to text like spam or topic categories"
subs_sentence = re.sub("text","email",sentence)
print(subs_sentence)

# --- Section 4: Advanced Pattern Searching Utility ---
reviews = [
    "amazing! work from john.",
    "sarah did good...",
    "mike makes good coffee :)",
    "sam is scammer!!",
    "sarah makes good noodles.",
    "sara deserves a promotion",
    "best!! employee mike"
]

def pattern_search(pattern_to_find, review_list):
    """Filters a list of strings based on a provided regex pattern."""
    list_review = []
    for item in review_list:
        if re.search(pattern_to_find, item):
            list_review.append(item)
    return list_review

# Quantifier: '?' makes the preceding character 'h' optional (matches 'sara' or 'sarah')
pattern = r"sarah?"
sarah_reviews = pattern_search(pattern,reviews)
print(sarah_reviews)

# Anchor: '^' matches the start of the string
pattern = r"^a"
a_reviews = pattern_search(pattern,reviews)
print(a_reviews)

# Anchor: '$' matches the end of the string
pattern = r"e$"
e_reviews = pattern_search(pattern,reviews)
print(e_reviews)

# Grouping and Alternation: '|' matches 'noodl' OR 'deserv' followed by 'es'
pattern = r"(noodl|deserv)es"
x_reviews = pattern_search(pattern,reviews)
print(x_reviews)

# --- Section 5: Data Cleaning (Punctuation Removal) ---
# Character Class: [^\w\s] matches any character that is NOT a word character (\w) or whitespace (\s)
pattern = r"[^\w\s]"
y_reviews = []
for review in reviews:
    # Use re.sub to replace identified punctuation with an empty string
    no_punc = re.sub(pattern,"",review)
    y_reviews.append(no_punc)

print(y_reviews)