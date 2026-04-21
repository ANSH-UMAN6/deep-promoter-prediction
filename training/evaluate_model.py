import torch
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt

def evaluate(model, dataloader):

    model.eval()

    y_true = []
    y_pred = []
    y_probs = []

    with torch.no_grad():
        for x, y in dataloader:

            output = model(x)
            probs = torch.sigmoid(output).view(-1)

            preds = (probs > 0.5).int()

            y_true.extend(y.numpy())
            y_pred.extend(preds.numpy())
            y_probs.extend(probs.numpy())

    # 📊 METRICS
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))

    # 📊 CONFUSION MATRIX
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:\n", cm)

    plt.figure()
    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar()
    plt.savefig("static/confusion_matrix.png")
    plt.close()

    # 📈 ROC CURVE
    fpr, tpr, _ = roc_curve(y_true, y_probs)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr)
    plt.title(f"ROC Curve (AUC = {roc_auc:.2f})")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.savefig("static/roc_curve.png")
    plt.close()

    print("Graphs saved!")