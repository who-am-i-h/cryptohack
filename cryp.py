import cv2 as cv

img1 = cv.imread("im.png")
img2 = cv.imread("im1.png")

xor_img = cv.bitwise_xor(img1,img2)

cv.imshow("hekll", xor_img)
cv.waitKey(0)
cv.destroyAllWindows