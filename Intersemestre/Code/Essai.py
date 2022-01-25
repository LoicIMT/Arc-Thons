from cv2 import cv2 as cv
import numpy as np

imgcv_vierge = cv.imread('.\Image\Cible_vierge.JPG')
imgcv_fleche = cv.imread('.\Image\Cible_fleche.JPG')
imgcv_diff = cv.subtract(imgcv_vierge,imgcv_fleche)

cv.imshow('image',imgcv_diff)
cv.waitKey(0)
cv.destroyAllWindows()

#edges = cv.Canny(imgcv_diff, 50, 150)
#
#cv.imshow("edges",edges)
#cv.waitKey(0)
#cv.destroyAllWindows()
#
#lines = cv.HoughLinesP(edges,1,np.pi/180,40,minLineLength=30,maxLineGap=30)
#i = 0
#for x1,y1,x2,y2 in lines[0]:
#    i+=1
#    cv.line(imgcv_diff,(x1,y1),(x2,y2),(255,0,0),1)
#print(i)
#
#cv.imshow("res",imgcv_diff)
#cv.waitKey(0)
#cv.destroyAllWindows()



