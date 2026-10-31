import cv2

image = cv2.imread(r"C:\Users\bolla\Downloads\tree_image.jpg")

if image is None:
    print("Image not found")
else:
    roi = image[50:200, 50:200]
    output = image.copy()

    h, w = roi.shape[:2]
    output[0:h, 0:w] = roi

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped and Pasted Image", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
