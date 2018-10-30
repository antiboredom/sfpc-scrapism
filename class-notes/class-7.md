# 10/30 - Bots



# Troubleshooting videogrep

Some students had problems with videogrep!


            “The right attitude is… it’s amazing it works at all!” - Sam


- **bool is not iterable** might mean it didn’t find the subtitle or video file

Make sure

- Subtitle file name is the same as video file name, and it can end in .vtt OR .en.vtt
- Videos might need to be the same size
- Keep all videos the same format and size
  - Make sure youtube-dl gets the same format and size by using the -f setting (-f 22 gives you a 1280x720 video on youtube, use capital F (-F) to see what formats there are)
  - Convert using ffmpeg: (-vcodec copy means the video doesn’t get reencoded = faster)
    - ffmpeg -i myvideo.mkv -vcodec copy myvideo.mp4 
- If a video has youtube auto-generated subtitles, it’ll have **word** **by word** timings. If it’s subtitles uploaded by the user it might have **sentence by sentence** timings.
  - look at the subtitle file, look for <c> tags surrounding each word, and a timestamp tag next to it
  - you can use sphinx to transcribe the videos so they’ll all have the same format
- **The word i’m searching for is in the vtt, but videogrep doesn’t find it**
  - check the vtt, if that word doesn’t have timing tags for only that word, and instead it’s part of a sentence, videogrep might not find it
    - use sphinx to transcribe the video



To test a regular expression
https://regex101.com/



# Bots bots beep boop

Today:

1. How we can write python code we can use in multiple contexts
  1. You want to write code that’s reusable / acts like a tool
  2. We’ll be able to write one file that does something with any kind of input
  3. Can be used from another script
  4. Applicable to other programming languages

We’ll make an example script, and then we’ll make it modular.

- Take a video of a sunset
- overlay a word
  - the word will be different



## The script

We got a video of a sunset from youtube

https://www.youtube.com/watch?v=Nl3S8VhUxfY&


We’ll clip it to start at 01:48 until 01:52

    
    # Import VideoFileClip to load a video, 
    # TextClip to overlay text, and CompositeVideoClip 
    # to take two or more clips and overlay them as layers
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
    
    text = "A specter is haunting this sunset"
    
    # Load the video, get a subclip that's just our small range, in seconds
    clip1 = VideoFileClip("sunset.mp4").subclip(108, 112)
    # Make a text clip, give it a duration
    clip2 = TextClip(text).set_duration(4)
    
    # Make a composite video, takes a list of clips
    composition = CompositeVideoClip( [ clip1, clip2 ] )
    
    # Export the video
    composition.write_videofile("sunset_words.mp4")
    

Problems with this code

- The text is tiny
  - We didn’t tell the text what size to make it
- the video is a bit big, it’ll faster if we resize it
- we want the text clip to be the same size as the video

Options for TextClip: https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=textclip#textclip


## Making it modular

We want to reuse this code, so we’ll turn all of this into a **function** with def, and turning the code into a block

Also, we want to use arguments from the terminal to **reuse the script with any text we want**, by using sys.argsv

**vidbot.py**

    # Import VideoFileClip to load a video, 
    # TextClip to overlay text, and 
    # CompositeVideoClip to take two or more clips and overlay them as layers
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
    
    def compose(text):
      # Load the video, get a subclip that's just our small range, in seconds
      # e.g. start time is one minute, 48 seconds = 60 + 48 = 108
      # Then resize it to make it faster, resize takes a tuple
      clip1 = VideoFileClip("sunset.mp4").subclip(108, 112).resize( (1920/2, 1080/2) )
      # Make a text clip, give it a duration
      # We'll also make it the size of the video clip
      clip2 = TextClip(text, size=clip1.size).set_duration(4)
      
      # Make a composite video, takes a list of clips
      composition = CompositeVideoClip( [ clip1, clip2 ] )
      
      # Export the video
      composition.write_videofile("sunset_words.mp4")
    
    # sys.argv gives us the arguments from the terminal, in a list (first item is the script name)
    text = sys.argv[1]
    # call our function using the text from the terminal
    compose(text)
    


Now we have a tool to create these videos from the terminal. IT’S AMAZING.


## Adding more options

We want to be able to change the duration

- We’ll make our function take a duration parameter,
  - the start and end of the clip will get calculated based on that
- We’ll make the duration optional
  - by adding a default value on the parameter with *duration=4.0*
  - by checking the sys.argv parameter is actually there, avoid throwing an error if it’s not

