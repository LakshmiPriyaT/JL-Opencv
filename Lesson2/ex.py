import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two example images
image1 = np.zeros((300, 300, 3), dtype=np.uint8)  # Black image
image2 = np.ones((300, 300, 3), dtype=np.uint8) * 255  # White image

# Perform pixel-wise subtraction
sub = cv2.subtract(image1, image2)
add = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# Display the original images and the subtraction result
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title('Addition result')

plt.show()



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two example colorful images
image1 = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)  # Random colors
image2 = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)  # Random colors

# Perform pixel-wise subtraction
sub = cv2.subtract(image1, image2)
add = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# Display the original images and the subtraction result
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title('Addition result')

plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two simple colorful images
image1 = np.zeros((300, 300, 3), dtype=np.uint8)
image1[:, :150, :] = [0, 255, 0]  # Green region on the left

image2 = np.zeros((300, 300, 3), dtype=np.uint8)
image2[:, 150:, :] = [0, 0, 255]  # Red region on the right

# Perform pixel-wise subtraction
sub = cv2.subtract(image1, image2)
add = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# Display the original images and the subtraction result
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title('Addition result')

plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two images with red on both sides
image1 = np.zeros((300, 300, 3), dtype=np.uint8)
image1[:, :150, :] = [0, 0, 255]  # Red on the left

image2 = np.zeros((300, 300, 3), dtype=np.uint8)
image2[:, 150:, :] = [0, 0, 255]  # Red on the right

# Perform pixel-wise subtraction
sub = cv2.subtract(image1, image2)
add = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# Display the original images and the subtraction result
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title('Addition result')

plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two images with three different colors
image1 = np.zeros((300, 300, 3), dtype=np.uint8)
image1[:, :100, :] = [0, 0, 255]  # Red on the left
image1[:, 100:200, :] = [0, 255, 0]  # Green in the middle
image1[:, 200:, :] = [255, 0, 0]  # Blue on the right

image2 = np.zeros((300, 300, 3), dtype=np.uint8)
image2[:, :100, :] = [255, 0, 0]  # Blue on the left
image2[:, 100:200, :] = [0, 255, 0]  # Green in the middle
image2[:, 200:, :] = [0, 0, 255]  # Red on the right

# Perform pixel-wise subtraction
sub = cv2.subtract(image2, image1)
add = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# Display the original images and the subtraction result
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtraction Result')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB))
plt.title('Addition result')

plt.show()

