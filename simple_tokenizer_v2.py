import re

class SimpleTokenizerV2:
  # Initializes with an enumerated Set, vocab
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i: s for s,i in vocab.items()}
  
  # String encoded against existing vocabulary? Should unrecognized text be added to vocab?
  def encode(self, text):
    preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
    preprocessed = [
      item.strip() for item in preprocessed if item.strip()
    ]
    preprocessed = [
      item if item in self.str_to_int 
      else "<|unk|>" for item in preprocessed
    ]
    # What happens if the text contains untokenized strings?
    ids = [self.str_to_int[s] for s in preprocessed]
    return ids

  # Tokens given to decode are translated
  def decode(self, ids):
    text = " ".join([self.int_to_str[i] for i in ids])
    text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
    return text