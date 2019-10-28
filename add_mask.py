import random
from PIL import Image

class Add_mask():

    # Generate an image based on some text.
    def run_on_input(self, image, mask):

        # Resize foreground to background
        (width, height) = (image.width, image.height)
        mask = mask.resize((width, height))

        # Appyle mask to image
        alpha_mask = mask.getchannel("A")
        image.putalpha(alpha_mask)
        return image
