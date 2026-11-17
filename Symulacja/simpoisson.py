import numpy as np

def add_poisson_noise(image, lam):
  image = image / 255

  for y, row in enumerate(image):
    for x, pixel in enumerate(row):
      photons = pixel * lam
      image[y, x] = np.random.poisson(photons)

  return np.clip(image / lam * 255, 0, 255)