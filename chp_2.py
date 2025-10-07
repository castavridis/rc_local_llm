# Import "The Verdict" by Edith Warton into root
# The Verdict is a 20,749-character short story with 4690 tokens
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
print(preprocessed[:30])