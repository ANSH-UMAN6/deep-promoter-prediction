# 🧬 DNA Promoter Predictor using Deep Learning (CNN)

A bioinformatics + deep learning project for predicting **Promoter** and **Non-Promoter** DNA sequences using a **1D Convolutional Neural Network (CNN)** built with **PyTorch** and deployed through a **Flask web application**.

---

## 📌 Project Overview

Promoters are regulatory DNA regions located near genes that initiate transcription. Correct identification of promoter regions is important in:

* Gene regulation studies
* Genome annotation
* Disease research
* Drug discovery
* Biotechnology

Traditional wet-lab methods are expensive and time-consuming. This project provides an AI-based computational alternative.

---

## 🚀 Features

✅ Manual DNA sequence prediction
✅ Real genomic sequence fetch using Ensembl API
✅ Human / Mouse organism selection
✅ Promoter vs Non-Promoter classification
✅ Confidence score output
✅ Dynamic graph visualization
✅ Flask-based web interface

---

## 🧠 Technologies Used

| Technology          | Purpose             |
| ------------------- | ------------------- |
| Python              | Core language       |
| PyTorch             | CNN model           |
| Flask               | Backend             |
| HTML/CSS/JavaScript | Frontend            |
| Matplotlib          | Graph generation    |
| Ensembl REST API    | Genomic data source |

---

## 📂 Project Structure

```text
sequence-motif-research/
│── app.py
│── motif_model.pth
│── models/
│   └── cnn_model.py
│── preprocessing/
│   └── encode_sequences.py
│── training/
│   ├── train_model.py
│   ├── build_dataset.py
│   └── evaluate_model.py
│── templates/
│   └── index.html
│── static/
│   ├── style.css
│   └── prediction_graph.png
│── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/dna-promoter-predictor.git
cd dna-promoter-predictor
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask torch requests matplotlib scikit-learn
```

---

## 🧪 Train the Model

```bash
python training/train_model.py
```

This generates:

```text
motif_model.pth
```

---

## 🌐 Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🧬 How It Works

### Input

DNA Sequence:

```text
ATGCGTACGTTAGCGATCGTAGC...
```

### Preprocessing

* Fixed-length normalization
* One-hot encoding

### Prediction Output

```text
Promoter (Score: 0.91)
```

or

```text
Non-Promoter (Score: 0.12)
```

---

## 📊 CNN Architecture

```text
Input Sequence
   ↓
Conv1D Layer
   ↓
ReLU
   ↓
MaxPooling
   ↓
Conv1D Layer
   ↓
Flatten
   ↓
Fully Connected Layer
   ↓
Sigmoid Output
```

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* ROC Curve
* Confusion Matrix
* Loss Curve

---

## 🔬 Biological Importance

Promoters regulate gene expression by enabling transcription initiation. This model learns sequence motifs such as:

* TATA box
* GC-rich regions
* CpG islands
* Other hidden promoter signatures

---

## 🔮 Future Scope

* Transformer-based models
* More species support
* Explainable AI motif detection
* Better dashboard UI
* Clinical genomics applications

---

## 👨‍💻 Author

**Ansh**

Bioinformatics / Deep Learning Project

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project, give it a star on GitHub.
