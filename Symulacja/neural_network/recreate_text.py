from neural_network.neural_network import check_char

def sort_by_x(char):
  return char["x"]

def sort_by_y(char):
  return char["y"]

def split_into_lines(identified_chars):
  lines = []

  last_y = 0

  line = []

  for char in identified_chars:
    if abs(char["y"] - last_y) > 30:
      if line:
        lines.append(line)
      
      line = []
      last_y = char["y"]

    line.append(char)

  lines.append(line)

  return lines

def recreate_text_nn(identified_chars):
  text = ""

  lines = split_into_lines(identified_chars)

  for line in lines:
    line.sort(key = sort_by_x)

    last_char = {}

    for char in line:
      if last_char:
        if abs(last_char["x"] - char["x"]) > 20:
          text += " "

      text += check_char(char["image"])

      last_char = char

    text += " "

  return text