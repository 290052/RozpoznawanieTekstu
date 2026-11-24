import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy import ndimage

def merge_dots(image, characters):
  merged = []
  used = set()

  for i, dot in enumerate(characters):
    if i in used:
      continue

    for j, char in enumerate(characters):
      if i == j or j in used:
        continue

      dot_center = dot["x"] + dot["width"] / 2
      char_center = char["x"] + char["width"] / 2

      horizontal_distance = abs(dot_center - char_center)
      vertical_distance = char["y"] - (dot["y"] + dot["height"])

      if (
        dot["width"] <= 7
        and dot["height"] <= 7
        and char["height"] <= 15
        and horizontal_distance <= 8
        and 0 <= vertical_distance <= 12
      ):
        x1 = min(dot["x"], char["x"])
        y1 = min(dot["y"], char["y"])

        x2 = max(
          dot["x"] + dot["width"],
          char["x"] + char["width"]
        )
        y2 = max(
          dot["y"] + dot["height"],
          char["y"] + char["height"]
        )

        merged_img = image[y1:y2, x1:x2]

        merged.append({
          "image": merged_img,
          "x": x1,
          "y": y1,
          "width": x2 - x1,
          "height": y2 - y1
        })

        used.add(i)
        used.add(j)
        break

    if i not in used:
      merged.append(dot)
      used.add(i)

  return merged

def segment_image(image):
  binary = image > 127

  structure = np.ones((3, 3), dtype=int)

  labeled = ndimage.label(binary, structure)[0]

  objects = ndimage.find_objects(labeled)

  characters = []

  for region in objects:
    y_slice, x_slice = region

    char_img = image[y_slice, x_slice]

    characters.append({
      "image": char_img,
      "x": x_slice.start,
      "y": y_slice.start,
      "width": char_img.shape[1],
      "height": char_img.shape[0]
    })

  return merge_dots(image, characters)

def visualize_segments(image, characters):
  fig, ax = plt.subplots()

  ax.imshow(image, cmap="gray")

  for char in characters:
    x = char["x"]
    y = char["y"]

    height, width = char["image"].shape

    rect = patches.Rectangle(
      (x, y),
      width,
      height,
      linewidth=1,
      edgecolor="red",
      facecolor="none"
    )

    ax.add_patch(rect)

  plt.show()