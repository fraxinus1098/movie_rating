import streamlit as st
import openai
st.title("Movie Rating Predictor")
movie_summary = st.text_area("Movie Summary", height=200)
if movie_summary:
"query from an LLM, where the user prompt is the movie summary"
response = openai.chat.completions.create(
model="gpt-4o-mini",
...
)
predicted_rating = response.choices[0].message.content
st.success(f"Predicted IMDb Rating: {predicted_rating}") #st.success() displays
a green success message box in your app UI.
