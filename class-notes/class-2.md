# Sept 25 - Python part 2. Manipulating text. Automating writing

**Instructor**: Sam Lavigne | [splavigne@gmail.com](mailto:splavigne@gmail.com) 
**Teaching Assistant**: Fernando Ramallo | [fernando.ramallo@gmail.com](mailto:fernando.ramallo@gmail.com) 
**Track**: Code Poetry, Fall 2018 
**Location**: School for Poetic Computation | 155 Bank St, New York, NY 10014 **Time**: Tuesdays 10am to 1pm 
**Office Hours**: Tuesdays 2pm to 4pm (or by appointment)

Syllabus: http://github.com/antiboredom/sfpc-scrapism
Slack channel: #2018-fall-scrapism
Sam’s office hours Sign-up sheet: [+Sam Office Hours](https://paper.dropbox.com/doc/Sam-Office-Hours-gaKmWg2Qo7jnn2FbO7F5b) 
Fernando’s office hours sign-up sheet: [+Fernando (TA) Office Hours](https://paper.dropbox.com/doc/Fernando-TA-Office-Hours-p8FxDav0hzpIjrJ4rtfeX) 


# Notes



Fernando gave a presentation about his work

- His website http://byfernando.com/
- His games https://fernandoramallo.itch.io/ (get in touch if you want a free copy of any)

We all went through our assignments


Get you in the mood of using language that you find around.
Juxtaposition


# Readings

Claire Bishop

- Good survey of things that have been done around reutilizing existing language
- attempts to create art that are not commodifiable, a characteristic of social art
- frequently dealing with ethical political concerns
- creating a social space, rather than making an object
- social art isn’t held to same standards as normal art, when judged. is it good art? good activism? sometimes neither. important to take note of / be aware of, when making work that’s aesthetic and activist. 
  - is making an art project the best way to achieve activist goals?
  - is doing an activist project the best way to achieve the artistic goals?
  - set your own ideas for how your work is judged / sometimes it’s not quantifiable
  - 

Detournement 

- different intepretations of it
  - what is the source text advocating for / in using it your erradicating its context
  - you’re renewing its value
  - as a practitioner, what would your desired goal be? make a new thing and destroy the old? give new value to the old through that act?



# Python


# See Sam’s reader with more examples here:

https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-02-python-basics.md



## Using the right version

when you installed python 3, it didn’t remove your old version
if you type python, sometimes it runs the **older** version that comes with Mac, not the one we’ll use

Depending on your settings, you might be able to type ***python*** in the terminal and get the right version, but to make sure you can type **python3**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_B93F4A161C5A44CDAEDBB62D1CDA4B91AEE6CCE1A00E6E4521CF0698C91A37EA_1537886949835_image.png)



**To exit the python console, press Ctrl + D**


## Creating a file with the Terminal

On the terminal:


1. Make a new folder with **mkdir python_lesson_1**
2. Enter it with **cd python_lesson_1**
3. Create a file with **touch hello.py**
  1. **touch** updates a file’s modified date if it exists, otherwise it creates it
4. Open the file with the default editor with **open hello.py**
  1. To change the default editor: right click the file in Finder > Get Info > Change the default app in the Open With section



## Writing our first program

**Print something to the screen:**

On the text editor for hello.py:

    
    print("a specter is haunting europe")
    


Hit save on your editor

Run the program to see its output.
On the termina:

    
    $ python3 hello.py
    
![](https://d2mxuefqeaa7sj.cloudfront.net/s_B93F4A161C5A44CDAEDBB62D1CDA4B91AEE6CCE1A00E6E4521CF0698C91A37EA_1537887306088_image.png)



**Expressions**

python replaces mathematical operations with the value of that operation


    
    # print mathematical operations
    print( 1 + 1 )   # outputs 2
    print( 5 / 33 )
    print( 1 + 7 / 25 * 5 ) 
    


You can compare expressions


    
    print( 1 == 2 )  # returns True or False depending on if 1 equals 2
    
    print( 1 < 2 ) # less than
    print( 1 > 2 ) # greater than
    print( 1 >= 2 ) # equal or greater than
    print( 1 <= 2 ) # equal or lesser than
    print( 1 != 2 ) # not equal
    


You can **comment** parts of code out with # so they’re in your file but they don’t run


    
    print(1+2)
    # print("Hello")
    

Some editors let you comment the code you select with **Ctrl + /**


You can save the value of an expression with **variables**, where you assign a name to an expression or value


    
    some_number = 100
    

the value 100 is now stored in the variable some_number. We can see its value with print()


    
    print(some_number) 
    # Output: 100
    

There’s different **kinds** of values:

- Integer: a whole number (1, 2, 3, 5, 1000)
- Float: a number with decimals (1.55345, 2.0)
- String: a piece of text, defined between quotes (“hello”, “a spectre… “)
- Boolean: True or False
- Lists: a list of items
    
    some_number = 100
    some_float = 10.5
    some_string = "a spectre is haunting europe"
    some_boolean = False
    a_list = [ 1, 100, 20, 25, -305 ]   # a list of integers
    # You can combine types, not a good idea but..
    another_list = [ "hi", 1, 1.53242, False ]
    

The most important for us is going to be


## Strings

A string is a series of characters

we can make a variable that stores a string

we can combine variables to make new values.

If we add two strings together, it **concatenates** them


    
    first_name = "Karl"
    last_name = "Marx"
    
    full_name = first_name + last_name
    
    print(full_name) # Output: KarlMarx
    
    # To put a space between the values
    full_name = first_name + " " + last_name
    print(full_name) # Output: Karl Marx
    

Each character in our string has a numerical index
If we want the first letter, we **access it with brackets and an index** (starting from zero)

    
    first_letter = full_name[0]
    second_letter = full_name[1]
    
    print(first_letter) #Output: K
    

If we use an **index outside of the length of the string**, we get an error

    
    print(full_name[1000]) # Output: IndexError: string index out of range
    


We can use **indices with negative numbers** to start at the end and walk our way backwards:


    
    # Get the last letter
    last_letter = full_name[-1]
    second_to_last_letter = full_name[-2]
    

We can also get **ranges of characters**, this makes python very powerful for our kind of work


    
    print(full_name[0:3]) # Outputs the first three characters: Kar\


We can combine everything we've seen so far:


    
    print(full_name[4:-1]) # Gets a range from the fifth character to the last one
    


We can check for the length of a string, with **len()**


    
    total_characters = len(full_name)
    


I can determine if a string contains another string, using the **in** keyword

- my_string in another_string: return True or False
    
    sentence = "A spectre is haunting Europe"
    
    # is "spectre" inside the sentence?
    print("spectre" in sentence) #Output: True
    
    print("specter" in sentence) #Output: False
    
    
    # it's case-sensitive
    print("Spectre" in sentence) #Output: False
    
    # to make the check case-insensitive, we turn it into lowercase
    print("europe" in sentence) #Output: False
    print("europe" in sentence.lower()) #Output: True .  # Note: doesn't modify sentence


**String methods** lets us manipulate strings in interesting ways:


    
    sentence = "A spectre is haunting Europe"
    
    # Make every character upper case
    print(sentence.upper()) # Outputs: A SPECTRE IS HAUNTING EUROPE
    
    # or lower case
    print(sentence.lower()) #Outputs: a spectre is haunting europe
    
    # capitalize the first letter of each word
    print(sentence.title()) #Outputs: A Spectre Is Haunting Europe
    
    # Use replace to find a word and replace it with another
    print(sentence.replace("is", "was")) #Outputs: A spectre was haunting Europe
    
    # We can chain these operations together
    print(sentence.replace("is", "was").upper()) #Outputs: A SPECTRE WAS HAUNTING EUROPE
    

None of these examples **modify the original value**, but if we want to actually change it

    
    sentence.upper() # only returns the upper case sentence, doesn't modify the variable
    sentence = sentence.upper() # assigns the variable to the newer upper case version
    


You can go through **more string methods** here:
https://docs.python.org/3.7/library/stdtypes.html#string-methods
like center

    
    sentence = sentence.center(30, "*") #puts the character * around the sentence until it's 30 characters long
    


You can also do fun things like **multiplication**

    
    hello = "Hello" * 100
    print(hello) # Outputs: hellohellohellohellohello ...
    
    hello = "hello" + "o" * 100
    print(hello) # Outputs: helloooooooooooooo
    
    hello = "he" + "l" * 1000 + "o"
    
    


We can **combine different types**, but there are different ways

The bad way:

    
    number = 10
    message = "The number is " + number
    # This throws an error (cannot concatenate 'str' and 'int' objects)
    

The OK way, convert a number to a string:

    
    message = "The number is " + str(number)
    

The better way if you have lots of numbers, use format, it’ll replace {} with the number

    
    # one value
    message = "The number is {}".format(number)
    
    # two values
    message = "The number is {} and the 2nd number is {}.".format(number, 100)
    print(message) # Outputs: The number is 10 and the 2nd number is 100
    


## Make the computer say it

In the terminal

    
    python3 strings.py | say
    



## Save the output of a python file to a text file from the terminal


    
    python 3 strings.py > strings.txt
    


## Lists

Make an empty lists.py file
In the terminal:

    touch lists.py
    open lists.py


A lot of methods from strings apply to lists.


    # Declaring a list
    names = ["Marx", "Trotsky", "Lenin", "Engels"]
    
    # Get the length with len(names)
    print("Total names: ", len(names)) # Outputs: 4
    
    # Add items to a list
    names.append("Stravinsky")
    
    # We can declare an empty list
    some_list = []
    
    # You can multiply a list
    print(names * 10) # Outputs a list with the content of the names list 10 times
    
    # You can add lists together
    print(names + some_list)
    
    # You can access individual items by their index starting with zero
    print(names[0]) # First item
    print(names[-1]) # Last item
    print(names[0:3]) # A list with items from the first to the 4th item
    
    


We can go through every item in our list, called **iteration,** using the **for** keyword

    
    # declare a variable name first, then the list we're going through second
    # it'll temporarily store each of the values in the variable name
    for name in names:
      print(name)
    # Outputs: calls print for every item, outputs its value

In other languages a *block* is defined with brackets { }, but in python it’s defined by **white space, using indentation**
Anything that shares the same indentation (e.g. a Tab), is part of the same block

    
    for name in names:
      print(name)
      print("is a dead white guy") # also inside the loop
      
      print("and so is:")  # Still inside the loop
      
    print("That's all the dead white guys in our list")  # Outside of the loop
      




## More 

We’ll grab Kafka’s Metamorphosis from gutenberg
https://www.gutenberg.org/cache/epub/5200/pg5200.txt

Save it to a file next to our python script

We’ll read the text file and store it as a variable
In our python script:

    
    text = open("kafka.txt").read() # the name of the file, relative to where the script is
    
    print(text) # Outputs: the entire text
    
    

Now we can do stuff with it


    
    print(text.upper())
    


To read every single lines, Instead of read() we use readlines()

    
    text = open("kafka.txt").readlines()
    # text is now a list of string items, with each line from the file
    

Now we can iterate over the lines


    
    for line in text:
      print(line) #Outputs each line
      

The problem, it’s putting a space in between each line.
This is because there’s an extra character after a line break, called a newline character
We can get rid of that with strip()


    
    for line in text:
      line = line.strip()
      print(line) # Outputs each line without whitespace or extra line breaks
      


Each of the lines is a string, so we can print parts of each line


    
    for line in text:
      line = line.strip()
      print(line[0:4])
    
    # Output is the first four characters of each line
    

Or do fun stuff like replacing


    
    for line in text:
      line = line.strip()
      print(line.replace('e', 'eeeeeee'))
      



## Processing text

We’re gonna use a function called split() to break downs a string according to a delimiter character.
You can use split() to return a string as a list separated by a character
You can use join() to join a list back into a string

    
    for line in text:
      line = line.strip()
      words = line.split(" ") # Separates the lines by an empty space, getting a list of words
      
      print(words[0]) # Outputs the first word of each sentence
      
      # Chain it all together!
      print(words[0].center(30, '~').upper())
      


We can use the **random** methods to do interesting stuff

Sometimes you have to tell python to add **modules** with the **import** keyword to add functionality you need. Here we’ll import the [random module](https://docs.python.org/3.5/library/random.html). 

- Use the documentation to find what you can do with a module
- Make sure you’re seeing the documentation of the python version you’re using (e.g. 3.5)
    # Import the module
    import random
    
    text = open("kafka.txt").readlines()
    
    for line in text:
      line = line.strip()
      words = line.split(" ")
      
      random_word = random.choice(words)  #Get a random item from the word list
      
      random.shuffle(words) # Randomizes the order of the items in the list
    


We use the join() method to join the randomized word list in to a string

    
    
    for line in text:
      line = line.strip()
      words = line.split(" ")
      random.shuffle(words)
      
      new_line = " ".join(words) # Joins each element in the list by sticking the space character in between the words, outputs a string
      


We can sort with sorted()


    
    for line in text:
      line = line.strip()
      words = line.split(" ")
      random.shuffle(words)
      
      words = sorted(words) # Sort the words list alphabetically
      
      new_line = " ".join(words)
      


Final script

    # Import the module
    import random
    
    text = open("kafka.txt").readlines()
    for line in text:
      line = line.strip()
      words = line.split(" ")
      random.shuffle(words)
      words = sorted(words)
      new_line = " ".join(words)
      print(new_line)


## List comprehension

Make a new file comps.py


We can make a list of upper case’d items

    names = ["Trotsky", "Marx", "Lenin", "Engels"]
    
    uppercase_names = []
    for name in names:
      uppercase_names.append(name.upper())
    
    

There’s a handier way of doing this in python, called **list comprehension.**
This does the same thing as the example above

    names = ["Trotsky", "Marx", "Lenin", "Engels"]
    
    uppercase_names = [name.upper() for name in names]
    

It’s saying: for every value in the list **names** temporarily store it as a variable **name**, make that upper case and store it in a new list called **uppercase_names**


    
    names = [name.replace('r', 'arrrrr') for name in names]
    

We can filter too, by adding **if statements** inside too:

    
    names = [name for name in names if name[0] == "l"]
    # returns elements inside of the list whose first letter is l
    


We can add this filtering technique to the words in our previous example

    import random
    
    text = open("kafka.txt").readlines()
    for line in text:
      line = line.strip()
      words = line.split(" ")
    
      words = [word for word in words if word.startswith("a")]
    
      new_line = " ".join(words)
        
      print(new_line)
      # prints all the words that start with a  

OR more:

      words = [word for word in words if len(word) > 5
      # all the words that have 5 or more characters in them


      words = [word for word in words if word.endswith("ing")]
      # all the words that end in ing



# Assignment for next week

Also available in: https://github.com/antiboredom/sfpc-scrapism

Transform a non-poetic text into a poetic text

- up to you to determine what’s poetic

Read some file, or if the text is short you can just put that text directly into python as  a variable

if don’t know what to do try stuff like sorting, randomizing, replacing, deleting things

by taking something that exists and using these methods we can reformat it, rework it, you can use whatever is at your disposal. you’re not bound by command line, so you can take the output of that text and you’re welcome to format it into something interesting, put it into open frameworkds, whatevr you want to do

Take something that exists, do something that transforms it.

If you’re more advanced, you can start to get into using third party libraries to analyze text.
If you’re feeling ambitious, make this program so that it can deal with any text. Make this poetic operation so it can work with any text that you feed it.


