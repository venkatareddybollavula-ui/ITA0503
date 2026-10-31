import cv2

image_path = r"C:\Users\bolla\Downloads\tree_image.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Image not found")
else:
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
