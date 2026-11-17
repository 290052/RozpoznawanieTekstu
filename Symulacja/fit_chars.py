import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def fit_chars(image, filters, method):
  # Zbiór macierzy wynikowych splotu/korelacji przypisany do każdego znaku
  results = {}

  # Normalizacja obrazu do wartości od -1 do 1
  image = image / 127.5 - 1

  # Pętla iterująca po wszystkich filtrach
  for key, f in filters.items():
    # Normalizacja filtru do wartości od -1 do 1
    filter = f / 127.5 - 1

    # Jeżeli wykonywana jest operacja splotu, filtr jest obracany
    if method == "convolution":    
      filter = np.flip(filter, axis=(0, 1))

    # Pusta macież do której zostanie wpisany wynik splotu lub korelacji dla każdego piksela
    result = np.zeros((
      len(image) - len(filter) + 1,
      len(image[0]) - len(filter[0]) + 1
    ))

    # Określenie wielkości filtra
    f_height, f_width = filter.shape

    # Wygenerowanie wszystkich możliwych fragmentów obrazu o wielkości filtra
    fragments = sliding_window_view(image, (f_height, f_width))

    # Wykonanie splotu/korelacji każdego fragmentu obrazu z filtrem
    results[key] = np.einsum("ijkl,kl->ij", fragments, filter)

  return results