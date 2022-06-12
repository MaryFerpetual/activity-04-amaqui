import cv2
filepath ="doog.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("",image)
cv2.waitKey(0)
cv2.destroyAllWindows()