
import streamlit as st
from detector import analyze_url

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️"
)

st.title("🛡️ PHISHGUARD")

st.caption("INTELLIGENT PHISHING URL DETECTION SYSTEM")

st.divider()

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Website Security Scanner")
    st.write("Analyze suspicious URLs and identify potential phishing indicators.")

with col2:
    st.metric("Detection Engine", "ACTIVE")

st.divider()

url = st.text_input("Enter a website URL:")

if st.button("Analyze URL"):

    if url.strip():

        score, reasons = analyze_url(url.strip())

        st.subheader("Analysis Results")

        # Calculate risk level
        if score <= 1:
            st.success("LOW RISK")
            st.write("No major warning signs were detected.")

        elif score <= 3:
            st.warning("MEDIUM RISK")
            st.write("Some suspicious characteristics were detected.")

        else:
            st.error("HIGH RISK")
            st.write("Several suspicious characteristics were detected.")

        # Risk score meter
        score_col, bar_col = st.columns([1, 3])

        with score_col:
            st.metric("Risk Score", f"{score}/11")

        with bar_col:
            st.write("Threat Level")
            st.progress(min(score / 11, 1.0))
            st.caption(f"{score} out of 11 risk points")

        # Display reasons
        if reasons:
            st.write("### Why was this URL flagged?")

            for reason in reasons:
                st.write("⚠️", reason)

        else:
            st.write("No suspicious characteristics found by our current checks.")

        # Safety recommendations
        st.write("### 🛡️ Safety Recommendation")

        if score >= 4:
            st.error("Avoid visiting this website. Do not enter personal information.")

        elif score >= 2:
            st.warning("Be careful. Verify the website address before proceeding.")

        else:
            st.info(
                "No major warning signs detected. Still verify the website "
                "before entering sensitive information."
            )

    else:
        st.warning("Please enter a URL first.")
