import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Translator", layout="centered")

# Supported languages
languages = {
    "English": "en",
    "Bangla": "bn",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Arabic": "ar",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn"
}

st.title("🌐 Python Translator App")
st.write("Enter text below and pick source & target languages.")

# Input area
text = st.text_area("Text to translate", height=180)

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("Source language", list(languages.keys()))
with col2:
    target = st.selectbox("Target language", list(languages.keys()), index=2)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                src_code = languages[source]
                tgt_code = languages[target]
                translated = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
                st.success("Translation complete:")
                st.text_area("Translated text", value=translated, height=180)
            except Exception as e:
                st.error(f"Translation error: {e}")
