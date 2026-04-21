import torch
import torch.nn as nn
import torch.nn.functional as F


class MotifCNN(nn.Module):
    def __init__(self):
        super(MotifCNN, self).__init__()

        self.conv1 = nn.Conv1d(4, 32, kernel_size=10)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5)

        self.pool = nn.MaxPool1d(2)

        self._to_linear = None
        self._get_conv_output()

        self.fc1 = nn.Linear(self._to_linear, 64)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(64, 1)

    def _get_conv_output(self):
        x = torch.randn(1, 4, 200)
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        self._to_linear = x.view(1, -1).shape[1]

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        x = x.view(x.size(0), -1)

        x = F.relu(self.fc1(x))
        x = self.dropout(x)

        return self.fc2(x)  