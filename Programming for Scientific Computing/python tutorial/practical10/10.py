# Generating frames from video

# Importing all necessary libraries
import cv2
import os
import numpy as np
import glob

# Reading the video from specified path
traffic_video = cv2.VideoCapture("./video/traffic2.mp4")

# Setting current frame to zero
current_frame = 0

while (True):
	
	# Reading from frame
	ret, frame = traffic_video.read()
	
	if  ret:
		# If video is still left continue creating images
		name = 'frame_'+ str(current_frame) + '.jpg'
		print("Creating",name,"...")
		
		# Writing the extracted images
		cv2.imwrite('./generated_frames/' + name, frame)
		
		current_frame += 1
	else:
		break
	
# Realeasing all  space and windows once done
traffic_video.release()
cv2.destroyAllWindows()