# 10/23 Video


https://www.youtube.com/watch?v=KgbSjRMqyjc&


Today

- download video
- manipulate them
- python library called numPy, lets you edit video in python


# Example scripts from this class

https://github.com/antiboredom/sfpc-scrapism/tree/master/class-notes/examples/video




# Getting material with Youtube-dl

scraping web for video is difficult, so we use **youtube-dl** to download videos from the terminal
https://youtube-dl.org/
Documentation:
https://github.com/rg3/youtube-dl/blob/master/README.md#output-template-examples

To install, in terminal:

    $ brew install youtube-dl

It’s a web scraper just for video. For every website they reversed engineered how to get a video file


## To use it
    $ youtube-dl [URL]



## See the possible formats with -F
    $ youtube-dl [URL] -F
    # outputs the format available for that file, and resolutions
    
    # you can choose a specific format to download, with -f and the code for that format
    $ youtube-dl [UDL] -f 22


- Some formats let you download only the video, or only the audio



## Download every single video from a youtube user

Paste the URL from the **youtube channel**
Get every TED talk:

    
    $ youtube-dl https://www.youtube.com/user/TEDtalksDirector 
    

Also works for, e.g. playlists
https://www.youtube.com/user/TEDtalksDirector/playlists



## Decide what the output name it’ll be with -o
    
    $ youtube-dl [URL] -o [FILENAME]
    



## Try and always save with a specific format (like mp4)
    
    $ youtube-dl [URL] --merge-output-format mp4
    



## Download subtitles
- add “,cc” to your search, to only get videos with closed captions

     --write-auto-sub
     --skip-download Download only subtitles and not the video
    
    $ youtube-dl [URL] --write-auto-sub --skip-download
    


- check sam’s tool for parsing subtitle files
## Get the URLS of the video and audio
    
    # --get-url
    $ youtube-dl [URL] --get-url
    



## Tips
- Avoid URLs with “&”
  - Make sure the URL for youtube is just https://www.youtube.com/watch?v=[ID]
- limit max downloads with --max-downloads to save space
- call the program from python with subprocess.call(…)
- Use it for more sites:
  - full list: https://rg3.github.io/youtube-dl/supportedsites.html
  - 









# VLC video player

Use VLC to play every video format imaginable
https://www.videolan.org/vlc/





# Use ffmpeg to convert formats / edit video

https://ffmpeg.org/
Documentation: https://ffmpeg.org/ffmpeg.html (insane and confusing, just google stuff)

Usage:

    
    # ffmpeg -i \[Some kind of input\] [parameters (optional)] [Some kind of output]
    
    # convert my mp4 video to mov format
    $ ffmpeg -i mycatvideo.mp4 mycatvideo.mov
    


## Turn things into animated GIFs
    
    $ ffmpeg -i kitten.mp4 kitten.gif
    
    # use -r 3 . to set it to 3 frames a second
    $ ffmpeg -i kitten.mp4 -r 3 kitten.gif
    



## Output frames to images


    
    # 1. set the output format to an image format (eg jpg)
    # 2. put %d in the output name, it'll be replaced by the frame number
    
    $ ffmpeg -i kitten.mp4 kitten_frame_%d.jpg
    


## Turn a bunch of images into a video
    # 1. set the INPUT format to the image format (eg jpg)
    # 2. put %d in the INPUT name, it'll be replaced by the frame number, make sure those files exist
    
    $ ffmpeg -i kitten_frame_%d.jpg kitten.mp4
    


## Cut/trim video (e.g. get rid of the intro)
    
    # BEFORE the input, use -ss [timestamp]
    # AFTER the input, use -t [length in seconds]
    
    # start at 10 seconds, and go for 10 seconds
    $ ffmpeg -s 00:00:10 -i kitten.mp4 -t 10 output.mp4
    


## Get info about a video with ffprobe
    
    $ ffprobe kitten.video
    # outputs a bunch of info, like duration, bitrate, etc.
    


## Combine all this
    
    # Start at 10 seconds, get a 10 seconds video, turn into a GIF
    $ ffmpeg -s 00:00:10 -i kitten.mp4 -t 10 output.gif
    


