import re
from collections import Counter

def wordcount(text: str) -> dict:
    # Remove punctuation (considering spaces around words and punctuation marks) and convert to lowercase
    text = re.sub(r'[!?.]', '', text).lower()
    text = re.sub(r'[^\w\s]', '', text)  # Removes commas and other remaining punctuation
    # Split the text into words
    words = text.split()
    # Count the occurrences of each word
    word_count = Counter(words)
    return dict(word_count)

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

# Get the word count
word_count_result = wordcount(text)
print(word_count_result)
