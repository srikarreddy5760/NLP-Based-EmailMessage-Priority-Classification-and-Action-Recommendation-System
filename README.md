
# NLP-Based Email/Message Priority Classification and Action Recommendation System

## 📌 About the Project

The **NLP-Based Email/Message Priority Classification and Action Recommendation System** is a machine learning web application that helps users identify important messages, categorize them, and determine appropriate actions.

The system uses Natural Language Processing (NLP) and Machine Learning to analyze user-entered messages and classify them into priority levels and categories.

## ✨ Features

- **Priority Classification:** Classifies messages as High, Medium, or Low.
- **Category Classification:** Categorizes messages into Academic, Work/Professional, Personal, Financial, Promotional, or Other.
- **Action Recommendation:** Suggests suitable actions based on predefined rules.
- **Confidence Estimate:** Displays a model-derived confidence estimate.
- **Important Keywords:** Identifies selected keywords relevant to the prediction.
- **Web Interface:** Allows users to enter messages and view results through a web application.

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- NLTK
- TF-IDF Vectorization
- Scikit-learn
- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (SVM)
- Flask
- HTML
- CSS
- JavaScript
- Joblib

## ⚙️ How It Works

1. The user enters a message into the web application.
2. The system preprocesses the text using NLP techniques.
3. TF-IDF converts the message into numerical features.
4. Machine learning models predict the priority and category.
5. The system displays the results, confidence estimate, important keywords, and recommended action.

## 📊 Dataset

The prepared dataset contains **1,800 messages** with the following priority distribution:

| Priority | Number of Messages |
|---|---:|
| High | 600 |
| Medium | 600 |
| Low | 600 |
| **Total** | **1,800** |

The dataset includes six categories:

- Academic
- Work/Professional
- Personal
- Financial
- Promotional
- Other

## 🤖 Machine Learning Models

Three algorithms were implemented and compared:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine (SVM)

### Best Model Results

| Classification Task | Best Model | Accuracy |
|---|---|---:|
| Priority Classification | Linear SVM | 93.61% |
| Category Classification | Linear SVM | 98.61% |

*Note: These results were obtained on the prepared test dataset. Performance may differ on real-world messages, particularly because some message categories are strongly associated with specific priority labels in the dataset.*

## 🚀 Installation and Execution

### Prerequisites

- Python installed
- Visual Studio Code or another Python IDE
- Required project files and trained model files

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project folder:

```bash
cd NLP-Email-Message-Priority-Classification
```

Replace the repository URL and folder name with your actual GitHub details if they differ.

### Step 2: Install Dependencies

```bash
pip install flask pandas scikit-learn nltk joblib
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

Enter a message and view its predicted priority, category, and recommended action.

**Important:** Ensure that the trained model files, Flask templates, and other required project files are available in their expected locations before running the application.

## 📁 Project Structure

```text
NLP-Email-Message-Priority-Classification/
│
├── app.py
├── dataset/
│   └── messages.csv
├── models/
│   └── trained model files
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

*The structure above is illustrative. Adjust file and folder names to match your actual repository.*

## 🔮 Future Enhancements

- Integrate with Gmail or Outlook.
- Use a larger and more diverse message dataset.
- Improve confidence estimates through probability calibration.
- Add more explainable AI techniques.
- Develop more context-aware action recommendations.
- Explore transformer-based NLP models.

## 🎓 Project Information

- **Project Title:** NLP-Based Email/Message Priority Classification and Action Recommendation System
- **Course:** Natural Language Processing
- **Department:** Computer Science and Engineering (AI & ML)
- **Institution:** Vardhaman College of Engineering, Hyderabad

## 📌 Limitations

- Predictions depend on the quality and diversity of the training dataset.
- Classification results may not generalize to every real-world message.
- Confidence estimates are derived from Linear SVM decision scores and are not calibrated probabilities.
- Recommended actions are generated using predefined rules.
- The current application requires users to enter messages manually; direct email-platform integration is not implemented.

## 📄 Disclaimer

This project is developed for educational purposes. The predictions and recommendations are intended to assist users and should not replace human judgment when handling important messages.
