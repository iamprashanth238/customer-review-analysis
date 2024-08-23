import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Example dataset
data = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t')

# Text preprocessing (you may include additional steps)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['Review'])
y = data['Liked']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the model and vectorizer
with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
