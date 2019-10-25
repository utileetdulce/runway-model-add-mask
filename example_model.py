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

        image.putalpha(mask)

        return image
