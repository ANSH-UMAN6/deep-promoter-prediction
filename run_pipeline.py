import os

print("STEP 1: Downloading promoter sequences")
os.system("python data_collection/download_promoters.py")

print("\nSTEP 2: Downloading non-promoter sequences")
os.system("python data_collection/download_non_promoters.py")

print("\nSTEP 3: Training model")
os.system("python training/train_model.py")

print("\nSTEP 4: Evaluating model")
os.system("python evaluation/evaluate_model.py")

print("\nSTEP 5: Visualizing learned motifs")
os.system("python visualization/motif_visualization.py")

print("\nPipeline completed successfully!")