from flask import Flask, request, jsonify, render_template
import torch
import requests
import random
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt 
import os
from models.cnn_model import MotifCNN
from preprocessing.encode_sequences import encode_sequence, fix_length

app = Flask(__name__)

# Load model
model = MotifCNN()
model.load_state_dict(torch.load("motif_model.pth", map_location="cpu"))
model.eval()


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():
    seq = request.form["sequence"]

    seq = fix_length(seq)
    encoded = encode_sequence(seq)

    x = torch.tensor(encoded).permute(1, 0).unsqueeze(0).float()

    with torch.no_grad():
        output = model(x)
        score = torch.sigmoid(output).item()

    label = "Promoter" if score > 0.5 else "Non-Promoter"

    return jsonify({
        "prediction": label,
        "confidence": round(score, 3)
    })


@app.route("/predict_organism", methods=["POST"])
def predict_organism():

    organism = request.form.get("organism", "homo_sapiens")
    chrom = request.form.get("chromosome", "1")
    start_pos = int(request.form.get("start", 1))
    end_pos = int(request.form.get("end", 1000000))

    if end_pos <= start_pos:
        return jsonify([{"error": "End must be greater than Start"}])

    server = "https://rest.ensembl.org"
    headers = {"Accept": "application/json"}

    sequences = []

    # Fetch genes
    region_url = f"/overlap/region/{organism}/{chrom}:{start_pos}-{end_pos}?feature=gene"
    response = requests.get(server + region_url, headers=headers)

    if response.ok:
        genes = response.json()

        for gene in genes:
            try:
                gene_start = gene["start"]

                promoter_start = max(1, gene_start - 200)
                promoter_end = gene_start + 50

                seq_url = f"/sequence/region/{organism}/{chrom}:{promoter_start}..{promoter_end}:1?"
                seq_response = requests.get(server + seq_url, headers=headers)

                if seq_response.ok:
                    sequences.append(seq_response.json()["seq"])

            except:
                continue

    # Non-promoters
    count = len(sequences)

    for _ in range(count):
        try:
            rand_start = random.randint(100000000, 150000000)
            rand_end = rand_start + 1200

            seq_url = f"/sequence/region/{organism}/{chrom}:{rand_start}..{rand_end}:1?"
            response = requests.get(server + seq_url, headers=headers)

            if response.ok:
                sequences.append(response.json()["seq"])

        except:
            continue

    if len(sequences) == 0:
        return jsonify([{"sequence": "No data", "label": "Error", "score": 0}])

    # Prediction
    results = []

    for seq in sequences:
        seq = fix_length(seq)
        encoded = encode_sequence(seq)

        x = torch.tensor(encoded).permute(1, 0).unsqueeze(0).float()

        with torch.no_grad():
            output = model(x)
            score = torch.sigmoid(output).item()

        label = "Promoter" if score > 0.5 else "Non-Promoter"

        results.append({
            "sequence": seq[:30] + "...",
            "label": label,
            "score": round(score, 3)
        })

    # =========================
    # 📊 PROFESSIONAL GRAPH
    # =========================
    scores = [item["score"] for item in results]
    labels = [item["label"] for item in results]

    plt.figure(figsize=(8,5))

    # Line plot
    plt.plot(scores, linestyle='-', alpha=0.4)

    # Colored points
    colors = ['green' if l == "Promoter" else 'red' for l in labels]
    plt.scatter(range(len(scores)), scores, c=colors, s=80)

    # Threshold line
    plt.axhline(y=0.5, linestyle='--')

    # Labels
    plt.title("Prediction Confidence Across Sequences")
    plt.xlabel("Sequence Index")
    plt.ylabel("Score (Probability)")

    # Grid
    plt.grid(alpha=0.3)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Promoter',
               markerfacecolor='green', markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Non-Promoter',
               markerfacecolor='red', markersize=8)
    ]

    plt.legend(handles=legend_elements)

    # Save graph
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/prediction_graph.png")
    plt.close()

    # =========================
    # RETURN
    # =========================
    return jsonify({
        "results": results,
        "graph": "prediction_graph.png"
    })

    # =========================
    # RETURN (INSIDE FUNCTION)
    # =========================
    return jsonify({
        "results": results,
        "graph": "prediction_graph.png"
    })
if __name__ == "__main__":
    app.run(debug=True)