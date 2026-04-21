from preprocessing.load_sequences import load_sequences
from preprocessing.encode_sequences import encode_sequence, fix_length


def prepare_dataset():

    promoters = load_sequences("data/promoters.fasta")
    non_promoters = load_sequences("data/non_promoters.fasta")

    labels = [1] * len(promoters) + [0] * len(non_promoters)

    sequences = promoters + non_promoters

    encoded = []

    for seq in sequences:

        seq = fix_length(seq)

        encoded.append(encode_sequence(seq))

    return encoded, labels