boop

    # import VideoFileClip to load a video, TextClip to overlay text, and CompositeVideoClip to take two or more clips and overlay them as layers
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
    import sys
    import argparse
    
    # our function takes a text and duration. duration is optional and defaults to 4.0
    def compose(text, duration=4.0):
      # define when our video starts (one minute, 48 seconds = 60 + 48 = 108)
      start = 108
      # and calculate when it ends
      end = start + duration
      # Load the video, get a subclip that's just our calculated range
      # Then resize it to make it faster, resize takes a tuple
      clip1 = VideoFileClip("sunset.mp4").subclip(start, end).resize( (1920/2, 1080/2) )
      # Make a text clip, give it a duration
      # We'll also make it the size of the video clip
      clip2 = TextClip(text, size=clip1.size).set_duration(4)
      
      # Make a composite video, takes a list of clips
      composition = CompositeVideoClip( [ clip1, clip2 ] )
      
      # Export the video
      composition.write_videofile("sunset_words.mp4")
    
    # sys.argv gives us the arguments from the terminal, in a list (first item is the script name)
    text = sys.argv[1]
    # get the duration from the second parameter, if it's there, otherwise use a default
    if len(sys.argv) > 2:
      # it comes as a String, we need to turn it into a number with float()
      duration = float(sys.argv[2])
    else:
      duration = 3
    # call our function
    compose(text, duration)
    



## Tips
- Use the argparse module to simplify parsing sys.argv
  - https://docs.python.org/3/library/argparse.html


## Another script that sends the video

We’ll make a script that sends you the video in an email (?)

in the terminal:

    pip3 install emails

python email.py:

    import emails
    
    # Create our message object 
    message = emails.html(
      html="Hello friend!", 
      subject="Specter blah blah", 
      mail_from=("Scrap Ism", "scrapism.sfpc@gmail.com")
    )
    # Attach the file
    # Read the video file in binary form (using rb mode)
    message.attach(data=open("sunset_words.mp4", "rb"), filename="sunset_words.mp4")
    
    # Send the email
    message.send(
      to=("Sam", "splavigne@gmail.com"), 
      # A bunch of email server stuff from google
      smtp={
        "host": "smtp.gmail.com",
        "port": 465,
        "ssl": True,
        # You'd use an actual email login info (maybe not your own)
        "user": "scrapism.sfpc@gmail.com",
        "password": "scrapismscrapism"
      }
    )

SO COOL


## Making the script import the other script 

Using **import vidbot** we can import the functions from the other script 🤯 

- “vidbot” is whatever name of the other script, without .py

When importing another script, everything in the lowest indentation level will be executed. To avoid this we run the code only if the script is run directly through the terminal.
we add this hacky python thing to it

    if __name__ == "__main__":
      # our code

So our resulting videobot.py:

    
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
    import sys
    import argparse
    
    def compose(text, duration=4.0):
      start = 108
      end = start + duration
      clip1 = VideoFileClip("sunset.mp4").subclip(start, end).resize( (1920/2, 1080/2) )
      clip2 = TextClip(text, size=clip1.size).set_duration(4)
      composition = CompositeVideoClip( [ clip1, clip2 ] )
      composition.write_videofile("sunset_words.mp4")
    
    if __name__ == "__main__":
      text = sys.argv[1]
      if len(sys.argv) > 2:
        duration = float(sys.argv[2])
      else:
        duration = 3
      compose(text, duration)
      


and in our **email.py** we call the vidbot compose function, by adding

    
    import vidbot
    
    # ...
    
    vidbot.compose("cool emailz", 1)
    


We’ll also turn the video into a gif before sending it

    
    import subprocess
    
    subprocess.call(["ffmpeg", "-i", "sunset_words.mp4", "sunset_words.gif"])
    


And we’ll take the message from:

- Corpora https://github.com/dariusk/corpora

resulting email.py

    import emails
    import vidbot
    import subprocess
    
    isms = [
      "abstract expressionism",
      "academic",
      "action painting",
      "aestheticism",
      "art deco",
      "art nouveau",
      # ...
    ]
    
    # Create our message object 
    message = emails.html(
      html="Hello friend!", 
      subject="Specter blah blah", 
      mail_from=("Scrap Ism", "scrapism.sfpc@gmail.com")
    )
    # Turn into a gif
    subprocess.call(["ffmpeg", "-i", "sunset_words.mp4", "sunset_words.gif"])
    # Attach the file
    # Read the video file in binary form (using rb mode)
    message.attach(data=open("sunset_words.gif", "rb"), filename="sunset_words.gif")
    
    # Send the email
    message.send(
      to=("Sam", "splavigne@gmail.com"), 
      # A bunch of email server stuff from google
      smtp={
        "host": "smtp.gmail.com",
        "port": 465,
        "ssl": True,
        # You'd use an actual email login info (maybe not your own)
        "user": "scrapism.sfpc@gmail.com",
        "password": "scrapismscrapism"
      }
    )




