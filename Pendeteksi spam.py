import pandas as pd
import re
import nltk

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

nltk.download('stopwords')

df = pd.read_csv(r"C:\Users\DELL\OneDrive\Documents\Tugas Coding\Python\Tugas\emails.csv")

print("Jumlah Data:", len(df))
print(df.head())

stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = str(text).lower()

    text = re.sub(r'http\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    tokens = text.split()

    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

print("Preprocessing...")
df["clean_text"] = df["text"].apply(preprocess)

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)   # penting: menangkap frasa "click here", "free money"
)

X = vectorizer.fit_transform(df["clean_text"])
y = df["spam"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\ HASIL MODEL ")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

emails_baru = [
    "Congratulations! You have won $5000. Click here now.",
    "Please attend the meeting tomorrow at 9 AM.",
    "Claim your free lottery prize today.",
    "The project report has been submitted.",
    "Urgent! Verify your account immediately to avoid suspension."
]

print("\n===== PREDIKSI EMAIL BARU =====")

for email in emails_baru:
    clean = preprocess(email)
    vector = vectorizer.transform([clean])
    pred = model.predict(vector)[0]

    hasil = "SPAM" if pred == 1 else "HAM"

    print("\nEmail:")
    print(email)
    print("Prediksi:", hasil)
