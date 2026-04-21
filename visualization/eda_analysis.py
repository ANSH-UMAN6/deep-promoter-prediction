import matplotlib.pyplot as plt
from collections import Counter
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocessing.load_sequences import load_sequences
from preprocessing.load_sequences import load_sequences

promoters = load_sequences("data/promoter.fasta")
non_promoters = load_sequences("data/non_promoter.fasta")

all_sequences = promoters + non_promoters

bases = []

for seq in all_sequences:
    bases.extend(list(seq))

count = Counter(bases)

plt.bar(count.keys(),count.values())
plt.title("Nucleotide Frequency")
plt.xlabel("Base")
plt.ylabel("Count")
plt.show()
def gc_content(seq):

    g = seq.count("G")
    c = seq.count("C")

    return (g+c)/len(seq)
gc_values = []

for seq in all_sequences:
    gc_values.append(gc_content(seq))

plt.hist(gc_values,bins=50)
plt.title("GC Content Distribution")
plt.show()
def gc_content(seq):

    g = seq.count("G")
    c = seq.count("C")

    return (g+c)/len(seq)
gc_values = []

for seq in all_sequences:
    gc_values.append(gc_content(seq))

plt.hist(gc_values,bins=50)
plt.title("GC Content Distribution")
plt.show()