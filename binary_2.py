# read the image file
img_1 = cv2.imread('C:\\Users\\tamim\\crackseg\\data\\train\\masks\\10000.jpg')
  
ret, bw_img = cv2.threshold(img_1, 0, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img_1, 120, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Binary", cv2.WINDOW_NORMAL)
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Save the image 
bw_img.dtype='uint8'
cv2.imwrite('10000.jpg', bw_img)
