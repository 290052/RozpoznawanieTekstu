from PIL import Image
import numpy as np

def resize_char(char_img):
  if char_img.dtype == bool:
    char_img = char_img.astype(np.uint8) * 255

  height, width = char_img.shape

  #scale = min(15 / width, 33 / height)

  #new_width = max(1, round(width * scale))
  #new_height = max(1, round(height * scale))

  # resized = Image.fromarray(char_img).resize(
  #   (new_width, new_height),
  #   Image.Resampling.LANCZOS
  # )

  # resized = np.array(resized)

  result = np.zeros((33, 15), dtype=int)

  #x = (15 - new_width) // 2
  #y = (33 - new_height) // 2
  x = (15 - width) // 2
  y = (33 - height) // 2

  #result[y:y + new_height, x:x + new_width] = resized
  result[y:y + height, x:x + width] = char_img

  return result

def resize_chars(characters):
  resized_chars = []

  for i in range(len(characters)):
    resized_chars.append({
      "image": resize_char(characters[i]["image"]),
      "x": characters[i]["x"],
      "y": characters[i]["y"]
    })

  return resized_chars