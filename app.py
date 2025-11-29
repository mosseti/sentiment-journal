import streamlit as st
from transformers import pipeline
import plotly.express as px
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Mood Journal", layout="centered")

st.title("🧠 AI Mood Journal")
st.write("Write a journal entry and let AI analyze your mood.")

# Load model (cached so it loads only once)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

sentiment_analyzer = load_model()

# Load or initialize journal history
def load_history():
    try:
        return pd.read_csv("journal_history.csv")
    except:
        return pd.DataFrame(columns=["timestamp", "entry", "label", "score"])

def save_history(df):
    df.to_csv("journal_history.csv", index=False)

history = load_history()

# USER INPUT
entry = st.text_area("📝 Write your journal entry:", height=150)

if st.button("Analyze & Save"):
    if entry.strip() == "":
        st.warning("Please write something first.")
    else:
        with st.spinner("Analyzing mood..."):
            result = sentiment_analyzer(entry)[0]
            label = result["label"]
            score = round(result["score"], 3)

        # Store entry
        new_row = {
            "timestamp": datetime.now(),
            "entry": entry,
            "label": label,
            "score": score
        }
        history = pd.concat([history, pd.DataFrame([new_row])], ignore_index=True)
        save_history(history)

        st.success(f"Mood detected: **{label}** (confidence: {score})")

# Show history + chart
if len(history) > 0:
    st.subheader("📊 Mood History")

    fig = px.line(
        history,
        x="timestamp",
        y="score",
        color="label",
        markers=True,
        title="Sentiment Score Over Time"
    )
    st.plotly_chart(fig)

    st.dataframe(history)