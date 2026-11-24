import torch
import numpy as np
import os

from neural_network.gen_dataset import prepare_dataset
from neural_network.train_model import train_model

training_dataset = prepare_dataset()

label_to_char = {
  sample["label"]: sample["char"]
  for sample in training_dataset
}

training_x = torch.from_numpy(
  np.stack([sample["image"] for sample in training_dataset])
).float()

training_x = training_x.flatten(start_dim=1)

training_x = training_x / 255.0

training_y = torch.tensor([
  sample["label"] for sample in training_dataset
], dtype=torch.long)

model = torch.nn.Sequential(
  torch.nn.Linear(495, 128),
  torch.nn.ReLU(),
  torch.nn.Linear(128, 64),
  torch.nn.ReLU(),
  torch.nn.Linear(64, 101)
)

if os.path.exists("Symulacja/neural_network/model.pth"):
  model.load_state_dict(torch.load("Symulacja/neural_network/model.pth", weights_only=True))
elif os.path.exists("Symulacja/neural_network/checkpoint.pth"):
  model.load_state_dict(torch.load("Symulacja/neural_network/checkpoint.pth", weights_only=True))
else:
  train_model(model, training_x, training_y)

#train_model(model, training_x, training_y)

def check_char(char_img):
  x = torch.from_numpy(char_img).float()

  x = x / 255.0
  x = x.flatten().unsqueeze(0)

  pred = model(x)

  label = torch.argmax(pred, dim=1).item()
  char = label_to_char[label]

  return char