# 10/02 - Dictionaries, scraping the web



# Dictionaries

List = collection of items ordered numerically
Dictionary = no order, the items are indexed by another variable (usually a String)



On the terminal
Make a new file and open it

    
    $ touch dicts.py
    $ open dicts.py


**Dictionaries are Key and Value pairs**
They’re used to represent structures of data

In python, you define dictionaries with curly brackets { }

    
    person = { } # empty dictionary
    
    person = { "first_name": "Karl, "last_name": "Marx", "age": 235 }
    
    # An easier way to look at it:
    person = { 
      "first_name": "Karl, 
      "last_name": "Marx", 
      "age": 235 
    }
  

“first_name” is the **Key**, “Karl” is the **value**

the values can be of any type: int, float, boolean, Strings, or even other dictionaries

**Dictionaries can contain any type, including dictionaries and lists**

    
    person = { 
      "first_name": "Karl", 
      "last_name": "Marx", 
      "age": 235,
      "pet": {
        "name": "Proleterry",
        "species": "parrot",
        "age": 12
      },
      "favorite_books": ["Ethics", "Twilight"]
    }
    


You’ll want to do things with values in the dictionary


## Getting values

**You can get a value from a dictionary using brackets and accessing the key**
The key has to be exactly the name of the key, e.g. first_name
If it doesn’t exist, an error halts the program

    
    # 1. access the value using brackets by referencing the key
    print( person["first_name!"] ) #Outputs: KeyError, there is no key names first_name!
    
    print( person["first_name"] ) #Outputs: Karl
    

**A safer way is to use the get method,**
Returns None without an error if the key isn’t present

    
    name = person.get("first_name")
    

Sometimes dictionaries will have nested values, like a list and dictionaries, so you’ll **iterate** through the values

    
    for book in person["favorite_books"]:
      print(book)
      


## You can iterate through a dictionary 

and get all its properties

    
    for key in person:
      print(key) # prints all the keys
      print(person[key]) # prints all the values
      


## Adding and modifying the dictionary

Accessing a key and modifying its value will override the value for that key:

    
    # replaces the value for first_name
    person["first_name"] = "Lenin"
    

If the key doesn’t exist, you can create it and assign a value

    
    person["middle_name"] = "Terry"
    # now there's a new key middle_name with value Terry
    




# Intro to HTML

HTML is a markup language, that the web is written in.


## Tags

Works as a series of **tags**
A tag looks like

    \<tagname\>some stuff\</tagname\>

The beginning of the tag, the contents of it, and the closing of a tag

There’s different types for different things

- \<p\> paragraph
- \<strong\> makes text bold
  - this text is normal and \<strong\>this text is bold\</strong\>
- \<a\> makes a link
  - \<a href=”http://www.google.com\>go to google\</a\>
- \<h1\> makes a header
  - \<h1\>My Header\</h1\>
- \<div\> represents a random division of text
  - \<div\>I’m a div\</div\>


## Attributes

Each tag can have a series of attributes, a set of **key** and **value** pairs
Two most important ones for scraping is

- **id** attribute 
  - gives a unique identifier to a particular tag
    - \<p id=”the-most-important-paragraph”\>Hi I’m very important\</p\>
  - an id can only be applied to one tag
- **class** attribute
  - designates a category of tag, that the author of the page uses to find or group
  - you can have multiple tags with the same class
    - \<p class=”moderately-important”\>I am somewhat important\</p\>
    - \<p class=”moderately-important”\>I am also somewhat important\</p\>


## Specific attributes

There’s some attributes that can only be applied to certain tags

- **href** is only applied to \<a\> to indicate where to go when you click on a link
  - \<a href=”http://www.google.com”\>google\</a\>
- **src** only applied to \<img\> to indicate which image
  - \<img src=”logo.png\>


## Structure

A web page looks like this

    
    \<html\>
      \<head\>
        \<title\>My page title\</title\>
      \</head\>
      \<body\>
        \<h1\>Hello i am header\</h1\>
    
        \<p\>a paragraph\</p\>
        
      \</body\>
    \</html\>


## CSS

Cascading Style Sheets, 
just know that CSS is used to apply style to a page
so the HTML stays the same for the content but the CSS indicates text color, sizes, etc.

it’s comprised of a selector, that references a part of the page, brackets that contain style

A CSS style sheet looks like this

    // this sets all the p tags to have a red border
    p {
      border: 1px solid red;
    }
    

Different selectors

    
    // style the p tags and all the strong tags
    p, strong {
    }
    
    // style all the \<a\> tags inside all the \<p\> tags
    p a {
    
    }
    
    // style everything with a certain class name, preseed with a period
    .moderately-important {
    
    }
    
    // style an id, using #. e.g. style this \<p id="logo"\>logo text\</p\>
    #logo {
    
    }
    
    // style the \<a\> tags inside \<p\> tags, but only if they're a certain class
    p a.moderately-important {
    
    }
    
# Web scraping


Open Chrome


## View source 

go to a website
e.g. https://newyork.craigslist.org/d/antiques/search/ata

Right click \> View Source
to see the source code



## See source code for specific elements

Right click \> Inspect

Highlights the part of the website as you hover over the source code.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491358282_image.png)





## To scrape you want to figure out how to find a certain element

We right click a header and inspect the structure of the page where that element is.

We see that it’s a specific **class**, so we can find all elements of that class to see if that gives us all the headers/

