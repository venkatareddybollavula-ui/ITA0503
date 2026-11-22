import os
import sys
import cv2
import numpy as np

def create_circle_image(image_size=(400, 500), output_path="34.jpg"):
    """
    Exercise 34: Write a Python function to create a white image size entered by the user
    and then create a shape of Circle using OpenCV.
    """
    height, width = image_size
    # Create white canvas
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define circle properties
    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    # Draw circle (color: Red (0, 0, 255), thickness: 2)
    cv2.circle(image, center, radius, (0, 0, 255), 2)

    # Save output
    cv2.imwrite(output_path, image)
    print(f"Circle image ({width}x{height}, radius={radius}) saved to '{output_path}'.")

    # Display image
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Circle Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    if os.environ.get("HEADLESS", "0") == "1" or not sys.stdin.isatty():
        user_width, user_height = 500, 400
    else:
        try:
            w_in = input("Enter image width [default 500]: ").strip()
            h_in = input("Enter image height [default 400]: ").strip()
            user_width = int(w_in) if w_in else 500
            user_height = int(h_in) if h_in else 400
        except (EOFError, ValueError):
            user_width, user_height = 500, 400
    create_circle_image((user_height, user_width))
