# 🌟 Motivational Quote Generator (Google Gemini Capstone Project)

This project is a **capstone application** built with **Google Gemini** (via the `google-generativeai` API) and **Streamlit**. It generates **motivational quotes** in two ways:
- From a **given topic** (e.g., Success, Hard Work, Life, etc.)
- From an **uploaded image**, where Gemini analyzes the visual content and creates an inspiring quote.

---

## 🚀 Features
- **Text-based quote generation**: Enter or select a topic and generate a structured JSON response containing the quote and author.
- **Image-based quote generation**: Upload a JPG/PNG image, and Gemini will generate a motivational quote inspired by the image.
- **Interactive UI with Streamlit**:
  - Temperature slider 🎚️ to adjust creativity/randomness.
  - Live rendering of quotes in a clean, styled interface.
- **Error handling** for invalid responses or missing JSON formatting.

---

## 🛠️ Tech Stack
- **Python 3**
- **Google Gemini (Generative AI API)**
- **Streamlit** (for the web interface)
- **PIL (Pillow)** for image handling
- **Regex + JSON** for parsing structured AI responses

