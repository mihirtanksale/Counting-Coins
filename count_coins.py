import cv2
import numpy as np

img=cv2.imread("coins.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
#Apply Guassian blur

blurred=cv2.GaussianBlur(gray,(11,11),0)
cv2.imshow("Blurred",blurred)
#Apply canny edge detection
edged= cv2.Canny(blurred,30,150)
cv2.imshow("Edge",edged)
#Find countors

cnts,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Draw green color around contours
coins=img.copy()
cv2.drawContours(coins,cnts,-1,(0,255,0),2)

#display count

print ("I count {} coins in this image".format(len(cnts)))

cv2.imshow("Contours",coins)
cv2.waitKey()
cv2.destroyAllWindows()
