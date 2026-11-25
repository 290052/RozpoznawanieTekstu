def calc_accuracy(recreated_text, original_text):
  correct = sum(a == b for a, b in zip(recreated_text, original_text))

  return int(correct / len(original_text) * 100)