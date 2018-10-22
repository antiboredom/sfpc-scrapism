# 10/16 - Photos 📸

# 📒 Agenda
- image manipulation 
  - getting images
  - photo manipulation
    - Image Magick
    - TLDR
    - Subprocess
    - [Pillow](https://pillow.readthedocs.io/en/5.3.x/) 🛌 😴
- video manipulation (if we have time!)
# 🤔 Who did homework?!?!
- Ilona has a WIP: who is coming out day for?
  - [AI weirdness](http://aiweirdness.com/), training neural networks with a sense of humor
- Tim made a lyric 🎶 generator using TextBlob
  - Kanye & Ayn Rand 🙃 
# 🖼️ How do we get images off a website?
- [Shutterstock](https://www.shutterstock.com/), [Pexels](https://www.pexels.com/), good image resources 
- Check whether website still loads by toggling javascript on/off
  - If it does, it should be easy to scrape
- When searching, make sure you select only Photos
![](https://d2mxuefqeaa7sj.cloudfront.net/s_760AA603A36DCE03DC9C80E71E2F81C1E2EDCAAED6138F202B76C43EC5789514_1539700121631_image.png)


**Use Requests_Html library to help scrape**
Gets all images. Generalizable to any website, but will pull all images. 

    from requests_html import HTMLSession
    #requests is library requests_html is based off, use to download image
    import requests
    #subprocesses are how python can call other command line tools 
    import subprocess
    url = 'https://www.shutterstock.com/search?searchterm=existential+despair&search_source=base_search_form&language=en&page=1&sort=popular&image_type=all&measurement=px&safe=true'
    
    # searches through all the html tags and grabs specified tags
    session = HTMLSession()
    r = session.get(url)
    
    # Gets all images on the page
    images = r.html.find('img'')
    for img in images:
      print(img)

To get image source

    for img in images:
      src = img.attrs.get('src') # Gets image source
      title = img.attrs.get('alt') # Gets image title

Get title of each image using the split command

    # Gets end of url for img name
    imgname = src.split('/')[-1]
    imgdata = requests.get(src).content
    
    #wb is the command for 'write binary'
    open(imgname, 'wb').write(imgdata)


# Basic photo manipulation in command line
## [IMAGE MAGICK](https://www.imagemagick.org/script/index.php) 🧙 🧙‍♂️ ✨ 

F*or command line photo manipulation!*

Run this command in terminal

    brew install imagemagick

Examples of Image Magick Functionality: Creating GIF, converting file types, resize, etc. 

    #Rename and convert file type
    convert <filename.abc> <newfilename.xyz>
    
    #Whoa! Maintains the aspect ratio 😱
    convert <filename.abc> -resize 1000x1000 <bigfilename.abc>
    
    #Rotate!
    convert <filename.abc> -rotate 90 <rotated.abc>
    
    #Invert photo
    convert <filename.abc> -negate 90 <negative.abc>
    
    #You can combine them 🤝
    convert <filename.abc> -negate -rotate 90 <combined.abc>
    
    #Creating GIF from a folder of images
    convert images/*.jpg -delay 0 animation.gif
    
    #Montage tiles images into a grid 
    montage images/*.jpg montage.jpg

👉 All the Image Magick command line options [**here**](https://imagemagick.org/script/command-line-options.php)❗


## [TLDR](https://tldr.sh/)

Finds common terminal commands with keywords 

    brew install tldr
    tldr <command line tool>


## [Subprocess](https://docs.python.org/2/library/subprocess.html)

Allows you to use command line

    import subprocess
    
    # Same as: say hi
    subprocess.call(["say", "hi"])
    
    # Same as: say -r 300 "a specter is haunting this python script
    # No need to double quote things!
    subprocess.call(["say", "-r", "300", "a specter is haunting this python script"])

**Subprocess example #1:** Says title of each image

    for img in images:
      src = img.attrs.get('src') # Gets image source
      title = img.attrs.get('alt') # Gets image title
      subprocess.call(["say", title]

**Subprocess example #2:** Downloads each file and converts it to negative

    subprocess.call(["convert", imgname, "-negate", imgname + ".neg.jpg"])

**Subprocess example #3:** Takes all images in folder and makes an animated gif

    subprocess.call(["convert", "*.jpg", "-delay", "0", "animation.gif"])


## [Pillow](https://pillow.readthedocs.io/en/5.3.x/)

**Install using pip**

    pip3 install pillow

**Basic example**

    from PIL import Image, ImageFilter
    #If image & file are in separate folders, provide file path
    img = Image.open("<filename.jpg>")
    
    #Resizing images
    #Thumbnail respects original aspect ratio, takes a new size as a tuple (width, height). It also doesn't make things bigger than they already are. Changes original image.
    img.thumbnail((100, 100))
    img.save("<small_filename.jpg>")
    
    #Resize doesn't respect original aspect ratio. Does not change original image.
    img = img.resize((1000, 1000))
    
    #Rotates image
    img = img.rotate(45)
    
    #Apply a  filter
    img = img.filter(ImageFilter.BLUR)

**Image draw**

    from PIL import Image, ImageFilter, ImageDraw
    img = Image.open("<filename.jpg>")
    
    #Draws on image!
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "HELLO!")
    draw.ellipse((0, 0, 500, 500), fill=(255, 255, 255))

**Collaging images together**

    from PIL import Image, ImageFilter, ImageDraw
    #glob syntax allows you to use /* to easily refer to all items at a path
    from glob import glob
    import random
    
    #a list of all the file names
    files = glob("images/*.jpg")
    
    #Takes three parameters: kind of image, width & height
    canvas = Image.new("RGB", (1000, 1000))
    
    #Loop through all files and stick them on image
    for filename in files:
      img = Image.open(filename)
      
      #generates random location
      x = random.randint(-100, 1000)
      y = random.randint(-100, 1000)
      
      #takes an image pastes it on something else
      canvas.paste(img, (x, y))
    
    canvas.save("collage.jpg")
    

**Get rid of labels**
*Crops image*

    img = img.crop(0, 0, img.size[0], img.size[1]-20)

To use transparency, use the RGBA colorspace. Can’t combine images in Pillow that don’t have the same colorspace

    canvas = Image.new("RGBA", (1000, 1000))
    img = img.convert("RGBA")
    canvas.save("collage.png")


## [Open CV and Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

Installation

    pip3 install opencv-python

**What is a Haar Cascade?**
Computer is looking for patterns. When we tell open CV, we can tell it to grab anything: a face, an eyeball, a smile, etc. [**Download XML file**](https://github.com/opencv/opencv/tree/master/data/haarcascades) ****depending on what you want to detect.

1 - Eyes

2 - Eyeglasses

3 - Front of face

4 - Profile

5 - Full body

6 - Left eye

7 - Right eye

8 - Lower body


    import cv2
    import numpy as np
    
    cascade = cv2.CascadeClassifier("eye.xml")
    
    #makes video object, looks for video camera on 💻
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, 1280)
    video_capture.set(4, 720)
    
    #creates an infinite loop 
    while True:
      ret, frame = video_capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      #becomes a list of coordinates with eyeballs
      eyeballs = cascade.detectMultiScale(gray)
      
      for (x,y,w,h) in eyeballs:
        #draws rectangle onto image
        #(image, coords, color, stroke width
        #to grab part of the frame 
        eye_img = frame[y:y+h, w:x+w]
        #to keep each frame an increasing number
        outname = "eye_" + str(index) + ".jpg" 
        cv2.imwrite(eye_img, outname)
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,0),2)
      
      #makes window on computer
      cv2.imshow("Video", frame)
      
      #looking for an exit key
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
    #Should stream the video
    VideoCapture.release()
    cv2.destroyAllWindows()

Instead of using a live video, you can read an image in.

    from glob import glob
    
    files = glob('images/*.jpg')
    for filename in files:
      frame = cv2.imread(filename)
      
      #everything else same as above!

detectMultiScale has a few options ([list of params](https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html))

    #eyeballs have to be at least 100, 100
    cascade.detectMultiScale(gray, minSize=(100,100)
# Libraries & Add-Ons

[Open CV and Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

  - Open CV is easiest to implement

[Dark Flow Library](https://github.com/thtrieu/darkflow) chaan find people and other objects  (like apples, oranges, etc) 
[Image2Text](https://github.com/tensorflow/models/tree/master/research/im2txt) 

