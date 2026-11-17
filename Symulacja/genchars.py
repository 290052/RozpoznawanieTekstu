import numpy as np
from PIL import Image, ImageDraw, ImageFont

def generate_filters():
  # Określenie czcionki i jej rozmiaru
  font = ImageFont.truetype("JetBrainsMonoNerdFont-Regular.ttf", 24)
  ascent, descent = font.getmetrics()
  

  # Lista znaków dla których zostanie wygenerowany wzorzec
  characters = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"
  characters += "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
  #characters += "0123456789"
  #characters += ".,/?;:!`~@#$%^&*()'"
  #characters += '"'
  #characters += "\\"
  #characters += " "

  # Tablica gotowych wzorców
  chars = {}

  for char in characters:
    # Wyznaczenie szerokości znaku
    width = int(font.getlength(char)) + 1

    # Stworzenie nowego obrazu
    image = Image.new("L", (width, ascent + descent), color=0)
    draw = ImageDraw.Draw(image)

    # Rysowanie na obrazie jednego znaku
    draw.multiline_text((0, 0), char, fill=255, font=font)

    # Dodwanie obrazu jednego znaku w słowniku
    chars[char] = np.array(image)

  return chars