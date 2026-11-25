import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFont

from textgen import generate_image
from simpoisson import add_poisson_noise
from genchars import generate_filters
from accuracy import calc_accuracy

from convolution.fit_chars import fit_chars
from convolution.identify_chars import identify_chars
from convolution.recreate_text import recreate_text

from neural_network.segmentation import segment_image, visualize_segments
from neural_network.normalize_segments import resize_chars
from neural_network.recreate_text import recreate_text_nn

# Metoda rozpoznawania tekstu (0 - splot/korelacja, 1 - sieć neuronowa)
method = 1

# Czcionka
font = ImageFont.truetype("JetBrainsMonoNerdFont-Regular.ttf", 24)

# Tekst do narysowania na obrazie
#text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus massa neque, maximus at felis et, elementum cursus nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis ultricies eu enim tincidunt feugiat. Aliquam tincidunt congue lacus, sed."
text = "Ala ma kota, kot ma alę, są ze sobą szczęśliwi. As to pies ali."

# Generowanie obrazu
image = generate_image(text, font)

# Wyświetlenie obrazu
plt.figure(figsize=(12, 5))
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Obraz wejściowy")
plt.axis("off")
plt.show()

# Symulacja szumu poissona
image = add_poisson_noise(image, 16)

# Wyświetlenie obrazu
plt.figure(figsize=(12, 5))
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Obraz z szumem Poissona")
plt.axis("off")
plt.show()

if method == 0:
  # Generowanie wzorców liter
  filters = generate_filters(font)

  # Generowanie macierzy prezentujących wyniki splotu/korelacji ("convolution" - splot, "corelation" - korelacja)
  #results = fit_chars(image, filters, "convolution")
  results = fit_chars(image, filters, "corelation")

  # Wyświetlanie przykładowej macierzy wyników splotu/korelacj
  plt.figure(figsize=(12, 5))
  plt.imshow(results["m"], cmap="gray", vmin=0, vmax=1)
  plt.title("Macierz wyników splotu/korelacji dla litery m")
  plt.axis("off")
  plt.show()

  identified, identified_all, identified_chars = identify_chars(image, results, filters)

  recreted_text = recreate_text(identified_chars)

  print("Odtworzony tekst:")
  print(recreted_text)

  accuracy = calc_accuracy(recreted_text, text)

  print("Skuteczność:", accuracy, "%")

  # Wszystkie wykryte litery
  plt.figure(figsize=(12, 5))
  plt.imshow(identified_all, cmap="gray", vmin=0, vmax=255)
  plt.title("Wszystkie wykryte litery")
  plt.axis("off")
  plt.show()

if method == 1:
  characters = segment_image(image)

  characters = resize_chars(characters)

  recreted_text = recreate_text_nn(characters)

  print("Odtworzony tekst:")
  print(recreted_text)

  accuracy = calc_accuracy(recreted_text, text)
  print("Skuteczność:", accuracy, "%")

  visualize_segments(image, characters)