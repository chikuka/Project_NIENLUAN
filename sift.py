# -*- coding: utf-8 -*-
"""SIFT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1An0P5IxFWHvOsZ0XBJodxUEuWo7UC_RI
"""

import cv2

# reading the image
img = cv2.imread('table.jpg')
# convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# create SIFT feature extractor
sift = cv2.xfeatures2d.SIFT_create()
# detect features from the image
keypoints, descriptors = sift.detectAndCompute(img, None)
# draw the detected key points
sift_image = cv2.drawKeypoints(gray, keypoints, img)
# show the image
cv2.imshow('image', sift_image)
# save the image
cv2.imwrite("table-sift.jpg", sift_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# read the images
img1 = cv2.imread('book.jpg')
img2 = cv2.imread('table.jpg')

# convert images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# create SIFT object
sift = cv2.xfeatures2d.SIFT_create()
# detect SIFT features in both images
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)
# create feature matcher
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
# match descriptors of both images
matches = bf.match(descriptors_1,descriptors_2)
# sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)
# draw first 50 matches
matched_img = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
# show the image
cv2.imshow('image', matched_img)
# save the image
cv2.imwrite("matched_images.jpg", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

!pip install pysift
import cv2
import pysift

image = cv2.imread('your_image.png', 0)
keypoints, descriptors = pysift.computeKeypointsAndDescriptors(image)