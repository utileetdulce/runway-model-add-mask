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
    def run_on_input(self, im):

        # image = np.array(im)
        # print(type(image))
        # print(image.dtype)
        # print(image.shape)
        # b,g,r,a = cv2.split(image)
        # print(a.shape)
        # alpha = cv2.merge((a,a,a,a))
        print("shape: {}, mode: {}, info:{}".format(im.size, im.mode, im.info))

        image = np.array(im.getdata(), np.uint8).reshape(im.size[1], im.size[0], 4)
        # arr = array(img)
        
        # Read the foreground image with alpha channel
        foreGroundImage = cv2.imread("test.png", -1)
        foreGroundImage2 = cv2.cvtColor( image, cv2.COLOR_RGBA2BGRA)
        print("foreGroundImage[...]")
        print(foreGroundImage[...])
        print("foreGroundImage2[...]")
        print(foreGroundImage2[...])

        print("shape: {}, type: {}".format(foreGroundImage.shape, foreGroundImage.dtype))
        print("shape: {}, type: {}".format(foreGroundImage2.shape, foreGroundImage2.dtype))


        # Split png foreground image
        b,g,r,a = cv2.split(foreGroundImage2)

        # Save the foregroung RGB content into a single object
        foreground = cv2.merge((b,g,r))

        # Save the alpha information into a single Mat
        alpha = cv2.merge((a,a,a))

        # Read background image
        background = cv2.imread("backGround.jpg")

        # Convert uint8 to float
        foreground = foreground.astype(float)
        background = background.astype(float)
        alpha = alpha.astype(float)/255

        # Perform alpha blending
        foreground = cv2.multiply(alpha, foreground)
        background = cv2.multiply(1.0 - alpha, background)
        outImage = cv2.add(foreground, background)


        return outImage
        # return image[:,:,3]
