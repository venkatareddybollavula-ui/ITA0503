import cv2
import numpy as np

image = cv2.imread(r"C:\Users\bolla\Downloads\tree_image.jpg")

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)

    output = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat Output", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
