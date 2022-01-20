# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:44:54 2022

@author: nicis
"""

import cv2
import sys
import numpy 
import template_matching as tm
import Image_alignment as im

PREVIEW  = 0   # Preview Mode
MATCH = 1
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = 'Camera'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

picture=[]

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    
    frame = cv2.flip(frame,1)
    if image_filter == PREVIEW:
        result = frame
    elif image_filter == MATCH:
        result = tm.match(frame)
 

    cv2.imshow(win_name, result)
    picture.append(frame)
    
    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('P') or key == ord('p'):
        image_filter = PREVIEW
    elif key == ord('M') or key == ord('m'):
        image_filter = MATCH
source.release()
cv2.destroyWindow(win_name)

'''
for i in range(len(picture)):
    picture[i]=cv2.cvtColor(picture[i],cv2.COLOR_BGR2RGB)
cv2.imshow("Boss",picture[3])
cv2.waitKey(0)
cv2.destroyAllWindows()

'''