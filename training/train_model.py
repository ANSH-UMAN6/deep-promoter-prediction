import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from training.evaluate_model import evaluate
from models.cnn_model import MotifCNN
from preprocessing.encode_sequences import encode_sequence, fix_length


# =========================
# LOAD DATASET
# =========================

sequences = []
labels = []

with open("dataset.txt") as f:
    for line in f:
        seq, label = line.strip().split(",")
        sequences.append(seq)
        labels.append(int(label))


# =========================
# ENCODE
# =========================

X = [encode_sequence(fix_length(seq)) for seq in sequences]
y = labels

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y   # 🔥 CRITICAL
)

class SequenceDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x = torch.tensor(self.X[idx]).permute(1,0).float()
        y = torch.tensor(self.y[idx]).float()
        return x, y


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

train_loader = DataLoader(SequenceDataset(X_train, y_train), batch_size=32, shuffle=True)


# =========================
# MODEL
# =========================

model = MotifCNN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.BCEWithLogitsLoss()


# =========================
# TRAIN
# =========================

losses = []

for epoch in range(10):
    total_loss = 0

    for x, y in train_loader:
        optimizer.zero_grad()

        pred = model(x)
        loss = loss_fn(pred.view(-1), y.view(-1))

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    losses.append(total_loss)

    print(f"Epoch {epoch}: Loss = {total_loss:.4f}")
    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(losses)
    plt.title("Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.savefig("static/loss_curve.png")
    plt.close()

    for x, y in train_loader:
        optimizer.zero_grad()

        pred = model(x)

        loss = loss_fn(pred.view(-1), y.view(-1))

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch}: Loss = {total_loss:.4f}")

    test_loader = DataLoader(SequenceDataset(X_test, y_test), batch_size=32)
    evaluate(model, test_loader)

torch.save(model.state_dict(), "motif_model.pth")

print("Total:", len(y))
print("Promoters:", sum(y))
print("Non-promoters:", len(y) - sum(y))