
# Import VideoFileClip to load a video, 
# TextClip to overlay text, and 
# CompositeVideoClip to take two or more clips and overlay them as layers
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import sys
import argparse

# our function takes a text and duration. duration is optional and defaults to 4.0
def compose(text, duration=4.0, outname="sunset_words.mp4"):
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
  composition.write_videofile(outname)

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
