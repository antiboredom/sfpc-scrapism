
# Get random segments from a video and make a new video from all those subclips

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
final_clip.write_videofile("random_dance.mp4")

# use this to write a video file with audio that mac understands
#final_clip.write_videofile(“random_dance.mp4”, codec="libx264", temp_audiofile="something.m4a", remove_temp=True, audio_codec="aac")
