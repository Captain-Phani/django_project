import cv2
import numpy as np
img=cv2.imread("C:/Users/Phani/Pictures/Saved Pictures/wallpaperflare.com_wallpaper.jpg")
# cv2.imshow('img',img)

rows,cols,_= img.shape
print("Rows",rows)
print("Cols",cols)

#img cut
# cut_img=img[540:1081,0:960]
# cv2.imshow("img cut",cut_img)

#Region of interest(ROI)-to crop the portion of image in particular shape
cv2.rectangle(img,(700,200),(1200,713),(0,255,0),3)
roi=img[200:713,700:1200]

cv2.imshow('img',roi)
cv2.waitKey(0)