import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Funkcja zawijająca tekst na obrazie
def wrap_text(text, font, max_width, draw):
  words = text.split()  # Tablica słów z tekstu
  lines = []            # Wynikowe linie
  current_line = ""     # Badana linia

  # Pętla przechodzi przez wszystkie słowa w tekście
  for word in words:
    # Testowana linia - jeżeli linia jest jeszcze pusta to badamy tylko kolejne słowo, jeżeli coś w niej jest to obecną zawartość z dodatkiem kolejnego słowa
    test_line = current_line + " " + word if current_line else word

    # Obliczenie szerokości testowanej linii
    text_width = draw.textbbox(
      (0, 0),
      test_line,
      font=font
    )[2]

    if text_width <= max_width:
      # Jeżeli badana linia jest mniejsza niż maksymalna szerokość to dodajemy do badanej linii słowo
      current_line = test_line
    else:
      # W przeciwnym razie linia jest zapisywana do wynikowych linii, a słowo jest zapisywane do nowej linii
      lines.append(current_line)
      current_line = word

  # Dodanie do wynikowych linii ostatniej badanej linii jeżeli coś w niej się znajduje, a nie zapełniła się jeszcze
  if current_line:
    lines.append(current_line)

  # Zwrócenie połączonych wynikowych linii w jeden tekst za pomocą znaków nowej linii
  return "\n".join(lines)

def generate_image(width, height, text):
  # Tworzenie czarnego obrazu obrazu
  image = Image.new("L", (width, height), color=0)

  # Wczytanie czcionki
  font = ImageFont.truetype("JetBrainsMonoNerdFont-Regular.ttf", 24)

  # Umieszczenie tekstu na obrazie
  draw = ImageDraw.Draw(image)

  # Zawijanie tekstu
  text = wrap_text(text, font, width - 60, draw)

  # Rysowanie tekstu
  draw.multiline_text(
    (30, 30),
    text,
    fill=255,
    font=font,
    spacing=12
  )

  # Konwersja obrazu do macierzy NumPy
  return np.array(image)