## Making a twitter bot

Now you have to apply to post to twitter
https://developer.twitter.com/en/apply-for-access


- install a python library to interface with twitter
- make an application with twitter dev
- get a set of keys
  - consumer key
  - consumer secret key
  - access token

boop

    from twython import Twython
    import vidbot
    
    # parameters are APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
    twitter = Twython("dslfgjlskdfgjdflsgjdslfgsdffjldisfdf","dslfgjlskdfgjdflsgjdslfgsdffjldisfdf","dslfgjlskdfgjdflsgjdslfgsdffjldisfdf","dslfgjlskdfgjdflsgjdslfgsdffjldisfdf",)
    
    vidbot.compose("A spectre blah blah", 1)
    video = open("sunset_words.mp4", "rb")
    response = twitter.upload_video(media=video, media_type="video/mp4")
    twitter.update_status(media_ids=[response["media_id"]])
    


## See also:
- instagram picture of plunger
  - https://www.instagram.com/samepicofplunger/
- Post to tumblr using their API
- instagram api for python unofficial
  - https://github.com/LevPasha/Instagram-API-python


# Turn a python script into a website!


## Running a server

install flask, make webservers with it
http://flask.pocoo.org/


    pip3 install flask

make webapp.py

boop

    from flask import Flask
    app = Flask(__name__)
    
    # In webservers
    # You set up routes, when the user goes to the this URL then show them this thing
    # using a 'decorator'
    # when user enters the base URL /, perform the function on the next line
    @app.route("/")
    def home():
      return "hello"
    
    # run the web server when we run the script and get the web server going
    if __name__ == "__main__":
      #run in debug mode to update the server when we change the script
      app.run(debug=True)

When running the script, a local web server will be created and you can open your browser to the address the script gives you (http://127.0.0.1:5555)

When you make a change to your script, you need to **stop and restart the server**
To make it easier, you can tell flask to restart the server every time there’s a change to the file by changing:

    app.run(debug=True)


## Getting data from the URL bar

We can get information about the request the user made in the url

- 127.0.0.1:5000/?text=lol

we get that with the flask request module

    # ...
    @app.route("/")
    def home():
      text = request.args.get("text")
      return "hello!! " + text
    # ...



## Compositing the video from the website

We need to

- call the compose function of vidbot
  - but we need to make the output file name unique, since there might be more than one user at the same time
- Show the user a preview of the file
  - using flask static server
  - showing the video in a <video> tag

First we’ll add an output file option to vidbot.py on the compose() function

Making a unique filename

- use the time, in seconds and milliseconds, rare but possible for people to do it at the same time but unlikely so good enough

boop

    import vidbot
    from flask import Flask
    import time
    
    app = Flask(__name__)
    
    # In webservers
    # You set up routes, when the user goes to the this URL then show them this thing
    # using a 'decorator'
    # when user enters the base URL /, perform the function on the next line
    @app.route("/")
    def home():
      # get the text parameter from the URL. First parameter is the id, second is what to return if it's not there
      text = request.args.get("text", "")
      # Get a unique timestamp 
      ts = str(time.time())
      # Get the output video file name
      outname = "static/" + ts + ".mp4"
      if text:
              # Create the output video
              vidbot.compose(text, 1, outname)
              # Show an html tag with the video in it
              return '<video autoplay loop src=' + outname + '>,</video>'
      else:
              # If there's no text in the URL, prompt the user
              return "Type text into the url"
    
    # run the web server when we run the script and get the web server going
    if __name__ == "__main__":
            #run in debug mode to update the server when we change the script
            app.run(debug=True)
            



## See also
- Deploy a website using flask
  - Heroku
    - https://duckduckgo.com/?q=heroku+flask+app&atb=v125-5__&ia=qa
    - doesn’t host static files
  - DigitalOcean
    - https://www.digitalocean.com/
    - more complicated to set it up


Proper way to  have modules

- Make different environments to keep the right modules for your project
- using virtualenv
- on the terminal:
  - virtualenv [folder to store the modules] -p [version of python]

    virtualenv env -p python3
    source env/bin/activate # set the shell to use this environment
    
now when you use pip install, the packages get installed to that environment
    pip freeze #shows what packages are installed for this environment



# CLASS DONE WE MADE IT

