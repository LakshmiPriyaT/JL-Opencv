import cv2
import numpy as np

# Load the image
image = cv2.imread("Lesson7/red.png")
# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the red color (in HSV)
lower_red = np.array([100, 40, 40])
upper_red = np.array([100, 255, 255])

# Create a mask that isolates the red color in the image
mask = cv2.inRange(hsv, lower_red, upper_red)

# Apply some morphological operations to clean up the mask (optional)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

# Use the mask to extract the red regions from the original image
red_masked_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image and the red-masked image
cv2.imshow("Original Image", image)
cv2.imshow("Red Masked Image", red_masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()