import os
import sys
import cv2
import numpy as np

def add_text_to_image(image_size=(400, 500), text="opencv Rocks!", output_path="35.jpg"):
    """
    Exercise 35: Write a Python function to create a text string entered by the user
    that must appear on the given image using OpenCV.
    """
    height, width = image_size
    # Create white canvas
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_thickness = 2
    text_color = (0, 0, 255) # Red color

    # Calculate centered position using getTextSize
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    # Draw text
    cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

    # Save output
    cv2.imwrite(output_path, image)
    print(f"Image with text '{text}' saved to '{output_path}'.")

    # Display image
    if os.environ.get("HEADLESS", "0") != "1":
        cv2.imshow("Image with Text", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    if os.environ.get("HEADLESS", "0") == "1" or not sys.stdin.isatty():
        user_width, user_height, user_text = 500, 400, "opencv Rocks!"
    else:
        try:
            w_in = input("Enter image width [default 500]: ").strip()
            h_in = input("Enter image height [default 400]: ").strip()
            t_in = input("Enter the text to display [default 'opencv Rocks!']: ").strip()
            user_width = int(w_in) if w_in else 500
            user_height = int(h_in) if h_in else 400
            user_text = t_in if t_in else "opencv Rocks!"
        except (EOFError, ValueError):
            user_width, user_height, user_text = 500, 400, "opencv Rocks!"
    add_text_to_image((user_height, user_width), user_text)
