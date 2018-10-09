# python3 -m pip install spacy
# sudo python3 -m spacy download en
import spacy

pairs = [
  ["A specter is haunting Europe--the specter of Communism.", "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."],
  ["The discovery of America, the rounding of the Cape, opened up fresh ground for the rising bourgeoisie.", "The discovery of Mrs. Philips, the rounding of the daughters, opened up fresh ground for the ball."]
]

# Load English tokenizer  - Other languages: https://spacy.io/usage/models
nlp = spacy.load('en_core_web_sm')

# Similarity
for pair in pairs:
  nlp1 = nlp(pair[0])
  nlp2 = nlp(pair[1])
  print("Phrase 1:  ", nlp1)
  print("Phrase 2:  ", nlp2)
  print("--- Similarity: ", nlp1.similarity(nlp2))