We right click a craigslist header and find:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491758062_image.png)


we see that its class attribute says **result-title,** and that it’s inside an **\<a\>** tag
so we’ll try to find **all the \<a\> tags with the result-title attribute, to find all the headers**

## Testing inside the browser

You can quickly find elements inside the browser using the **Console.**

you can use the document.querySelectorAll() that takes one argument that is a css selector


    
    document.querySelectorAll("h2") // finds all the h2 tags
    




## Getting the CSS selector for an element automatically

On the console:
Right click \> Copy \> Copy Selector
gets you the CSS selector
**but this only helps sometimes**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491844671_image.png)




# How do we translate this into Python and make it automatic?

We’ll use a library called requests-html


- Documentation, How Tos
  - https://html.python-requests.org/
  

It’s a library and you can scrape HTML pages with it

To scrape a page:

- First you download the page, then you convert it into a python data structure you can manipulate
- Getting the HTML involves downloading the page and getting all the text
- The second part is called **parsing**, going through the text and getting data from it


## Installing the library

You can install libraries in self-contained environments, or globally. 

On the terminal:

    $ pip3 install requests-html




## Using it

On a new python file

    
    #import the library
    from requests_html import HTMLSession
    
    # create a new session
    session = HTMLSession()
    
    # open a website
    r = session.get("https://newyork.craigslist.org/d/missed-connections/search/mis")
    
    print(r) # returns if it was able to open the page or not
    
    

**You can find items in the page using css selectors**

    
    titles = r.html.find(".result-title")
    
    for title in titles:
      print(title) # prints out the entire tag
      
      print(title.text) # prints out the text inside the tag
      
      

**You can access tags from the items in the page**

    
    for title in titles:
      print(title.attrs["href"]) # gets the URL in the href attribute
      
      print(title.attrs.get("href")) # a safer way, since some tags might not have the attribute
      

**We want to also get the description, so we can tell the computer to click on a link and get a part of that other page**

**We also want to get a single element of a page**

    
    
    titles = r.html.find(".result-title")
    for title in titles:
      url = title.attrs.get("href")
      name = title.text
      
      # open the URL we found
      r = session.get(url)
      # we found the part of the page we want in the article page has an id "postingbody"
      # so we get the part of the page with the id (ids are prefaced by #)
      content = r.html.find("#postingbody", first=True)
      
      if (content.text) # only if we found something
        print (content.text)
      
        # without the first=True attribute we'd get a list, and content.text would throw an error
      content = r.html.find("#postingbody")
      

**Errors from r.html.find()**
You might get an error for a few reasons

- It couldn’t find that element

**Mitigate the requests to not get banned with the time module**

    
    # at the top of the page, import the time module
    import time
    
    # use the sleep method to stop the script
    for title in titles:
      time.sleep(0.2) # stop the script for 0.2 seconds
      #...
      



## Full script
    import time
    from requests_html import HTMLSession
    
    session = HTMLSession()
    r = session.get("https://newyork.craigslist.org/d/missed-connections/search/mis")
    
    titles = r.html.find(".result-title")
    for title in titles:
      url = title.attrs.get("href")
      name = title.text
      
      r = session.get(url)
      content = r.html.find("#postingbody", first=True)
      
      if (content.text) # only if we found something
        print (content.text)
      
      sleep(0.2)
      



## Other ways of parsing a page

Instead

You can have a for loop that goes through the html object

- It’ll use **intelligent pagination** where it automatically looks for “next” links, and gives you all the subsequent pages, e.g for search results
- This is easier sometimes
    
    for html in r.html:
      titles = html.find(".result-title")
      
      for title in titles:
        print(title)
      



## Getting multiple items

In alibaba search results, we might want to get several elements of a post, instead of finding both elements separately we can get the whole post.

alibaba.py

    
    from requests_html import HTMLSession
    session = HTMLSession()
    
    r = session.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=drugs")
    
    

We inspect the title we want


![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538495567641_image.png)


we go up the hierarchy, hovering over the code and find what fills up the entire post

we find \<div class=”item-content”\> contains the entire box

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538495625813_image.png)


so we get the box on our python script

    
    # find the box by using the class we found
    items = r.html.find(".item-content")
    
    for item in items:
      # now we have the whole item
      print(item) #returns \<Element 'div' class=('item-content',)\> showing we're getting an element
      
      # we find the price class in the item
      price = item.find(".price", first=True).text
      # we find the title
      title = item.find(".title", first=True).text
      
      print(title + " costs " + price) # returns Pain Pills Raw... costs $1.00
      




## Downloading images

https://github.com/antiboredom/detourning-the-web-2018/blob/master/week_04/shutterstock.py


    import requests
    
    def download_file(url):
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        return local_filename
    




## Some websites have barebones HTML without the content

If the content of the HTML is barebones (like facebook) that means the content is loaded AFTER the HTML is downloaded

to help with that we can use the render() function to grab the full text of the page the way you’d see it in Chrome

    r.html.render()



# Homework

Make a big list using this technique

of whatever you want

There should be a reason to make that big list (a poetic, political, satirical, surrealist reason)

You’re welcome to manipulate that list in some way



# Next week

More advanced tools for analyzing language
natural language processing

if you want a head start, the libraries to look at are:

  - TextBlob https://textblob.readthedocs.io/en/dev/
  - Spacy https://spacy.io/




# More resources

**Understanding Word Vectors by Allison Parrish**
[https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469](https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469)




