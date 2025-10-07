# Import "The Verdict" by Edith Warton into root
# The Verdict is a 20,749-character short story with 
# 4690 tokens and 1130 individual words
import urllib.request
url = ("https://raw.githubusercontent.com/rasbt/"
"LLMs-from-scratch/main/ch02/01_main-chapter-code/"
"the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# Test that The Verdict has been downloaded and can be opened
with open("the-verdict.txt", "r", encoding="utf-8") as f:raw_text = f.read()
# print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# Split text by white space
import re
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

# Create an array from items that are not spaces
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# print(len(preprocessed))
# print(preprocessed[:30])

# Convert tokens into token IDs

# Get all words
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

# TODO: Explain this syntax
vocab = {token: integer for integer, token in enumerate(all_words)}

for i, item in enumerate(vocab.items()):
  print(item)
  if i >= 50:
    break

import simple_tokenizer_v1
tokenizer = simple_tokenizer_v1.SimpleTokenizerV1(vocab)
text=""""It's the last he painted, you know,"
      Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))

# Below will error out to illustrate errors with unknown tokens
# text = "Hello, do you like tea?"
# print(tokenizer.encode(text))

# Add special tokens for unknown and endoftext
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token: integer for integer, token in enumerate(all_tokens)}
print(len(vocab.items()))
for i,item in enumerate(list(vocab.items())[-5:]):
  print(item)

import simple_tokenizer_v2
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)

tokenizer = simple_tokenizer_v2.SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))