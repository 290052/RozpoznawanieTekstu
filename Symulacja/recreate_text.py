def sort_by_x(char):
  return char["x"]

def sort_by_y(char):
  return char["y"]

def split_into_lines(identified_chars):
  lines = []

  identified_chars.sort(key = sort_by_y)

  last_y = 0

  line = []

  for char in identified_chars:
    if char["y"] > last_y:
      lines.append(line)
      line = []
      last_y = char["y"]

    line.append(char)

  lines.append(line)

  return lines

def remove_duplicates(line):
  for i in range(len(line) - 1):
    if abs(line[i]["x"] - line[i + 1]["x"]) <= 3:
      if line[i]["score"] > line[i + 1]["score"]:
        line.pop(i + 1)
      else:
        line.pop(i)

def recreate_text(identified_chars):
  text = ""

  lines = split_into_lines(identified_chars)

  for line in lines:
    line.sort(key = sort_by_x)

    remove_duplicates(line)

    for char in line:
      text += char["char"]

    text += "\n"

  return text
