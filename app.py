import streamlit as st
import requests


BASE_URL = st.secrets["BASE_URL"]

def get_insights():
    res = requests.get(f"{BASE_URL}/aylien-tech-insights")
    res.raise_for_status()
    return res.json()["insights"]


st.title("Tech Insights")

insights = get_insights()

for insight in insights:
    st.markdown(
        f"### {insight['trigger']}\n"
        f"**Source**: {insight['source_name']}\n\n"
        f"**Trigger**: {insight['trigger']}\n\n"
        f"**Timestamp**: {insight['timestamp']}\n\n{insight['insight']}"
    )
