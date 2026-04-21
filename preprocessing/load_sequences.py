from Bio import SeqIO

def load_sequences(filepath):

    sequences = []

    for record in SeqIO.parse(filepath, "fasta"):
        sequences.append(str(record.seq).upper())

    return sequences