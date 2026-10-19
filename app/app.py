from flask import Flask, render_template, request, jsonify
import joblib
import os
import math

from preprocessing import clean_text
from recommendation import recommend_action


# ============================================================
# FLASK CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


# ============================================================
# LOAD TRAINED MODELS
# ============================================================

priority_model = joblib.load(
    os.path.join(BASE_DIR, "models", "priority_model.pkl")
)

category_model = joblib.load(
    os.path.join(BASE_DIR, "models", "category_model.pkl")
)

tfidf = joblib.load(
    os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")
)


# ============================================================
# CONFIDENCE
# ============================================================

def get_confidence(model, message_vector):

    scores = model.decision_function(message_vector)

    if len(scores.shape) == 1:
        score = abs(float(scores[0]))
    else:
        score = abs(float(max(scores[0])))

    confidence = 1 / (1 + math.exp(-score))

    return round(confidence * 100, 2)


# ============================================================
# IMPORTANT FACTORS
# ============================================================

def get_important_factors(message, priority, category):

    text = message.lower()

    factors = []

    urgency_words = [
        "urgent", "immediately", "asap",
        "today", "tomorrow", "deadline",
        "important", "critical"
    ]

    financial_words = [
        "payment", "loan", "debt",
        "bank", "money", "expense",
        "financial", "invoice"
    ]

    academic_words = [
        "assignment", "project", "exam",
        "faculty", "student", "college",
        "submission", "deadline"
    ]

    promotional_words = [
        "offer", "discount", "sale",
        "deal", "promotion", "shopping"
    ]

    for word in urgency_words:
        if word in text:
            factors.append(f"Urgency indicator: '{word}'")

    for word in financial_words:
        if word in text:
            factors.append(f"Financial indicator: '{word}'")

    for word in academic_words:
        if word in text:
            factors.append(f"Academic indicator: '{word}'")

    for word in promotional_words:
        if word in text:
            factors.append(f"Promotional indicator: '{word}'")

    if not factors:
        factors.append(f"Detected category: {category}")
        factors.append(f"Detected priority: {priority}")

    return factors[:5]


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# PREDICTION API
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "error": "Please enter a message."
        }), 400

    # Clean message
    cleaned_message = clean_text(message)

    # TF-IDF
    message_vector = tfidf.transform([cleaned_message])

    # Predictions
    priority = priority_model.predict(message_vector)[0]
    category = category_model.predict(message_vector)[0]

    # Confidence
    priority_confidence = get_confidence(
        priority_model,
        message_vector
    )

    category_confidence = get_confidence(
        category_model,
        message_vector
    )

    # Recommendation
    action = recommend_action(
        message,
        priority,
        category
    )

    # Important factors
    factors = get_important_factors(
        message,
        priority,
        category
    )

    return jsonify({
        "priority": priority,
        "category": category,
        "priority_confidence": priority_confidence,
        "category_confidence": category_confidence,
        "recommended_action": action,
        "important_factors": factors
    })


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)