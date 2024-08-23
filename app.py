import streamlit as st
import pickle

# Load the model and vectorizer
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit app
st.title("Sentiment Analysis")

user_input = st.text_area("Enter your review here:")

if st.button("Predict"):
    user_input_transformed = vectorizer.transform([user_input])
    prediction = model.predict(user_input_transformed)
    
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    st.write(f"Predicted Sentiment: {sentiment}")