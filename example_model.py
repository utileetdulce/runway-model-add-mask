import random
from PIL import Image
import numpy as np
from numpy import array
import cv2

class ExampleModel():

    def __init__(self, options):
        random.seed(options['seed'])
        self.truncation = options['truncation']

    # Generate an image based on some text.
    def run_on_input(self, image, mask):

        # Split png foreground image
        b,g,r,a = cv2.split( array(mask))

        # Save the foregroung RGB content into a single object
        foreground = cv2.merge((b,g,r))

        # Save the alpha information into a single Mat
        alpha = cv2.merge((a,a,a))

        # Read background image
        background = array(image)

        # Convert uint8 to float
        foreground = foreground.astype(float)
        background = background.astype(float)
        alpha = alpha.astype(float)/255

        # Perform alpha blending
        foreground = cv2.multiply(alpha, foreground)
        background = cv2.multiply(1.0 - alpha, background)
        outImage = cv2.add(foreground, background)

        return outImage
