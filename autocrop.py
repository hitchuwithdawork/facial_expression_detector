from PIL import Image
from autocrop import Cropper

cropper = Cropper()

# Get a Numpy array of the cropped image
cropped_array = cropper.crop('portrait.png')

# Save the cropped image with PIL if a face was detected:
if cropped_array:
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save('cropped.png')