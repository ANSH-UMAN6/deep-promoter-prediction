import numpy as np

mapping = {
"A":[1,0,0,0],
"C":[0,1,0,0],
"G":[0,0,1,0],
"T":[0,0,0,1],
"N":[0,0,0,0]
}

def fix_length(seq, max_len=200):

    if len(seq) > max_len:
        return seq[:max_len]

    return seq + "N"*(max_len-len(seq))

def encode_sequence(seq):

    encoded = [mapping.get(base,[0,0,0,0]) for base in seq]

    return np.array(encoded)