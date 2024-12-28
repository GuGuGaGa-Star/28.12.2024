import PIL
from PIL import Image
from PIL import ImageFilter

with Image.open("нг мем.jpg") as image_original:
    #image_original.show()

    image_gray = image_original.convert("L")
    image_gray.save("нг_мем_gray.jpg")
    #image_gray.show()

    image_blur = image_original.filter(ImageFilter.BLUR)
    image_blur.save("нг_мем_blur.jpg")

    image_rotate = image_original.transpose(Image.ROTATE_180)
    image_rotate.save("нг_мем_rotate.jpg")
