import pandas as pd
import random

random.seed(42)

# ============================================================
# 1. LOAD ORIGINAL DATASET
# ============================================================

df = pd.read_csv("dataset/messages_raw.csv")

# Combine subject + body
df["message"] = (
    df["subject"].fillna("") + " " +
    df["body"].fillna("")
).str.strip()

# ============================================================
# 2. MAP ORIGINAL CATEGORIES
# ============================================================

category_map = {
    "meeting_request": "Work/Professional",
    "customer_support": "Work/Professional",
    "personal": "Personal",
    "finance": "Financial",
    "phishing": "Other",
    "travel": "Other"
}

df["category"] = df["category"].map(category_map)

# ============================================================
# 3. MAP PRIORITIES
# ============================================================

priority_map = {
    "urgent": "High",
    "high": "High",
    "medium": "Medium"
}

df["priority"] = df["priority"].map(priority_map)

df = df.dropna(subset=["message", "priority", "category"])

df = df[["message", "priority", "category"]]

# Remove duplicates
df = df.drop_duplicates(subset=["message"])

# ============================================================
# 4. CREATE PROJECT-SPECIFIC ACADEMIC DATA
# ============================================================

academic_subjects = [
    "assignment submission",
    "project review",
    "internal examination",
    "laboratory record",
    "seminar presentation",
    "viva examination",
    "attendance requirement",
    "coding assessment",
    "semester examination",
    "mini project",
    "technical workshop",
    "academic registration",
    "project documentation",
    "practical examination",
    "faculty meeting",
    "course assignment",
    "department evaluation",
    "research presentation",
    "class test",
    "academic notice"
]

academic_actions = [
    "Please submit the required work",
    "Please complete the required work",
    "Please upload the document",
    "Please attend the scheduled session",
    "Please prepare the required material",
    "Please check the instructions",
    "Please complete the registration",
    "Please bring the required documents",
    "Please review the information",
    "Please contact the faculty coordinator"
]

academic_times = [
    "today",
    "tomorrow",
    "before the deadline",
    "this week",
    "by Friday",
    "before 10 AM",
    "next Monday",
    "before the examination",
    "before the project review",
    "within the given deadline"
]

academic_rows = []

for i in range(600):
    subject = random.choice(academic_subjects)
    action = random.choice(academic_actions)
    time = random.choice(academic_times)

    message = (
        f"Regarding the {subject}, {action} {time}. "
        f"Please make sure to follow the instructions provided by the department."
    )

    # Mix priority realistically
    priority = random.choices(
        ["High", "Medium", "Low"],
        weights=[45, 50, 5]
    )[0]

    academic_rows.append({
        "message": message,
        "priority": priority,
        "category": "Academic"
    })

# ============================================================
# 5. CREATE PROMOTIONAL DATA
# ============================================================

promotion_subjects = [
    "special sale",
    "exclusive discount",
    "weekend offer",
    "seasonal sale",
    "new product launch",
    "member offer",
    "limited time deal",
    "shopping promotion",
    "special customer offer",
    "festival discount",
    "new collection",
    "exclusive promotion",
    "free shipping offer",
    "anniversary sale",
    "clearance sale",
    "membership discount",
    "special bundle",
    "launch offer",
    "customer reward",
    "shopping event"
]

promotion_actions = [
    "Shop now and enjoy the offer",
    "Take advantage of the discount",
    "Visit our store to learn more",
    "Use the promotional offer today",
    "Explore our latest products",
    "Enjoy special savings",
    "Claim your offer",
    "Discover the new collection",
    "Check out the available deals",
    "Save more on your next purchase"
]

promotion_times = [
    "today",
    "this weekend",
    "for a limited time",
    "this week",
    "before the offer ends",
    "during our promotional period",
    "while the offer is available",
    "until the end of the month"
]

promotion_rows = []

for i in range(600):
    subject = random.choice(promotion_subjects)
    action = random.choice(promotion_actions)
    time = random.choice(promotion_times)

    message = (
        f"Our {subject} is now available. "
        f"{action} {time}. "
        f"Visit our website for more details."
    )

    promotion_rows.append({
        "message": message,
        "priority": "Low",
        "category": "Promotional"
    })

# ============================================================
# 6. COMBINE DATA
# ============================================================

additional_df = pd.DataFrame(
    academic_rows + promotion_rows
)

final_df = pd.concat(
    [df, additional_df],
    ignore_index=True
)

# Remove duplicates
final_df = final_df.drop_duplicates(
    subset=["message"]
).reset_index(drop=True)

# ============================================================
# 7. BALANCE EACH CATEGORY
# ============================================================

categories = [
    "Academic",
    "Work/Professional",
    "Personal",
    "Financial",
    "Promotional",
    "Other"
]

category_parts = []

# Maximum number taken from each category
category_target = 300

for category in categories:

    category_data = final_df[
        final_df["category"] == category
    ]

    print(
        f"{category}: {len(category_data)} available"
    )

    if len(category_data) >= category_target:

        category_data = category_data.sample(
            n=category_target,
            random_state=42
        )

    else:

        # If a category has fewer than target examples,
        # sample with replacement only when necessary.
        category_data = category_data.sample(
            n=category_target,
            replace=True,
            random_state=42
        )

    category_parts.append(category_data)

final_df = pd.concat(
    category_parts,
    ignore_index=True
)

# ============================================================
# 8. BALANCE PRIORITY
# ============================================================

# We want approximately equal priority distribution.
# Because category balancing comes first, we select
# 600 examples of each priority where possible.

priority_parts = []

for priority in ["High", "Medium", "Low"]:

    priority_data = final_df[
        final_df["priority"] == priority
    ]

    if len(priority_data) >= 600:

        priority_data = priority_data.sample(
            n=600,
            random_state=42
        )

    else:

        priority_data = priority_data.sample(
            n=600,
            replace=True,
            random_state=42
        )

    priority_parts.append(priority_data)

final_df = pd.concat(
    priority_parts,
    ignore_index=True
)

# ============================================================
# 9. SHUFFLE
# ============================================================

final_df = final_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# ============================================================
# 10. SAVE
# ============================================================

final_df.to_csv(
    "dataset/messages.csv",
    index=False
)

# ============================================================
# 11. DISPLAY FINAL INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATASET CREATED")
print("=" * 60)

print("\nTotal messages:")
print(len(final_df))

print("\nPriority distribution:")
print(final_df["priority"].value_counts())

print("\nCategory distribution:")
print(final_df["category"].value_counts())

print("\nMissing values:")
print(final_df.isnull().sum())

print("\nSaved to:")
print("dataset/messages.csv")