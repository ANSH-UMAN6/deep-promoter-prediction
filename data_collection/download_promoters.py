import requests
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from tqdm import tqdm
import time

server = "https://rest.ensembl.org"
headers = {"Accept": "application/json"}

TARGET = 500
records = []

chromosomes = [str(i) for i in range(1, 23)] + ["X", "Y"]

# scan chromosomes in smaller regions
WINDOW = 1000000

for chrom in chromosomes:

    if len(records) >= TARGET:
        break

    print("Scanning chromosome", chrom)

    for start in range(1, 50000000, WINDOW):

        if len(records) >= TARGET:
            break

        end = start + WINDOW

        region_url = f"/overlap/region/human/{chrom}:{start}-{end}?feature=gene"

        response = requests.get(server + region_url, headers=headers)

        if not response.ok:
            continue

        genes = response.json()

        for gene in tqdm(genes):

            if len(records) >= TARGET:
                break

            try:

                gene_start = gene["start"]

                promoter_start = gene_start - 1000
                promoter_end = gene_start + 200

                seq_url = f"/sequence/region/human/{chrom}:{promoter_start}..{promoter_end}:1?"

                seq_response = requests.get(server + seq_url, headers=headers)

                if not seq_response.ok:
                    continue

                seq = seq_response.json()["seq"]

                record = SeqRecord(
                    Seq(seq),
                    id=gene["id"],
                    description="promoter"
                )

                records.append(record)

                time.sleep(0.05)

            except:
                continue


print("Saving sequences...")

SeqIO.write(records, "data/promoters.fasta", "fasta")

print("Total promoters downloaded:", len(records))