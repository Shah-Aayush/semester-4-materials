# Generating video from frames

import cv2
import numpy as np
import glob

img_array = []

# Reading all jpg files
for filename in glob.glob('./generated_frames/*.jpg'):
	img = cv2.imread(filename)
	height, width, layers = img.shape
	size = (width,height)
	img_array.append(img)
	
# Encoding Techniques, No ofFrames
out = cv2.VideoWriter('./generated_video/project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

for frame in range(len(img_array)):
	out.write(img_array[frame])
	
print("Generated video is saved in \'./generated_video/project.mp4\'.")
out.release()