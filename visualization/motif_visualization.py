import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import matplotlib.pyplot as plt
from models.cnn_model import MotifCNN


# load model
model = MotifCNN()
model.load_state_dict(torch.load("motif_model.pth"))

print("Model loaded successfully")


# extract first convolution filters
filters = model.conv1.weight.data

print("Number of filters:", filters.shape[0])
print("Filter size:", filters.shape)


# visualize filters
for i in range(min(6, filters.shape[0])):

    plt.figure()

    plt.imshow(filters[i].cpu(), aspect="auto")

    plt.title(f"Motif Filter {i}")

    plt.xlabel("Position in motif")

    plt.ylabel("DNA base channel")

    plt.colorbar()

    plt.show()