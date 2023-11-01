import streamlit as st
import requests


def get_insights():
    res = requests.get("https://cre-hawk-model-5mpzwxcytq-uc.a.run.app/aylien-tech-insights")
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
