
# Combine two videos using moviepy

# import the editor library but call it mp to make it shorter
import moviepy.editor as mp
# another way is to only import the functions we need, a bit faster
# from moviepy.editor import VideoFileClip, concatenate_videoclips

# Join videos together
clip1 = mp.VideoFileClip("fan_upside_down.mp4")
clip2 = mp.VideoFileClip("prancercise.mp4")
# get a segment
clip2 = clip2.subclip(10, 13.5)

# the function takes a list of video objects
final_clip = mp.concatenate_videoclips([clip1, clip2])
# output the video to a file
final_clip.write_videofile("output.mp4")
