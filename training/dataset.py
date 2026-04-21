import torch
from torch.utils.data import Dataset

class SequenceDataset(Dataset):

    def __init__(self, sequences, labels):

        self.sequences = sequences
        self.labels = labels

    def __len__(self):

        return len(self.sequences)

    def __getitem__(self, idx):

        x = torch.tensor(self.sequences[idx]).float()
        y = torch.tensor(self.labels[idx]).float()

        x = x.permute(1,0)

        return x,y