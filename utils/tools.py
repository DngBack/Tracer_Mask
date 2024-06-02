import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2


def base64_to_pil(im_b64):
    im_bytes = base64.b64decode(im_b64)   # im_bytes is a binary image
    im_file = BytesIO(im_bytes)  # convert image to file-like object
    img = Image.open(im_file)   # img is now PIL Image object
    return img

def pil_to_base64(img):
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    im_b64 = base64.b64encode(im_bytes)
    return im_b64


def image_to_base64(image):
    img_to_byte = cv2.imencode('.jpg', image)[1].tobytes()
    byte_to_base64 = base64.b64encode(img_to_byte)
    return byte_to_base64.decode('ascii')  # chuyển về string


def base64_to_image(base64_string):
    base64_to_byte = base64.b64decode(base64_string)
    byte_to_image = np.frombuffer(base64_to_byte, np.uint8)
    image = cv2.imdecode(byte_to_image, cv2.IMREAD_COLOR)
    return image