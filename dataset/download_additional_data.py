from datasets import load_dataset

print("Downloading additional email dataset...")

dataset = load_dataset(
    "imnim/multiclass-email-classification",
    split="train"
)

df = dataset.to_pandas()

print("\nDataset downloaded successfully!")
print("Number of rows:", len(df))
print("\nColumns:")
print(df.columns.tolist())

df.to_csv(
    "dataset/category_source.csv",
    index=False
)

print("\nSaved as dataset/category_source.csv")