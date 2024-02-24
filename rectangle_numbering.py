import cv2
import numpy as np

# Load the image (assuming you have preprocessed it to extract each rectangle and line)
image = cv2.imread('rectangles.png', cv2.IMREAD_COLOR)

# Define the coordinates of the rectangles
rectangles = [
    ((50, 50), (200, 150)),  # Rectangle 1
    ((250, 50), (400, 150)),  # Rectangle 2
    ((50, 200), (200, 300)),  # Rectangle 3
    ((250, 200), (400, 300))  # Rectangle 4
]


# Assign numbers to the rectangles
for i, ((x1, y1), (x2, y2)) in enumerate(rectangles, start=1):
    cv2.putText(image, str(i), (x2 , y2+70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# Display the image
cv2.imshow('Numbered Rectangles ',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
