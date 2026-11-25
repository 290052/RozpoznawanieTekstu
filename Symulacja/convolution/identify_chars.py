import numpy as np
from PIL import Image, ImageDraw

def identify_chars(image, results, filters):
  identified_all = Image.fromarray(image)
  identified = {}
  identified_chars = []

  for key, result in results.items():
    max_position = np.unravel_index(
      np.argmax(result),
      result.shape
    )

    identified[key] = Image.fromarray(image)

    draw = ImageDraw.Draw(identified[key])
    draw_all = ImageDraw.Draw(identified_all)

    #positions = np.where(result >= result[max_position])
    positions = np.where(result >= result[max_position] * .997)
    #positions = np.where(result >= result[max_position] * .989)

    for position in range(len(positions[0])):
      if result[max_position] > 0.9:
        y = positions[0][position]
        x = positions[1][position]

        identified_chars.append({"char": key, "x": x, "y": y, "score": result[y][x]})

        draw.rectangle([
            x,
            y,
            x + filters[key].shape[1],
            y + filters[key].shape[0]
          ],
          outline="white",
          width=1
        )

        draw_all.rectangle([
            x,
            y,
            x + filters[key].shape[1],
            y + filters[key].shape[0]
          ],
          outline="white",
          width=1
        )

  return identified, identified_all, identified_chars