## Use ffmpeg to download a video URL you got from youtube-dl (!!!)
    
    # Get only the URL
    $ youtube-dl --get-url [YOUTUBE LINK]
    
    # copy that URL to ffmpeg, get only 5 seconds of it
    $ ffmpeg -i "[THE URL WE GOT]" -t 5 short_fan.mp4
    


## Stupid filters

https://ffmpeg.org/ffmpeg-filters.html

**vflip - flip the video vertically**

    
    $ ffmpeg -i in.mp4 -vf "vflip" out.mp4
    

**edgedetect**

- Add parameters to the filter after the -vf, in quotes
  - [option]=[value], separated with **:**
    
    $ ffmpeg -i in.mp4 -vf "edgedetect=low=0.1:high=0.4" out.mp4
    



## Change the speed of the video

The command is stupid

- PTS = Presentation Time Stamp, the time stamp eg. 00:10:00
- you tell it to make the PTS, e.g. twice what it is, therefore it slows down
- to make it faster you multiply the PTS by a decimal number, e.g. twice as fast = 0.5
- ugh just google it
    
    # slow it down, twice the length
    $ ffmpeg -i short_fan.mp4 -vf "setpt=2*PTS" slow_short_fan.mp4
    
    # speed it up, twice as fast
    $ ffmpeg -i short_fan.mp4 -vf "setpt=0.5*PTS" fast_short_fan.mp4
    

**Interpolation**

- When slowing down you can use motion-interpolate to create the frames in between, to make smoother slow-mo videos
  - https://cloudacm.com/?p=3055



## Use the camera
    
    $ ffmpeg -f avfoundation -pixel_format yuyv422 -framerate 30 -video_size 1280x720 -i 0:0 recording.mp4
    

Keeps recording until we hit Ctrl+C

**use -t to only record 5 seconds**

    
    $ ffmpeg -t 5 -f avfoundation -pixel_format yuyv422 -framerate 30 -video_size 1280x720 -i 0:0 recording.mp4
    



## Tips
- abort a long operation with Cmd+C
- when stuck, search for specific uses, eg. “ffmpeg make optimized gif”
- delete all files in a folder with terminal (if we downloaded too many files)
  - rm *.jpg
- use youtube-dl on a livestream to capture it




# Using MoviePy

We’ll use MoviePy for video editing
https://zulko.github.io/moviepy/
Documentation: https://zulko.github.io/moviepy/ref/ref.html


WIP library from Sam
https://antiboredom.github.io/vidpy/

Install

    
    $ pip3 install moviepy
    



## Put two videos together

**By concatenating**

    
    # import the editor library but call it mp to make it shorter
    import moviepy.editor as mp
    # another way is to only import the functions we need, a bit faster
    # from moviepy.editor import VideoFileClip, concatenate_videoclips
    
    # Join videos together
    clipl = mp.VideoFileClip("fan_upside_down.mp4")
    clip2 = mp.VideoFileClip("prancercise.mp4")
    
    # the function takes a list of video objects
    final_clip = mp.concatenate_videoclips([clip1, clip2])
    # output the video to a file
    final_clip.write_videofile("output.mp4")
    

**By compositing videos together (like layers in photoshop/premiere)**


## Get only a segment of a video clip, with subclip()
    # from 10 seconds to 13.5 seconds
    clip1 = mp.VideoFileClip("prancercise.mp4").subclip(10, 13.5)
    
    # also works like this
    clip1 = mp.VideoFileClip("prancercise.mp4")
    tiny_clip = clip1.subclip(10, 13.5)
    


## Resize a video file
- if the videos are of different sizes, the output might be broken, so we resize them
    
    clip1 = clip1.resize((1280, 720))
    




## Get random subclips from a video and combine them together


    import random
    import moviepy.editor as mp
    
    video = mp.VideoFileClip("dance.mp4")
    
    # get the duration of the video, in seconds
    video_duration = video.duration
    # define the duration of the subclips we're gonna take
    clip_duration = 0.5
    # make a list we'll populate with subclips
    clips = []
    
    for i in range(0,10): # do this 10 times
      # get a random start point
      # make it so the end can never be past the full video duration
      start = random.uniform(0, video_duration - clip_duration)
      # the end point is whatever start time plus the subclip duration
      end = start + clip_duration
      # add a subclip to the list, between our start and end points
      clips.append(video.subclip(start,end))
    
    # create the final video out of all the clips
    final_clip = mp.concatenate_videoclips(clips)
    # write it to a file
    final_clip.write_video("random_dance.mp4")



