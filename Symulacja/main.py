import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

from textgen import generate_image
from simpoisson import add_poisson_noise
from genchars import generate_filters
from fit_chars import fit_chars
from identify_chars import identify_chars
from recreate_text import recreate_text

# Parametry obrazu
width = 800
height = 300

# Tekst do narysowania na obrazie
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus massa neque, maximus at felis et, elementum cursus nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis ultricies eu enim tincidunt feugiat. Aliquam tincidunt congue lacus, sed."
#text = "Ala ma kota, kot ma alę, są ze sobą szczęśliwi. As to pies ali."

# Generowanie obrazu
image = generate_image(width, height, text)

# Wyświetlenie obrazu
plt.figure(figsize=(12, 5))
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Obraz wejściowy")
plt.axis("off")
plt.show()

# Symulacja szumu poissona
#image = add_poisson_noise(image, 4)

# Wyświetlenie obrazu
#plt.figure(figsize=(12, 5))
#plt.imshow(image, cmap="gray", vmin=0, vmax=255)
#plt.title("Obraz z szumem Poissona")
#plt.axis("off")
#plt.show()

# Generowanie wzorców liter
filters = generate_filters()

# Generowanie macierzy prezentujących wyniki splotu/korelacji ("convolution" - splot, "corelation" - korelacja)
results = fit_chars(image, filters, "corelation")

# Wyświetlanie przykładowej macierzy wyników splotu/korelacj
plt.figure(figsize=(12, 5))
plt.imshow(results["m"], cmap="gray", vmin=-495, vmax=495)
plt.title("Macierz wyników splotu/korelacji dla litery m")
plt.axis("off")
plt.show()

identified, identified_all, identified_chars = identify_chars(image, results, filters)

# Wszystkie wykryte litery
plt.figure(figsize=(12, 5))
plt.imshow(identified_all, cmap="gray", vmin=0, vmax=255)
plt.title("Wszystkie wykryte litery")
plt.axis("off")
plt.show()

# Wyświetlanie wykrytych liter m
plt.figure(figsize=(12, 5))
plt.imshow(identified["m"], cmap="gray", vmin=0, vmax=255)
plt.title("Wykryte litery m")
plt.axis("off")
plt.show()

text = recreate_text(identified_chars)

print(text)