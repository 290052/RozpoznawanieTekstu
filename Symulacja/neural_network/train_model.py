import torch

def train_model(model, x, y):
  loss_function = torch.nn.CrossEntropyLoss()
  optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

  for i in range(100001):
    optimizer.zero_grad()

    prediction = model(x)
    loss = loss_function(prediction, y)

    if i % 1000 == 0:
      print("Epoka: ", i)
      print("Błąd: ", loss.item())

      torch.save({
      "model": model.state_dict(),
      "optimizer": optimizer.state_dict(),
      "epoch": i
      }, "Symulacja/neural_network/checkpoint.pth")

    loss.backward()
    optimizer.step()

  prediction = model(x)
  predicted_classes = torch.argmax(prediction, dim=1)

  print("Przewidywane klasy: ", predicted_classes)
  print("Prawdziwe klasy: ", y)

  torch.save(model.state_dict(), "Symulacja/neural_network/model.pth")