## Play a bunch of clips overlayed on top of each other, for reasons

It’s like what we just did but instead of concatenate_videoclips:

    
    # use CompositeVideoClip to make a video that's all the clips layered together
    final_clip = mp.CompositeVideoClip(clips)
    



    
    import random
    import moviepy.editor as mp
    
    video = mp.VideoFileClip("dance.mp4")
    
    # get the duration of the video, in seconds
    video_duration = video.duration
    # define the duration of the subclips we're gonna take
    clip_duration = 1.5
    # make a list we'll populate with subclips
    clips = []
    
    for i in range(0,10): # do this 10 times
      # get a random start point
      # make it so the end can never be past the full video duration
      start = random.uniform(0, video_duration - clip_duration)
      # the end point is whatever start time plus the subclip duration
      end = start + clip_duration
    
      # store the subclip so we can do things to it
      clip = video.subclip(start,end)
    
      # set the position of the clip in our canvas
      clip = clip.set_position((random.randint(-100, 800), random.randint(-100, 400)))
      # set the start time, to whatever position we're in (i) by half, just for fun
      clip = clip.set_start( i / 2.0 )
      # add to the list
      clips.append(clip)
    
    # make a video that is a composite of all the subclip
    final_clip = mp.CompositeVideoClip(clips)
    
    # write it to a file
    final_clip.write_videofile(“random_dance.mp4”, codec="libx264", temp_audiofile="something.m4a", remove_temp=True, audio_codec="aac")
## Tips
- Functions on video clips don’t change the original clip, they return a new clip
  - so always do new_clip = clip1.resize((1280,720))
- To export with an audio codec that mac understands:
    
    write_videofile(“random_dance.mp4”, codec="libx264", temp_audiofile="something.m4a", remove_temp=True, audio_codec="aac")
    




# Videogrep

Videogrep is a command line tool that searches through dialog in video files and makes supercuts based on what it finds.

https://antiboredom.github.io/videogrep/


- Needs a video file with a subtitle or transcription file associated with it, with the same name
  - most youtube videos have them
  - we can use youtube-dl to get them



## Download a video, then use videogrep to get all the instances of a word and make a supercut
    
    # get the version 18 that's a smaller video, and download subtitles
    $ youtube-dl "[URL]" -f 18 --write-auto-sub
    
    # if our subtitles are in .vtt format, we add --use-vtt
    $ videogrep -i [name_of_the_video_file] --use-vtt --search "Korea"
    


## Get only individual words
    
    # use --search-type word
    $ videogrep -i [name_of_the_video_file] --use-vtt --search "Korea" --search-type word
    


## Set the output file
    
    # use -o output_name.mp4
    


## Add padding
    
    # add 300 ms of space between words
    # --padding 300
    


## Use regular expressions to search for multiple things
    
    # use the pipe character | to search for either text
    # search for "Korea" or any word with "nucl" in it
    # "Korea|nucl"
    $ videogrep -i [name_of_the_video_file] --use-vtt --search "Korea|nucl" --search-type word
    
    # the ^ character means the start of the word
    # ^a = all the words that begin with the letter a
    
    # the $ means the end of the word
    # ing$ = all the words that end with ing
    
    # 
    


## Export n-grams
    
    # -n 1
    # outputs the most used words
    
    # -n 2
    # outputs the most used couplings of words
    


## Use  sphinx to transcribe videos
    
    # install sphinx
    brew tap watsonbox/cmu-sphinx
    brew tap watsonbox/cmu-sphinx
    brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase
    brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxtrain # optional
    brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx
    
    # transcribe the video
    videogrep -i pompeo.mp4 --transcribe
    



# Next


- Upcoming workshop from hardware class TA
  - A servo motor + a camera + control it with python


## Homework
- explore these tools and make a python script that makes a new video every time you run it



