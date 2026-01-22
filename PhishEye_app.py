import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PhishEye",
    page_icon="🐟",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "name" not in st.session_state:
    st.session_state.name = ""

# ---------------- LOGIN SCREEN ----------------
if not st.session_state.logged_in:
    st.title("🐟 PhishEye")
    st.caption("AI-assisted phishing detection & cybersecurity awareness")
    st.markdown("**Powered by Ebiklean Global**")

    name = st.text_input("Enter your name")

    if st.button("Login"):
        if name.strip() == "":
            st.warning("Please enter your name to continue.")
        else:
            st.session_state.name = name
            st.session_state.logged_in = True
            st.rerun()

# ---------------- MAIN APP ----------------
else:
    st.sidebar.success(f"Logged in as {st.session_state.name}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🐟 PhishEye")
    st.markdown("**Powered by Ebiklean Global**")

    st.subheader("Phishing Risk Check")

    # Risk factors for phishing
    unknown_links = st.checkbox("Click links from unknown emails")
    weak_password = st.checkbox("Use weak or repeated passwords")
    public_wifi = st.checkbox("Use public Wi-Fi without protection")
    ignore_updates = st.checkbox("Ignore software/OS updates")

    if st.button("Check Phishing Risk"):
        # Convert booleans to numbers
        link_n = int(unknown_links)
        pwd_n = int(weak_password)
        wifi_n = int(public_wifi)
        update_n = int(ignore_updates)

        # Simple risk calculation
        risk_score = (link_n + pwd_n + wifi_n + update_n) / 4

        st.success("Phishing analysis complete")
        st.write(f"### Estimated Phishing Risk Score: **{risk_score * 100:.1f}%**")

        if risk_score >= 0.75:
            st.error("High phishing risk! Take immediate action.")
        elif risk_score >= 0.4:
            st.warning("Moderate phishing risk. Improve security habits.")
        else:
            st.success("Low phishing risk. Keep practicing good habits.")

        # ---------------- DOWNLOADABLE REPORT ----------------
        report = f"""
🐟 PHISHEYE REPORT
Powered by Ebiklean Global

Name: {st.session_state.name}

Phishing Risk Factors:
- Clicking Unknown Links: {unknown_links}
- Weak/Repeated Passwords: {weak_password}
- Unsafe Public Wi-Fi: {public_wifi}
- Ignoring Updates: {ignore_updates}

Estimated Phishing Risk Score: {risk_score * 100:.1f}%

Recommendations:
- Avoid clicking unknown links
- Use strong, unique passwords
- Enable 2FA
- Keep software and OS updated
- Use VPN on public Wi-Fi

Disclaimer:
This tool provides phishing awareness only.
It is NOT a replacement for professional cybersecurity services.
"""

        st.download_button(
            label="📥 Download PhishEye Report",
            data=report,
            file_name="phisheye_report.txt",
            mime="text/plain"
        )

    st.divider()
    st.subheader("💰 Investor & Impact Overview")
    st.write(
        """
        - Rising demand for phishing & cybersecurity awareness tools  
        - Suitable for schools, NGOs, SMEs, and individuals  
        - Scalable across web and mobile platforms  
        """
    )