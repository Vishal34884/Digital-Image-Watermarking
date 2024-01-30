#Importing Libraries
import numpy as np
import cv2
#Reading Input Image
image = cv2.imread('images/nature.jpg')
(image_height,image_width) = image.shape[:2]
#Reading watermark
watermark = cv2.imread('images/water.jpg')
(watermark_height,watermark_width) =watermark.shape[:2]
#Overlay
overlay = np.zeros((image_height, image_width, 3),dtype='uint8')
overlay[0:watermark_height,0:watermark_width] = watermark
print(image.shape)
print(overlay.shape)
cv2.addWeighted(overlay, 0.1, image, 1.9, 0.0,image)
# Displaying Output
cv2.imshow("Overlay", overlay)
cv2.imshow("Image", image)

cv2.imshow("Watermark",watermark)
cv2.imwrite("WaterMarked.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()