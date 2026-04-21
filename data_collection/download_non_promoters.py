import requests
import random
import time
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

server = "https://rest.ensembl.org"
headers = {"Accept": "application/json"}

TARGET = 500
records = []

chromosomes = [str(i) for i in range(1, 23)] + ["X", "Y"]

while len(records) < TARGET:

    chrom = random.choice(chromosomes)

    start = random.randint(1000000, 100000000)

    end = start + 1200

    seq_url = f"/sequence/region/human/{chrom}:{start}..{end}:1?"

    response = requests.get(server + seq_url, headers=headers)

    if not response.ok:
        continue

    try:

        seq = response.json()["seq"]

        record = SeqRecord(
            Seq(seq),
            id=f"random_{len(records)}",
            description="non_promoter"
        )

        records.append(record)

        print("Downloaded:", len(records))

        time.sleep(0.05)

    except:
        continue


print("Saving sequences...")

SeqIO.write(records, "data/non_promoters.fasta", "fasta")

print("Total non-promoters downloaded:", len(records))