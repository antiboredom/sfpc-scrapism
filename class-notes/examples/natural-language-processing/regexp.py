import re

text = "Mr. Hurst and Mr. Bingley were at piquet, and Mrs. Darcy was observing their game."
print(text)

p = re.compile('Mr[a-z]?\. ([a-z]*)', re.IGNORECASE)
for match in p.finditer(text):
  print("Found name: ",match.group(1))
