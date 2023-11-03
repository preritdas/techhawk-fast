import streamlit as st
import requests


BASE_URL = st.secrets["BASE_URL"]

def get_insights(category: str):
    res = requests.get(f"{BASE_URL}/techcrunch-startup-insights/{category}")
    res.raise_for_status()
    return res.json()["insights"]


st.title("TechCrunch Insights")
st.info("Choose a category from the sidebar.")

with st.sidebar:
    category = st.radio(
        label="Choose a category.",
        options=(
            "startups",
            "venture",
            "security",
            "artificial-intelligence",
            "apps"
        )
    )

insights = get_insights(category)

for insight in insights:
    st.markdown(
        f"### {insight['trigger']}\n"
        f"**Source**: {insight['source_name']}\n\n"
        f"**Trigger**: {insight['trigger']}\n\n"
        f"**Timestamp**: {insight['timestamp']}\n\n{insight['insight']}"
    )
