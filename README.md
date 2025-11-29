# 🧠 AI Mood Journal

An interactive AI-powered journal that analyzes the emotional tone of your entries using a transformer-based sentiment analysis model. Built with **Python**, **Streamlit**, **HuggingFace Transformers**, and **Plotly**, this app provides real-time mood detection and visual mood tracking over time.

---

## ✨ Features

- 📝 Write your daily journal entries directly in the browser  
- 🤖 Real-time sentiment analysis using a transformer model  
- 📊 Mood history visualized with interactive charts  
- 💾 Entries saved and stored locally on the server  
- 🌐 Fully deployed and accessible online via Streamlit Cloud  
- ⚡ Clean, modern UI built with Streamlit  

---

## 🤖 AI Model Used

This app uses the **CardiffNLP Twitter RoBERTa Base Sentiment model**:

- **Model:** `cardiffnlp/twitter-roberta-base-sentiment-latest`  
- **Type:** Transformer-based RoBERTa model  
- **Framework:** HuggingFace Transformers  
- **Outputs:** `Positive`, `Neutral`, `Negative` sentiments  

This model is known for:
- High performance on social-text sentiment tasks  
- Strong generalization on natural language input  
- Efficient real-time inference  

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Streamlit** – Front-end and UI
- **Transformers** – Sentiment analysis pipeline
- **Torch** – Model backend
- **Plotly** – Data visualization
- **Pandas** – Storage and data manipulation

---

## 🚀 Live Demo

Try the app online here:

👉 **https://mosseti-sentiment-journal.streamlit.app**


---


---

## 🛠️ Installation (Local)

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-journal.git
cd sentiment-journal

Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

