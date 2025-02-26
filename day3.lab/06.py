sentence = "the quick brown fox jumps over the lazy dog"

# Split sentence into words and count frequency using dictionary comprehension
word_freq = {word: sentence.split().count(word) for word in set(sentence.split())}

# Print word frequency dictionary
print(word_freq)
