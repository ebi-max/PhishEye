import streamlit as st
from datetime import datetime
import json

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="PhishEye",
    page_icon="🎣",
    layout="centered"
)

# ---------------------------------
# Header / Branding
# ---------------------------------
st.markdown("""
<h2 style="text-align:center;">🎣 PhishEye</h2>
<p style="text-align:center; font-weight:bold;">Powered by Ebiklean Global</p>
<p style="text-align:center;">AI-powered phishing awareness & detection</p>
<hr>
""", unsafe_allow_html=True)

# ---------------------------------
# Session State
# ---------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------------------------
# Login (Simple & Safe)
# ---------------------------------
if st.session_state.user is None:
    name = st.text_input("Enter your name to continue")
    if st.button("Login"):
        if name.strip():
            st.session_state.user = name
            st.rerun()
        else:
            st.warning("Please enter your name")
    st.stop()

st.success(f"Welcome, {st.session_state.user} 👋")

# ---------------------------------
# Notifications
# ---------------------------------
st.info("🔔 Tip: Always verify sender addresses and links before clicking.")

# ---------------------------------
# Phishing Check Inputs
# ---------------------------------
st.subheader("🎯 Phishing Risk Assessment")

email_type = st.selectbox(
    "What type of message are you checking?",
    ["Email", "SMS", "Social Media", "Website Link"]
)

unknown_sender = st.selectbox(
    "Is the sender unknown?",
    ["Yes", "No"]
)

urgent_tone = st.selectbox(
    "Does the message create urgency or fear?",
    ["Yes", "No"]
)

asks_info = st.selectbox(
    "Does it ask for personal or financial information?",
    ["Yes", "No"]
)

# ---------------------------------
# Classification Logic
# ---------------------------------
def phishing_classifier(sender, urgency, info):
    if sender == "Yes" and (urgency == "Yes" or info == "Yes"):
        return "High Risk", "🚨 Likely phishing attempt. Do not interact."
    elif urgency == "Yes":
        return "Moderate Risk", "⚠️ Be cautious and verify the source."
    else:
        return "Low Risk", "✅ No obvious phishing indicators detected."

# ---------------------------------
# Run Assessment
# ---------------------------------
if st.button("Analyze Message"):
    risk, advice = phishing_classifier(unknown_sender, urgent_tone, asks_info)

    st.subheader("🧠 PhishEye Result")
    st.write(f"**Risk Level:** {risk}")
    st.write(f"**Advice:** {advice}")

    # ---------- Corrected report dictionary ----------
    report = {
        "Name": st.session_state.user,
        "Message Type": email_type,
        "Unknown Sender": unknown_sender,
        "Urgent Tone": urgent_tone,
        "Requests Info": asks_info,
        "Risk Level": risk,
        "Advice": advice,
        "Generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Download button
    st.download_button(
        "📥 Download Phishing Report",
        json.dumps(report, indent=4),
        file_name="phisheye_report.json",
        mime="application/json"
    )

# ---------------------------------
# Awareness Gallery
# ---------------------------------
st.markdown("---")
st.subheader("🖼 Phishing Awareness Gallery")

st.image(
    [
        "https://images.unsplash.com/photo-1559136555-9303baea8ebd",
        "https://images.unsplash.com/photo-1600267165611-6d4a9e3c91d4"
    ],
    caption=["Fake Login Pages", "Suspicious Messages"],
    use_column_width=True
)

# ---------------------------------
# Chat Assistant
# ---------------------------------
st.markdown("---")
st.subheader("💬 PhishEye Assistant Chat")

user_msg = st.text_input("Ask about phishing or suspicious messages")

if st.button("Send"):
    if user_msg.strip():
        st.session_state.chat.append(("You", user_msg))
        st.session_state.chat.append(
            ("AI", "If a message pressures you or asks for sensitive data, it is likely phishing.")
        )
        st.rerun()

for sender, msg in st.session_state.chat:
    st.write(f"**{sender}:** {msg}")

# ---------------------------------
# Impact / Investor Dashboard
# ---------------------------------
st.markdown("---")
st.subheader("📊 Impact & Investor Snapshot")

c1, c2, c3 = st.columns(3)
c1.metric("Threat Type", "Phishing")
c2.metric("Primary Users", "Internet Users")
c3.metric("Scalability", "Very High")

st.info(
    "PhishEye helps reduce phishing scams by empowering users with "
    "early detection and awareness tools."
)

# ---------------------------------
# Explore Other Apps
# ---------------------------------
st.markdown("---")
st.subheader("🌍 Explore Other Tools")
st.markdown(
    "➡️ **AI CyberSafe Checker** – Digital safety & phishing prevention"
)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("""
<hr>
<p style="text-align:center; font-size:12px;">
© 2026 Ebiklean Global • AI for Social Good
</p>
""", unsafe_allow_html=True)