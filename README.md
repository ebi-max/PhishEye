# 🔍 PhishEye – Scam Image & Screenshot Detector  

PhishEye is a **vision-powered cybersecurity tool** built during **Hack02: LFMs with Eyes 👀**.  
It detects scam screenshots, fake bank alerts, and fraudulent receipts by combining **Vision-Language AI** with **OCR text analysis**.  

---

## 🚀 Features  
- 📂 Upload screenshots, alerts, or receipts  
- 👁️ Vision-Language Model (LFM2-VL / BLIP) generates captions & context  
- 🔤 OCR (Tesseract) extracts embedded text from images  
- ⚠️ Scam detection using **keyword + pattern analysis**  
- ✅ Verdict with explanation (Safe vs Scam)  
- 📊 Expander shows **AI caption & extracted text** for transparency  

---

## 🛠️ Tech Stack  
- [Streamlit](https://streamlit.io/) – Frontend UI  
- [Transformers](https://huggingface.co/transformers/) – Vision-Language Model (`Salesforce/blip-image-captioning-base`)  
- [Pytesseract](https://github.com/madmaze/pytesseract) – OCR for text extraction  
- [Python 3.9+](https://www.python.org/)  

---

## 📂 Project Structure
