# Image Library
from PIL import Image, ImageOps
import cv2

# TRACER 
from TRACER.inference.inference import Inference
from TRACER.config import getConfig, getConfig_Input

# Torch and Numpy 
import torch
import numpy as np

# Generate Library
import os
import requests
import json 
import requests
import base64
from io import BytesIO
from PIL import Image


#load module 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def convert_to_base64(image):
  """
  Chuyển đổi ảnh sang dạng base64

  Args:
    image_path: Đường dẫn đến ảnh

  Returns:
    Chuỗi base64 của ảnh
  """

  # Đọc ảnh
  # image = cv2.imread(image_path)

  # Mã hóa ảnh sang dạng base64
  _, buffer = cv2.imencode('.jpg', image)
  base64_string = base64.b64encode(buffer.tobytes()).decode("utf-8")

  return base64_string


def convert_mask_to_base64(image):
  """
  Chuyển đổi ảnh đen trắng sang dạng base64

  Args:
    image_path: Đường dẫn đến ảnh

  Returns:
    Chuỗi base64 của ảnh
  """

  # Đọc ảnh
  # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

  # Mã hóa ảnh sang dạng base64
  _, buffer = cv2.imencode('.jpg', image)
  base64_string = base64.b64encode(buffer.tobytes()).decode("utf-8")

  return base64_string


def decode_base64_to_np_array(base64_string):
    try:
        # Decode base64 to binary
        decoded_bytes = base64.b64decode(base64_string)
        
        # Convert binary data to a NumPy array
        image = Image.open(BytesIO(decoded_bytes))
        image_array = np.array(image)
        
        return image_array
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def get_image_from_url_base64(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            img = decode_base64_to_np_array(content)
            return img
        else:
            return None
    except Exception as e:
        return None


def rmbg(image):
    """
    Args:
        image (PIL Image): Image input for processing
    Output:
        image (PIL Image)
    """

    # Set Some Config Path
    img_url = "./TRACER/data/custom_dataset/Image.png"

    # Get image
    image.save(img_url)

    # Setting 
    arch = "7"
    exp_num = 0
    save_path = os.path.join(
        "results/", "custom_dataset/", f"TE{arch}_{str(exp_num)}"
    )

    # Get pre-mask
    mask_of_image, object_of_image = Inference(save_path).test()
    rgb_image = cv2.cvtColor(mask_of_image, cv2.COLOR_BGR2RGB)
    mask = Image.fromarray(rgb_image)
    return object_of_image

def getbg(image):
    """
    Args:
        image (PIL Image): Image input for processing
    Output:
        image (PIL Image)
    """

    # Set Some Config Path
    img_url = "./TRACER/data/custom_dataset/Image.png"

    # Get image
    image.save(img_url)

    # Setting 
    arch = "7"
    exp_num = 0
    save_path = os.path.join(
        "results/", "custom_dataset/", f"TE{arch}_{str(exp_num)}"
    )

    # Get pre-mask
    mask_of_image, object_of_image = Inference(save_path).test()
    rgb_image = cv2.cvtColor(mask_of_image, cv2.COLOR_BGR2RGB)
    mask = Image.fromarray(rgb_image)
    mask = Image.fromarray(rgb_image)
    thresh = 200
    fn = lambda x : 255 if x > thresh else 0
    mask = mask.convert('L').point(fn, mode='1')
    mask = ImageOps.invert(mask)
    return object_of_image, mask
