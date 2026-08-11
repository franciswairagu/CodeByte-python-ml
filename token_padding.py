# ==================================
# Question 
# ==================================

"""
Preprocess a list of texts using tensorflow keras libraries.
Remove any empty or whitespace only strings and tokenize those texts into integer sequences
After tokenization , pad the sequences so that they all have equal length.
Finally print the tokenized and padded sequences.
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

texts = ["Sky is blue", "I love python", "Chatgpt is by OpenAI", " "]

def preprocessor(texts):
    """
    Takes in a list of texts tokenize and pad them
    And returns the tokenized sequences and the padded sequences
    """
    # Remove empty or whitespaces only strings
    cleaned_texts = [text for text in texts if text.split()]

    # Tokenize texts 
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(cleaned_texts)

    tokenized_sequences = tokenizer.texts_to_sequences(cleaned_texts)

    # Add padding 
    padded_sequences = pad_sequences(tokenized_sequences, padding="post")

    return tokenized_sequences, padded_sequences

tokenized_sequences, padded_sequences = preprocessor(texts=texts)
print(f"\nOriginal texts:\n{texts}")
print(f"\nTokenized sequences:\n{tokenized_sequences}")
print(f"\nPadded sequences:\n{padded_sequences}")