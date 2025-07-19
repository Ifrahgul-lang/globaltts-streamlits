import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="GlobalTTS-X", layout="centered")
st.title("🌍 GlobalTTS-X: Multilingual Text to Speech")

text = st.text_area("Enter text")
lang = st.selectbox("Select language", ["en", "ur", "hi", "ar", "fr", "de", "es", "zh-CN", "ru"])

if st.button("🔊 Generate Speech"):
    tts = gTTS(text=text, lang=lang)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    st.audio(audio_bytes.getvalue(), format="audio/mp3")