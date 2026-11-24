import numpy as np
from PIL import Image, ImageDraw

def generate_filters(font, width=0, height=0):
  # Określenie rozmiaru czcionki
  if height == 0:
    ascent, descent = font.getmetrics()
    height = ascent + descent

  if width == 0:
    calc_width = True
  else:
    calc_width = False
  

  # Lista znaków dla których zostanie wygenerowany wzorzec
  characters = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"
  characters += "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
  characters += "0123456789"
  characters += ".,/?;:!`~@#$%^&*()'"
  characters += '"'
  characters += "\\"

  # Tablica gotowych wzorców
  chars = {}

  for char in characters:
    # Wyznaczenie szerokości znaku
    if calc_width:
      width = int(font.getlength(char)) + 1

    # Stworzenie nowego obrazu
    image = Image.new("L", (width, height), color=0)
    draw = ImageDraw.Draw(image)

    

    # Rysowanie na obrazie jednego znaku
    draw.multiline_text((0, 0), char, fill=255, font=font)

    # Dodwanie obrazu jednego znaku w słowniku
    chars[char] = np.array(image)

  return chars