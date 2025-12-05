import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Language Translation Tool (Deep Translator)")

# Input text
text_to_translate = st.text_area("Enter text to translate:")

# Language selection
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "Arabic": "ar",
    "German": "de",
    "Tamil": "ta",
    "Urdu": "ur"
}

source_lang = st.selectbox("Select source language:", list(languages.keys()), index=0)
target_lang = st.selectbox("Select target language:", list(languages.keys()), index=1)

# Translate button
if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text to translate!")
    else:
        try:
            translated_text = GoogleTranslator(source=languages[source_lang],
                                               target=languages[target_lang]).translate(text_to_translate)
            st.success("✅ Translation Completed!")
            st.subheader("Translated Text:")
            st.write(translated_text)
        except Exception as e:
            st.error(f"❌ Translation Failed: {e}")
