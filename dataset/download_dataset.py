from datasets import load_dataset
import pandas as pd

print("Downloading email dataset...")

dataset = load_dataset(
    "weijianzhg/email-triage-action-seed",
    split="train"
)

df = dataset.to_pandas()

print("\nDataset downloaded successfully!")
print("Number of rows:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

df.to_csv(
    "dataset/messages_raw.csv",
    index=False
)

print("\nSaved as dataset/messages_raw.csv")