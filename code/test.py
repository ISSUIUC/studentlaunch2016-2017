from main import *
from SimpleCV import *
import time
from datetime import datetime, timedelta

test_rect = 0
test_tolerances = 0
test_pic_time_1080 = 0
test_pic_time_max = 0
test_blob_colors = 1
test_color_matching = 0

# Show rectangles in pic
if(test_rect):
	#cam = SimpleCV.Camera()
	#img = capture_image(cam)
	img = Image("test_images/test11.png")
	rects = find_rects(img, 0.4)
	for rect in rects:
		rect.drawOutline((128,0,0),-1,4)
	img.show()
	time.sleep(3)
	
#Saves 100 versions of test file showing various tolerances of blobs rect
if(test_tolerances):
	i = 0
	while(i<100):
		img = Image("test_images/test11.png")
		rects = find_rects(img, float(i)/100)
		for rect in rects:
			rect.drawOutline((128,0,0),-1,4)
		save_image(img)
		i += 1
		
#Logs time to take and save a 1920x1080 pic
if(test_pic_time_1080):
	width = 1920
	height = 1080
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("\n1920x1080\n")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print t
		write_log(t)
		i += 1
		
#Logs time to take and save a 3280x2464 pic
if(test_pic_time_max):
	width = 3280
	height = 2464
	cam = SimpleCV.Camera(prop_set={'width':width, 'height':height})
	i = 0
	write_log("\n3280x2464\n")
	while(i<100):
		t1 = datetime.now()
		img = capture_image(cam)
		save_image(img)
		t2 = datetime.now()
		dt = t2 - t1
		t = str(dt.seconds*1000000 + dt.microseconds)
		print i
		print t
		write_log(t)
		i += 1

#Prints the colors of blobs in a pic
if(test_blob_colors):
	img = Image("test_images/test11.png")
	rects = find_rects(img)
	for rect in rects:
		print rect.meanColor()

#Tests if blobs color near target		
if(test_color_matching):
	print "testing"
