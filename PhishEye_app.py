# phisheye_app.py

import streamlit as st
from PIL import Image
import pytesseract
from transformers import pipeline

# Title + Header
st.set_page_config(page_title="PhishEye 🔍", page_icon="👁️")
st.title("PhishEye 🔍")
st.markdown("### Scam Image & Screenshot Detector")
st.write("Upload a screenshot, fake alert, or receipt, and let AI check if it looks like a scam.")

# Upload section
uploaded_file = st.file_uploader("📂 Upload an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Load a HuggingFace Vision-Language pipeline (placeholder for LFM2-VL)
@st.cache_resource
def load_model():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

vl_model = load_model()

def scam_detector(extracted_text: str, ai_caption: str):
    """
    Basic heuristic scam detection.
    Expand later with ML classification or fine-tuning.
    """
    suspicious_keywords = [
        "urgent", "bank", "verify", "password", "lottery",
        "account blocked", "transfer", "click here", "win"
    ]
    red_flags = [word for word in suspicious_keywords if word.lower() in extracted_text.lower() or word in ai_caption.lower()]

    if red_flags:
        return "⚠️ Likely Scam", f"Suspicious terms detected: {', '.join(red_flags)}"
    else:
        return "✅ Safe", "No obvious scam indicators found."

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing with AI..."):
        # Step 1: Caption the image (visual analysis)
        caption = vl_model(image)[0]['generated_text']

        # Step 2: Extract embedded text using OCR
        extracted_text = pytesseract.image_to_string(image)

        # Step 3: Run scam detection logic
        verdict, explanation = scam_detector(extracted_text, caption)

    # Show results
    st.subheader("🔎 Analysis Result")
    st.write(f"**Verdict:** {verdict}")
    st.write(f"**Explanation:** {explanation}")

    # Optional: Show extracted text + AI caption
    with st.expander("See AI Details"):
        st.write("**AI Caption:**", caption)
        st.write("**Extracted Text:**", extracted_text)
