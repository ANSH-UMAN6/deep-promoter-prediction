import random

def shuffle_sequence(seq):
    seq = list(seq)
    random.shuffle(seq)
    return "".join(seq)


def generate_negative_samples(promoters):
    negatives = []
    for i, seq in enumerate(promoters):
        negatives.append({
            "id": f"neg_{i}",
            "sequence": shuffle_sequence(seq)
        })
    return negatives