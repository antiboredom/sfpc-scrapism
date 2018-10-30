
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
  	return '<video autoplay loop src=' + outname + '></video>'
  else:
  	# If there's no text in the URL, prompt the user
  	return "Type text into the url"

# run the web server when we run the script and get the web server going
if __name__ == "__main__":
	#run in debug mode to update the server when we change the script
	app.run(debug=True)
