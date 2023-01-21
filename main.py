import numpy
import pyautogui
import imutils
import cv2
height = 200
width = 400
#image = pyautogui.screenshot()
#image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
#cv2.imwrite("in_memory_to_disk.png", image)

pyautogui.screenshot("normal_image.png")

image = cv2.imread("normal_image.png")
imutils.resize(image, width=1920, height=1080)
image = image[100:300, 1100:1500]
#image = image[136:150, 1151:1409]
cv2.imwrite("normal_image.png", image)


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = numpy.array([50, 100, 100])
upper = numpy.array([70, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
maskrgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
cv2.imwrite("cropped_mask.png", maskrgb)


green = cv2.imread("green.png")
images = numpy.array([image, maskrgb])
errorL2 = cv2.norm(images, cv2.NORM_L2)
similarity = 1 - errorL2 /( height * width )
print('Similarity = ',similarity)

cv2.imshow("Image", image)
cv2.imshow("Mask", maskrgb)
cv2.imshow("Green Always", green)

#cv2.imshow("Screenshot", imutils.resize(image))
if similarity <=.40:
    print("similar")
else:
    print("diff")
cv2.waitKey(0)


