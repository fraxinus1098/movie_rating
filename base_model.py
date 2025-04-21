import streamlit as st
import openai

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

st.title("Movie Rating Predictor")
movie_summary = st.text_area("Movie Summary", height=200)
if movie_summary:
    # Query from an LLM, where the user prompt is the movie summary
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a movie critic who specializes in predicting IMDb ratings. Based on the movie summary, predict an IMDb rating between 1.0 and 10.0."},
            {"role": "user", "content": movie_summary}
        ],
        temperature=0.5,
        max_tokens=100
    )
    predicted_rating = response.choices[0].message.content
    st.success(f"Predicted IMDb Rating: {predicted_rating}")  # st.success() displays a green success message box in your app UI.
