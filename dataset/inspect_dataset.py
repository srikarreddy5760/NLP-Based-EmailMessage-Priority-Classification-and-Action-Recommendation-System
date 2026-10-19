import pandas as pd

df = pd.read_csv("dataset/messages_raw.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nTotal messages:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\n" + "=" * 60)
print("PRIORITY LABELS")
print("=" * 60)

print(df["priority"].value_counts())

print("\n" + "=" * 60)
print("CATEGORY LABELS")
print("=" * 60)

print(df["category"].value_counts())

print("\n" + "=" * 60)
print("ACTION LABELS")
print("=" * 60)

print(df["action"].value_counts())

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

print("\n" + "=" * 60)
print("DUPLICATE MESSAGES")
print("=" * 60)

print("Duplicate rows:", df.duplicated().sum())

print("\n" + "=" * 60)
print("SAMPLE MESSAGES")
print("=" * 60)

for i in range(min(10, len(df))):
    print(f"\n--- Message {i + 1} ---")
    print("Subject :", df.loc[i, "subject"])
    print("Category:", df.loc[i, "category"])
    print("Priority:", df.loc[i, "priority"])
    print("Action  :", df.loc[i, "action"])