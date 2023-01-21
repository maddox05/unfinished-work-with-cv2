import cv2
import numpy as np

height = 258
width = 258
A = np.zeros((height,width,3), np.uint8)

B = np.zeros((height,width,3), np.uint8)
B[1:width//1,:,:] = (0,255,0)

errorL2 = cv2.norm( A, B, cv2.NORM_L2 )
similarity = 1 - errorL2 / ( height * width )
print('Similarity = ',similarity)
