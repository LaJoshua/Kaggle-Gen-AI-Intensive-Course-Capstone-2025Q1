import streamlit as st
import google.generativeai as genai
import json
import re
from PIL import Image

# --- CONFIGURE GEMINI ---
genai.configure(api_key="")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash")

# --- PROMPT TEMPLATE ---
FEW_SHOT_PROMPT = """
Here are some motivational quotes in JSON format:
1. {{ "quote": "Believe in yourself and all that you are.", "author": "Christian D. Larson", "category": "belief", "tone": "encouraging" }}
2. {{ "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill", "category": "success", "tone": "motivational" }}

Now create a new motivational quote about: {topic}.
Return the result strictly in JSON format like above, with keys: quote, author, category, and tone.
"""

# --- FUNCTION: Generate Structured Quote ---
def generate_structured_quote(topic, temperature=0.7):
    prompt = FEW_SHOT_PROMPT.format(topic=topic)
    try:
        response = model.generate_content(prompt, temperature=temperature)
        match = re.search(r'\{.*?\}', response.text, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found in response.")
        json_str = match.group()
        parsed_response = json.loads(json_str)
        return {
            "quote": parsed_response.get("quote", "No quote"),
            "author": parsed_response.get("author", "Anonymous")
        }
    except Exception:
        return {
            "quote": "Something went wrong.",
            "author": "System"
        }

# --- FUNCTION: Generate Quote from Image ---
def generate_quote_from_image(image_file, temperature=0.7):
    try:
        image = Image.open(image_file)
        response = model.generate_content(
            ["Generate a motivational quote inspired by this image. Return only the quote and author in JSON format like this: { \"quote\": \"...\", \"author\": \"...\" }", image],
            temperature=temperature
        )
        match = re.search(r'\{.*?\}', response.text, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found.")
        parsed = json.loads(match.group())
        return {
            "quote": parsed.get("quote", "Let the image speak to your soul."),
            "author": parsed.get("author", "Visual Muse")
        }
    except Exception:
        return {
            "quote": "Could not generate a quote from this image.",
            "author": "System"
        }

# --- STREAMLIT UI ---
st.set_page_config(page_title="Gemini Quote Generator", page_icon="🌟")
st.title("🌟 Motivational Quote Generator")

# --- Temperature Slider ---
st.subheader("🎚️ Adjust Temperature for Randomness")
temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)  # Min, Max, Default, Step size

# --- Text-Based Generator ---
st.subheader("🧠 Generate a Quote from a Topic")
topic = st.selectbox("Choose a topic:", ["Success", "Hard Work", "Positivity", "Failure", "Life"])
if st.button("Generate Quote"):
    result = generate_structured_quote(topic, temperature)
    st.markdown(f"**💬 _{result['quote']}_**")
    st.markdown(f"— *{result['author']}*")

# --- Image-Based Generator ---
st.subheader("🖼️ Generate a Quote from an Image")
uploaded_image = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
    if st.button("Generate Image Quote"):
        result = generate_quote_from_image(uploaded_image, temperature)
        st.markdown(f"**💬 _{result['quote']}_**")
        st.markdown(f"— *{result['author']}*")

# --- Footer ---
st.markdown("---")
st.caption("Made with 💡 using Gemini AI")