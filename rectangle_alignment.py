import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the images (replace with your actual file paths)
image1 = cv2.imread('rectangle1.png', cv2.IMREAD_GRAYSCALE)
#image2 = cv2.imread('rectangle2.png', cv2.IMREAD_GRAYSCALE)

# Detect contours and calculate rotation angles
def calculate_rotation_angle(image):
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rect = cv2.minAreaRect(contours[0])
    angle = rect[-1]
    #print('angle',angle)
    if angle > 45:
        angle -= 90
    return angle

# Rotate images to align rectangles
angle1 = calculate_rotation_angle(image1)
#print('angle1',angle1)
#angle2 = calculate_rotation_angle(image2)

rotated_image1 = cv2.warpAffine(image1, cv2.getRotationMatrix2D((image1.shape[1] // 2, image1.shape[0] // 2), angle1, 1), image1.shape[::-1])
#rotated_image2 = cv2.warpAffine(image2, cv2.getRotationMatrix2D((image2.shape[1] // 2, image2.shape[0] // 2), angle2, 1), image2.shape[::-1])

# Display the aligned images
#cv2_imshow(rotated_image1)
cv2.imshow('Aligned Rectangle 2', rotated_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
