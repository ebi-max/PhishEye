import streamlit as st
from datetime import datetime
import json
import random

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="Reddit CyberSafe Game",
    page_icon="🎮",
    layout="centered"
)

# ---------------------------------
# Header / Branding
# ---------------------------------
st.markdown("""
<h2 style="text-align:center;">🎮 Reddit CyberSafe Game</h2>
<p style="text-align:center; font-weight:bold;">Powered by Ebiklean Global</p>
<p style="text-align:center;">Learn cyber safety with interactive challenges</p>
<hr>
""", unsafe_allow_html=True)

# ---------------------------------
# Session State
# ---------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "chat" not in st.session_state:
    st.session_state.chat = []

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# ---------------------------------
# Login
# ---------------------------------
if st.session_state.user is None:
    name = st.text_input("Enter your name to start playing")
    if st.button("Login"):
        if name.strip():
            st.session_state.user = name
            st.rerun()
        else:
            st.warning("Please enter your name")
    st.stop()

st.success(f"Welcome, {st.session_state.user} 👋")

st.info("🔔 Tip: Answer carefully to learn about online safety!")

# ---------------------------------
# Quiz / Game Data
# ---------------------------------
questions = [
    {
        "q": "You receive an email asking for your password. What should you do?",
        "options": ["Ignore and report", "Reply immediately", "Click the link"],
        "answer": 0
    },
    {
        "q": "You see a suspicious link on social media. You should:",
        "options": ["Click it", "Report it or ignore", "Share it with friends"],
        "answer": 1
    },
    {
        "q": "A website asks for your credit card unexpectedly. You should:",
        "options": ["Provide info", "Check website security and legitimacy", "Ignore security warnings"],
        "answer": 1
    }
]

# ---------------------------------
# Display Question
# ---------------------------------
if st.session_state.question_index < len(questions):
    q_data = questions[st.session_state.question_index]
    st.subheader(f"❓ Question {st.session_state.question_index + 1}")
    st.write(q_data["q"])
    choice = st.radio("Select your answer:", q_data["options"])

    if st.button("Submit Answer"):
        if choice == q_data["options"][q_data["answer"]]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q_data['options'][q_data['answer']]}")
        st.session_state.question_index += 1
        st.rerun()
else:
    st.subheader("🏆 Game Finished!")
    st.write(f"Your score: {st.session_state.score} / {len(questions)}")

    # Download Report
    report = {
        "Name": st.session_state.user,
        "Score": st.session_state.score,
        "Total Questions": len(questions),
        "Generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    st.download_button(
        "📥 Download Game Report",
        json.dumps(report, indent=4),
        file_name="cybersafe_game_report.json",
        mime="application/json"
    )

# ---------------------------------
# Gallery / Hints
# ---------------------------------
st.markdown("---")
st.subheader("🖼 Cyber Safety Hints Gallery")
st.image(
    [
        "https://images.unsplash.com/photo-1591696331111-77ec7ab4dfe4",
        "https://images.unsplash.com/photo-1561130794-0b644a4a3f2a"
    ],
    caption=["Stay alert online", "Verify links and sources"],
    use_column_width=True
)

# ---------------------------------
# Chat Assistant
# ---------------------------------
st.markdown("---")
st.subheader("💬 Cyber Game Assistant")

user_msg = st.text_input("Ask about online safety during the game")

if st.button("Send Message"):
    if user_msg.strip():
        st.session_state.chat.append(("You", user_msg))
        st.session_state.chat.append(
            ("AI", "Remember: Never share passwords, verify links, and report suspicious messages.")
        )
        st.rerun()

for sender, msg in st.session_state.chat:
    st.write(f"**{sender}:** {msg}")

# ---------------------------------
# Investor / Impact Dashboard
# ---------------------------------
st.markdown("---")
st.subheader("📊 Impact & Investor Snapshot")

c1, c2, c3 = st.columns(3)
c1.metric("Game Type", "Interactive Quiz")
c2.metric("Target Users", "Internet Users")
c3.metric("Scalability", "High")

st.info(
    "Reddit CyberSafe Game improves awareness of phishing, social engineering, "
    "and online safety through gamified learning."
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