
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

# make a video that is a composite of all the subclips
final_clip = mp.CompositeVideoClip(clips)

# write it to a file
final_clip.write_videofile("random_dance.mp4")
# use this to write a video file with audio that mac understands
#final_clip.write_videofile(“random_dance.mp4”, codec="libx264", temp_audiofile="something.m4a", remove_temp=True, audio_codec="aac")
