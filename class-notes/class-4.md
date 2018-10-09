# 10/09 - Natural Language Processing

Raise your hand if you’ve had problems scraping

Scraping is more art than science

We’ll see other ways of scraping you can try

We’ll get into basics of natural language processing, using TextBlob, maybe a bit of SpaCy.

Who wants to share their lists?

- Elizabeth scraped foundation colors and sorted them
- Edgardo showed their Playlist Of The Chilean Dictatorship, scraping Billboard’s Top 1 hit during the dictatorship years
- Tomoya scraped Youtube and sorted thousands of thumbnails of recommended videos
- Tim scraped pictures of Plan-B



## Problem: Scraping google images, would return HTML without my content

Things to try:

**View source**

**Turn off Javascript**

- Turn off Javascript, then load a page
  - you’ll get a legacy page in simple HTML, sometimes for certain sites

**Use the Network tools**

- View > Developer Tools > Network
- You can see all the network requests from the browser to the server
  - So you can see, eg. images that are being loaded
  
![](https://d2mxuefqeaa7sj.cloudfront.net/s_EF94E54173BB9AD30672FE5689D53FCD672AC2999755231FC9590FA02D6C9AFF_1539096267653_image.png)

- You can get links from there, and content in JSON format
- Sometimes it’s easier than parsing the HTML itself

For getting results of a search:

1. Look for what looks like it has results, filter by XHR
2. right click > Copy > Copy link address
  1. sometimes will give you a link to a JSON with all the results
    - a Chrome extension for Beautifying JSON: JSON Formatter
3. You can hit Next, see what the new URL is, see what changed, maybe you can see how to get different pages

**Read the JSON in python:**

    import requests
    
    r = requests.get("....... crazy URL you got from network")
    
    # convert it to a JSON object
    data = r.json()
    
    # access its elements
    print(data["results"]["total_num_results"])
    
    # it gets bonkers
    print(data["results"]["cluster"][0]["patent"]["result"][0]["title"])
    


Network doesn’t work in cases like Twitter, where there’s no Next button, you just scroll down and it loads automatically

**When the JSON link gives you an error, use cURL**


1. Right click > Copy > Copy as CURL
2. Paste on a Terminal
  1. Now you’ll get the actual result of a query

You can paste a curl command on this online tool, and return a python requests command:

  https://curl.trillworks.com/




# Natural Language Processing

What is it?

  get computers to understand language, extract meaning from text
  Convert characters into some kind of data the computer understands and we can do something with.

We can get computers to:

- extract sentences
- get words
- for each word figure out what kind of word it is (Part of speech)
- Understand the sentiment of a text
- Classify text
  - here’s a bunch of negative sounding sentences, positive sentences, here’s a new sentence, is it positive or negative?

Based on rules, as machine learning or if else statements.
There’s a lot of biases

- what the computer determines has some form of ideology, coming from the creator’s intention, consciously or not



## TextBlob

We’ll use a library called TextBlob
https://textblob.readthedocs.io

Lets us

- basic NLP tasks
- easy-to-use
- tradeoff is that it’s less accurate than other libraries
  - other library, better, but more annoying to use: SpaCy
    - https://spacy.io/

**Installing**
On the terminal:

    
    $ pip3 install textblob
    

Install the data set

    
    $ python3 -m textblob.download_corpora
    

**Basic usage**

Breaking into sentences:

    
    from textblob import TextBlob
    
    blob = TextBlob("A specter is haunting this classroom. The specter of sleepiness.")
    
    print(blob.sentences)
    # Outputs a list of Sentence object
    
    # Iterate through all the sentences
    for sentence in blob.sentences:
      print(sentence)
      
    # Get all the words, removing the punctuation
    for word in blob.words:
      print(word)
    
    # Get the POS / part of speech (nouns, adjectives, etc.)
    for tag in blob.tags:
      print(tag) # Outputs a tuple (list you can't change) ('specter', u'NN'): the word, the part of speech
      print(tag[0]) # Word
      print(tag[1]) # POS
    
    # Get all the nouns
    nouns = []
    for tag in blob.tags:
      if tag[1] == "NN":
        nouns.append(tag[0])
    print(nouns)
    


Tags for Part of Speech

- Penn Treebank part of speech tagging system
  https://www.clips.uantwerpen.be/pages/mbsp-tags


Pluralize words

    
    for word in blob.words:
      print(word.pluralize(,))
    


Classify sentences between positive and negative ones, using a simple training set


    from textblob import TextBlob
    from textblob.classifiers import NaiveBayesClassifier
    train = [
        ('i am happy today', 'pos'),
        ('this is a good burger', 'pos'),
        ('you\'re a good boy', 'pos'),
        ('you are doing well', 'pos'),
        
        ('i do not like you', 'neg'),
        ("don't go there", 'neg'),
        ('this is so frustrating', 'neg'),
        ('things are bad', 'neg')
    ]
    cl = NaiveBayesClassifier(train)
    sentence = "I feel really bad"
    # Classify a sentence
    print(sentence,"is",cl.classify(sentence))
    # Get the probability
    prob = cl.prob_classify("I don't like tings")
    print("The probability that this sentence is negative is", prob.prob("neg"))
    print("The probability that this sentence is positive is", prob.prob("pos"))
    
    # Get all sentences of a certain category
    for sentence in blob.sentences:
      if (cl.classify(sentence) == "pos")
        print(sentence)
      
      # only if they have less than three words
      if len(sentence.words) < 3:
        print(sentence)
        


Get the sentiment (biased, unreliable)

    
    for sentence in blob.sentences:
      print(sentence.sentiment) # Returns a Sentiment object with a polarity value and a subjectivity value
      
      # Print only the positive sentences
      if (sentence.sentiment.polarity > 0.8)
        print(sentence)
        



# Natural Language Processing Examples

https://github.com/antiboredom/sfpc-scrapism/tree/master/class-notes/examples

# More Tools for NLP
## SpaCy
- https://spacy.io/usage/


## Concept Net
- http://conceptnet.io/
- synonyms, related terms, used for…, types
  - Use the same URL but add api., for seeing what’d you get with the API
    - http://conceptnet.io/c/en/glass
    - http://api.conceptnet.io/c/en/glass

Using the concept net API

    
    import requests
    
    word = "glass"
    r = requests.get("http://api.conceptnet.io/c/en/" + word)
    data = r.json()
    
    

Click a header, e.g. used for

http://conceptnet.io/c/en/glass?rel=/r/UsedFor&limit=1000

Get the API URL for all things glass is used for

http://api.conceptnet.io/c/en/glass?rel=/r/UsedFor&limit=1000

*edges* = the ways in which this word relates to other words

- *edges* has a *start* and a *end* ([start] is used for [end])*,* we want the *end*
    
    for edge in data["edges"]:
      if edge["rel"]["label"] == "UsedFor":
        print(edge["start"]["label"])
      

A project made with this:

- Darius Kazemi’s expanding mind bot
  - https://twitter.com/expandingbot




# Tips
## how to publish code to github without personal information
- Make a secrets.py that has your logins, or passwords or API keys, that you’re using in your code
- add it to .gitignore so it doesn’t get pushed to the server



## a prettier print() statement


    from pprint import pprint
    
    pprint(json)
    



# Homework TBD

