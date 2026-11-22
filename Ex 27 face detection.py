import cv2

path = r"C:\Users\dhars\Desktop\Watch.jpg"

img = cv2.imread(path)

print(img is None)

if img is not None:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
