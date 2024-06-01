

# Open an image file
image_path = 'Lesson1/pika.png'
from PIL import Image
import numpy as np

# Open an image file
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Get the dimensions of the image
height, width = image_array.shape[:2]

# Check if the image is grayscale or RGB
if len(image_array.shape) == 3:
    channels = image_array.shape[2]
else:
    channels = 1  # Grayscale image

# Accessing pixel values
i, j = 100, 200
pixel_value = image_array[i, j]

# For RGB images, pixel_value is a tuple (R, G, B)
# For grayscale images, pixel_value is a single intensity value

print(f"Pixel value at position ({i}, {j}): {pixel_value}")

from PIL import Image
import numpy as np

# Create a simple 3x3 image
image_data = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[128, 128, 128], [64, 64, 64], [192, 192, 192]],
    [[255, 255, 255], [0, 0, 0], [128, 128, 128]]
], dtype=np.uint8)

# Create a PIL Image from the NumPy array
image = Image.fromarray(image_data)

# Get the dimensions of the image
height, width, channels = image_data.shape

# Accessing pixel values at a specific position (row, column)
row, column = 1, 1  # Example position

# For RGB images, pixel_value is a tuple (R, G, B)
# For grayscale images, pixel_value is a single intensity value
pixel_value = image_data[row, column]

# Display the image and the accessed pixel value
image.show()
print(f"Pixel value at position ({row}, {column}): {pixel_value}")
