# Sept 18 - The Command Line
**Instructor**: Sam Lavigne | [splavigne@gmail.com](mailto:splavigne@gmail.com) 
**Teaching Assistant**: Fernando Ramallo | [fernando.ramallo@gmail.com](mailto:fernando.ramallo@gmail.com) 
**Track**: Code Poetry, Fall 2018 
**Location**: School for Poetic Computation | 155 Bank St, New York, NY 10014 **Time**: Tuesdays 10am to 1pm 
**Office Hours**: Tuesdays 2pm to 4pm (or by appointment)

Slack channel: #2018-fall-scrapism
Sam’s office hours Sign-up sheet: [+Sam Office Hours](https://paper.dropbox.com/doc/Sam-Office-Hours-gaKmWg2Qo7jnn2FbO7F5b) 
Fernando’s office hours sign-up sheet: [+Fernando (TA) Office Hours](https://paper.dropbox.com/doc/Fernando-TA-Office-Hours-p8FxDav0hzpIjrJ4rtfeX) 
 

# Reader
- [Intro to the command line](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-01-the-command-line.md)
- [Python basics](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-02-python-basics.md)
# Notes



- We all introduced ourselves, again!
- We’re gonna assume no technical knowledge, feel free to reach out for questions.
- Sam will record himself giving the class, put it in a private link


## Sam’s work

http://lav.io/

How can we make critical statements without saying specifically what that statement is.

https://lav.io/projects/white-collar-crime-risk-zones/
https://lav.io/projects/baabaa/ - An index of selected commodities listed for sale on alibaba.com. Items are arranged by price and minimum order quantity and are search results for terms like “riot gear” and “human labor”.
https://lav.io/projects/cspan-5/ - most frequently stated phrases turned into a video



## Scrapism

Q of this class: how do we make something new by using material that already exists / 
What new things are sayable today? .. by means of these tools that wouldn’t be sayable otherwise

Objectives

- learn python
- use it to collect material and manipulate it
- use text: how do we create automatic *poetry*
- image: how do we create automatic *collage*
- video: automatic *montage*

Look at groups and individuals from the past that used rule-based techniques / almost automatically / surrealists, dadaists, situationists
We’re gonna be making critiques, satires, commentaries, poetry.
Process:

- find a good source material
- figure out how to get that source material (get a lot of it)
- figure out how to parse it and transform it / take something that is a big mess from the internet, take unstructured information / transform it into something you can use
- figure out how to present what you’ve collected to the world / something new

We’re gonna treat everything *as a text***,** looking at images *as* *if they were* text, e.g. [C-SPAN5 bot](https://twitter.com/cspanfive) (treating video as text that is cut and put together). 

How do these techniques work in a post-Trump environment?
All information is out in the open, does that make this work superfluous?

I saw a horrible website today!
https://anti-captcha.com


## Class today

All the things we’re gonna talk about today are gonna be in these readers:

- [Intro to the command line](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-01-the-command-line.md)
- [Python basics](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-02-python-basics.md)

Every class will have a series of readings (technical and non-technical):

- Technical readings are what we talked about in the class, for reference / when you forget
- The readings are the ones listed in the [syllabus](https://github.com/antiboredom/sfpc-scrapism), *in the slot for the previous class* 



## The Terminal

Applications > Utilities > Terminal
Cmd+Space > “Terminal”


![](https://d2mxuefqeaa7sj.cloudfront.net/s_DB93935784C30DFE0319F4DADC3823BE454C5CF94C07DCD9BB4B5FA46EC71A23_1537283005399_image.png)


The terminal is a text-based way of navigating folders

**Print the directory you’re in:**

    pwd


![](https://d2mxuefqeaa7sj.cloudfront.net/s_DB93935784C30DFE0319F4DADC3823BE454C5CF94C07DCD9BB4B5FA46EC71A23_1537283131928_image.png)




**See what’s in the folder you’re in**

    ls
![](https://d2mxuefqeaa7sj.cloudfront.net/s_DB93935784C30DFE0319F4DADC3823BE454C5CF94C07DCD9BB4B5FA46EC71A23_1537283236404_image.png)


**Change the directory you’re in**

    cd [folder you want to enter]
    
    cd Desktop


![](https://d2mxuefqeaa7sj.cloudfront.net/s_DB93935784C30DFE0319F4DADC3823BE454C5CF94C07DCD9BB4B5FA46EC71A23_1537283219373_image.png)


**The terminal doesn’t understand spaces. Use commas “ to access folders and files with spaces.**


    cd Creative Cloud Files   # doesn't work
    cd "Creative Cloud Files"
    


**Going back: To go back one directory: cd ..**

    cd ..     # goes back to the previous folder


**Making directories: mkdir**

    mkdir [name of the directory]
    
    mkdir newfolder      # makes a folder called 'newfolder'



**Move files and folders and rename them: mv**


    mv [old name] [new name]
    
    mv newfolder/ newnamedfolder     #renames folder 'newfolder' to 'newnamedfolder'

slash means folder, it’s optional

can be used for moving a file, but also be used for renaming


**Creating new files: touch**
Updates the last date modified tag for a file or folder,  to be right now.
If that file doesn’t exist, it **creates that file**
a fast way of making files


    touch [name of file or folder]
    
    touch coolfile.txt       #makes an empty file called 'coolfile.txt'



**Delete**

    rm [name of file]
    
    rm coolfile.txt


**Hit tab to autocomplete a file or folder**

    cd Des[HIT TAB]       # autocompletes to cd Desktop




## Manipulating text

**Use gutenberg for source text**
A good external source to work with is [project Gutenberg](http://gutenberg.org/). 57,000 free eBooks public domain texts.

- Download files in Plain Text format

Moby dick text: https://www.gutenberg.org/cache/epub/15/pg15.txt
The Trial by Kafka: https://www.gutenberg.org/cache/epub/7849/pg7849.txt

Save file as Plain Text Document (or Page Source in Safari)

**See information about the file**

    file [name of file]
    
    file mobydick.txt 
    Output: mobydick.txt: UTF-8 Unicode (with BOM) text, with CRLF line terminators

**Looking inside the contents of a file**

    cat [name of file]   # prints content of the file on the screen
    
    cat mobydick.txt 
    # .... will print the entire text

**Use the ‘more’ command to actually read through the text with scrolling**

    more [name of file]
    
    more mobydick.txt
    # ... scroll through the text
    # ... type Q to exit



**Best command: say**

    say hello
    
    say this is your computer i am going to murder you
    


All the commands have a stucture
***name of command + argument (usually file or folder)***

**But most commands have additional options**
Every single command has a manual built-in. Access it with **man** keyword

    man say
    # will go to the manual about the say command, 
    # exit by typing Q

e.g. -v to change the voice, -f file, -r rate
usually two ways of accessing an option, e.g.

- -r rate
- --rate=rate
    say whatever
    # says 'whatever' at normal rate
    
    say -r 500 whatever
    # says 'whatever' at the rate of 500 words per minute
    
    # use -f option to read a file
    say -f mobydick.txt
    # says the entirety of Moby Dick outloud. Poetic!
    
    


**To stop a command**

- Ctrl + C: Stops the command
- Cmd + Q (Alt + F4 in windows): Closes the terminal entirely


**Use grep command to print every line of a text file that contains a certain word**
a line is understood as every time there’s a carriage return / breaking point / enter in the text

    
    grep trial thetrial.txt
    # prints all the lines of the text file that has the word 'trial'
    
    grep whale mobydick.txt
    
    # to search for more than one word, put it in quotes
    grep "the whale" mobydick.txt
    
    


**Sort comand** 
sorts every line

    sort thetrial.txt
    # returns the trial, alphabetically ordered
    
    sort -u # only uniques
    sort -r # reverse




**Save the output of the command line to a new file, with the > sign**
*this is called a redirect*

    [command] > [file name to save to]
    
    sort thetrial.txt > thetrial_sorted.txt
    # instead of printing, save whatever output to thetrial_sorted.txt file
    


**You can combine commands together**
take the output of one command, pipe it to another command, and chain things together
e.g. do the sort and grep at the same time

    
    # use the vertical bar character (pipe) | to chain commands 
    
    grep whale mobydick.txt | sort
    # take the output of the lines from grep, into the sort command, finally to the screen
    
    grep whale mobydick.txt | sort > sorted_whales.txt
    # make a text file with the lines that include "whale", sorted alphabetically
    


**Other fun commands**

**use cut to separate words**

    cut # breaks every line in the file by a delimiter, 
    # e.g. break the lines by spaces, 
    # -d delimiter
    # -f field
    
    cut -d " " -f 1 mobydick.txt
    # separate the lines by empty spaces (therefore separating each word), get the first field (the first instance, ie. the first word), of mobydick.txt

**use a wildcard to access multiple files**

    ls *.txt
    # lists any file that ends with .txt


**clear to clear the screen**

    clear
    # empties the terminal window




## How the file system works

Files and folders,
Every folder has exactly one parent folder, except the very top (the root)

The root folder (the hard drive) is described as a forward slash /

    cd /
    # goes to the root folder

Some files and folders are **hidden**

    cd /
    ls
    # will list all the files and folders in the root, you'll see some that are hidden in the Finder / Folder viewer

Each file/folder has a unique path
You can go to a specific folder and access a file inside it

    cd /Users/sam/Desktop/
    # go to the desktop
    more thetrial.txt
    # if there's a file called thetrial.txt in Desktop, it gets printed out
    # otherwise, an error

But you can also access a file by its **unique path**, from any other folder

    cd /
    more /Users/sam/Desktop/thetrial.txt

*Tip: Drag a folder or file from the Finder to the terminal and get its unique path without having to type it*

cd can be used to navigate the file system easily

    cd
    # cd with no argument goes to the root folder
    
    cd ../Documents
    # .. means one level up
    # goes one level up, and then down into the Documents folder, if it exists
    # can be combined:
    cd ../../../Desktop   #go three levels up and then into Desktop
    
    cd ./Desktop
    # . means the folder we are currently in
    

**open** opens a file in its default application

    open mobydick.txt
    # opens the text file in TextEdit or notepad
    
    open .
    # opens the folder we currently are in, in the folder viewer (eg. Finder)


**Some tricks to move the typing cursor quickly**
**Shortcuts:**

- Ctrl + A: brings the cursor to the beginning of the line
- Ctrl + E: brings the cursor to the end of the line
- Tab: for autocomplete of commands
  - “gr” + Tab: show all commands that start with gr
- Cmd + D: splits screen to have multiple terminals
- Cmd + N: makes a new terminal window
- Cmd + T: makes a new tab

**Another terminal program**

- iTerm



## Install python + text editor

**Installing python**
Your computer comes with python, but we need a different version.

There’s tons of ways to install python? 
We’re gonna use a tool called **brew** to install stuff with:
https://brew.sh/

Take the main example line, copy paste it into a Termina, hit enter.

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

“It should just work”

Once brew is installed, install python, on a terminal:

    brew install python3
## 

**Installing a text editor**

Doesn’t matter what text editor you use, but a few good ones

- Sublime https://www.sublimetext.com/ **paid but fast!** 
- Visual Studio Code https://code.visualstudio.com/   **free/open source**
- Atom https://atom.io/ **free/open source**

See [Python basics](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-02-python-basics.md) for install instructions

Text editors will color-code a python file to show you different parts.

You can also edit Python files in an **IDE**, “integrated development environment”, they are full platforms for programming, with lots of features. For the purpose of this class we’ll stick to plain text editors.

**Using python**

python is just a command line program (a program that you can use in the Terminal)

you might have more than one python version,
to use the one we’re using type **python3**

**Way ONE to use python: without arguments**

In a terminal window:

    python3


![](https://d2mxuefqeaa7sj.cloudfront.net/s_DB93935784C30DFE0319F4DADC3823BE454C5CF94C07DCD9BB4B5FA46EC71A23_1537288255592_image.png)



    >>> 2+1
    3   # output


To exit the python console, type 

    Ctrl + D
    
    >>> exit()


**Way TWO: next week!**




## Works to look for / Works we’re basing our work on

**Allison Parrish**
http://www.decontextualize.com/

https://twitter.com/everyword
a twitter bot that tweets every single word of the english language in alphabetical order

/ when you make a work for this, what is it you’re doing?
/ closer to a performance
/ the lens of performance can help us understand this work

not just about the bot itself, about the reactions to the bot

/ related to Claire Bishop’s reading

Responses to éclair
[https://twitter.com/everyword/status/475170297776447488](https://twitter.com/everyword/status/475170297776447488)

**Nick Monfort**
256 characters-long one line terminal commands to make poetry
https://nickm.com/poems/ppg256.html

**Everest Pipkin -** Cloud OCR
http://ifyoulived.org/translations.html
Misusing image conversion / analysis
https://procedural-generation.tumblr.com/

what does the cloud say according to the computer
poem

/ it’s broken / a natural lifespan/limit

**Daniel Temkin - Internet Directory**
http://danieltemkin.com/InternetDirectory
A 37k+ page loose-leaf book containing all 115 million .COM domains in alphabetical order, along with current IP addresses.


**Sam’s own - Patent Generator**
http://lav.io/2014/05/transform-any-text-into-a-patent-application/
Output: https://saaaam.s3.amazonaws.com/communist.pdf


**Kate Compton - Tracery**
http://www.tracery.io/
Text generation


/ You can make tools
/ You can share those tools, see what other people make with it
/ You are making a form / with constraints


**Kyle Macdonald - Keytweeter**
[https://vimeo.com/9922212](https://vimeo.com/9922212)
Tweets everything you type



**Great book for learning python**
Learn Python the hard way
https://www.learnpythonthehardway.org/

**Other resources for learning python**
Automate the Boring Stuff
https://automatetheboringstuff.com/

Python for Everybody
https://books.trinket.io/pfe/


## Assignment for next week

Look at python basics
Read 

- [Python basics](https://github.com/antiboredom/sfpc-scrapism/blob/master/reader-02-python-basics.md)
- [Artificial Hells (introduction and chapter 1)](https://selforganizedseminar.files.wordpress.com/2011/08/bishop-claire-artificial-hells-participatory-art-and-politics-spectatorship.pdf) By Claire Bishop
- [A User’s Guide to Détournement](http://www.bopsecrets.org/SI/detourn.htm)


**Find 3 sentences**
You’re gonna assign them to the rest of the class
not too long
they can come from anywhere / internet real world facebook post product packaging menu
as long as you don’t write them yourself

Combine them (one after the other)
either make sense together or not
that creates new possibilities when put together




## WordHack this Thursday! 

[[link]](https://www.facebook.com/events/713754025655700/?acontext=%7B%22ref%22%3A%2229%22%2C%22ref_notif_type%22%3A%22event_aggregate%22%2C%22action_history%22%3A%22null%22%7D&notif_id=1537184173953188&notif_t=event_aggregate)
WordHack is a monthly evening of performances and talks exploring the intersection of language and technology. Code poetry, digital literature, e-lit, language games, coders interested in the creative side, writers interested in new forms writing can take, all are welcome here.

This month we will feature talks and performances by:
JOANNE MCNEIL ([http://www.joannemcneil.com/](http://www.joannemcneil.com/))
MARTIN O'LEARY ([http://mewo2.com/](http://mewo2.com/))
ESTHER SEYFFARTH ([https://user.phil.hhu.de/~seyffarth/index.html](https://user.phil.hhu.de/~seyffarth/index.html))


## Syncrony NYC

Syncrony NYC
http://synchrony.nyc/2019/index.html
Synchrony is a DEMOPARTY that begins in NEW YORK CITY, continues on an Amtrak train, and concludes in MONTREAL.

Synchrony is about being creative with computers, and seeing how computers can produce amazing sorts of animation, graphics, music, and other experiences. At the end we have COMPOS (competitions) that are voted on by those who are there at the party. Some people may work on their entries for these compos for months beforehand; some, just on the train ride up. People are welcome to enter remotely, even if they are unable to attend.


