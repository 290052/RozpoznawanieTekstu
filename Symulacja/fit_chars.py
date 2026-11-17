import numpy as np

def fit_chars(image, filters, method):
  # Zbiór macierzy wynikowych splotu/korelacji przypisany do każdego znaku
  results = {}
  # Pętla iterująca po wszystkich filtrach
  for key, f in filters.items():
    # Normalizacja filtru do wartości od -1 do 1
    filter = f / 127.5 - 1

    # Jeżeli wykonywana jest operacja splotu, filtr jest obracany
    if method == "convolution":    
      filter = np.flip(f.astype(float) / 127.5 - 1, axis=(0, 1))


    # Pusta macież do której zostanie wpisany wynik splotu lub korelacji dla każdego piksela
    result = np.zeros((
      len(image) - len(filter) + 1,
      len(image[0]) - len(filter[0]) + 1
    ))

    for y in range(0, len(image) - len(filter) + 1):
      for x in range(0, len(image[0]) - len(filter[0]) + 1):
        # Fragment oryginalnego obrazu o wimiarach filtru zaczynający się od każdego piksela
        fragment = image[y:y + len(filter), x:x + len(filter[0])].astype(float) / 127.5 - 1

        # Spolt/korelacja wybranego fragmentu obrazu z filtrem
        result[y, x] = np.sum(fragment * filter)

    results[key] = result

  return results