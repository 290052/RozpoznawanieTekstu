from PIL import ImageFont, Image, ImageChops
import numpy as np

from genchars import generate_filters
from simpoisson import add_poisson_noise

#sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24]
sizes = [24]

font_names = [
  "JetBrainsMonoNerdFont-Regular.ttf",
  #"AdwaitaSans-Regular.ttf",
  #"LiberationSerif-Regular.ttf",
  #"GrapeNuts-Regular.ttf",
  #"FreeMono.otf",
  #"LiberationMono-Regular.ttf",
  #"NimbusMonoPS-Bold.otf",
  #"FiraSans-Regular.ttf",
  #"Cantarell-VF.otf",
  #"AdwaitaMono-Regular.ttf"
]

#lambdas = [1, 4, 16, 256]
lambdas = [16]

def shift_image(image, dx, dy):
  img = Image.fromarray(image)
  shifted = ImageChops.offset(img, dx, dy)

  result = np.array(shifted)

  if dx > 0:
    result[:, :dx] = 0
  elif dx < 0:
    result[:, dx:] = 0

  if dy > 0:
    result[:dy, :] = 0
  elif dy < 0:
    result[dy:, :] = 0

  return result

def gen_font_list():
  fonts = []
  for name in font_names:
      for size in sizes:
        fonts.append(ImageFont.truetype(name, size))

  return fonts

def generate_dataset():
  fonts = gen_font_list()
  dataset = []

  for font in fonts:
    dataset.append(generate_filters(font, 15, 33))

  return dataset

def prepare_dataset():
  data = generate_dataset()

  char_to_label = {
    char: i for i, char in enumerate(data[0].keys())
  }

  dataset = []

  for fontdata in data:
    for char, image in fontdata.items():
      for lam in lambdas:
        for x in range(-2, 3):
          for y in range(-3, 4):
            dataset.append({
              "label": char_to_label[char],
              "char": char,
              "image": shift_image(add_poisson_noise(image, lam), x, y)
            })

  return dataset