import cv2
import numpy as np

def hough_circles_image(file_path):
    # Read in image
    img = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, 130, 150)

    cv2.imwrite("sobel.jpg", edges)

hough_circles_image("coins.jpg")