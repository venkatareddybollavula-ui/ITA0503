import os
import cv2
import numpy as np

def subtract_foreground(image_path="image.jpg", lower_color=[0, 70, 50], upper_color=[15, 255, 255], output_path="37.jpg"):
    """
    Exercise 37: Write a Python function to subtract the foreground of the given input image
    based on color levels using OpenCV.
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'")
        return

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper range for foreground color (red rose petals)
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask to detect foreground objects
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert mask so foreground is removed and only background is retained
    mask_inv = cv2.bitwise_not(mask)

    # Extract the background
    background = cv2.bitwise_and(image, image, mask=mask_inv)

    # Save output
    cv2.imwrite(output_path, background)
    print(f"Foreground-subtracted (only background) image saved to '{output_path}'.")

    # Display results
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Original Image", image)
        cv2.imshow("Foreground Subtracted Image (Only Background)", background)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    subtract_foreground()
