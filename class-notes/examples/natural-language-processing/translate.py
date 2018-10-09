from textblob import TextBlob

text = open("pride.txt").read()[0:2000]
en_blob = TextBlob(text)

# Translate
# Language codes in: https://cloud.google.com/translate/docs/languages
# es_blob = en_blob.translate(to="es")

# Translate there and back
print("Translating...")
blob = en_blob.translate(to="es").translate(from_lang="es", to="en").translate(to="sw").translate(from_lang="sw", to="en")
output = str(blob)

# print(str(sentence),">>>",crazy_sentence)  

# Save to a file
f = open("output_parts-of-speech.txt", "w")
f.write(output)
f.close()

print("Done!")
