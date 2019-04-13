"""
ECE196 Face Recognition Project
Author: Will Chen
Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
"""import numpy as np"""
import cv2

# TODO: Edit this function
def process_image():
	image = cv2.imread('geisel.jpg', 0)
	cv2.imwrite('geiselgray.jpg', image)
	half = cv2.resize(image, None, fx=0.5, fy=0.5)
	ghalf = cv2.imwrite('geiselhalf.jpg', half)
	dim=half.shape
	center= [dim[0]/2, dim[1]/2]
	print(dim)
	print(center)	
	box = cv2.rectangle(half,(((center[1])-50),(center[0])-50),(50+(center[1]),(50+(center[0]))),(255,255,255),5) 
	#box = cv2.rectangle(half,(67-5,),(5+(dim[1]),(5+(dim[0]))),(255,0,0),1)
	cv2.imwrite('gesielbox.jpg', box)
	return

# Just prints 'Hello World! to screen.
def hello_world():
	print('Hello World!')
	return

# TODO: Call process_image function.
def main():
	hello_world()
	process_image()
	return


if(__name__ == '__main__'):
	main()
