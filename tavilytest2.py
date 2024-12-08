import streamlit as st
import pandas as pd
from datetime import datetime
from transformers import pipeline

# Configure the page
st.set_page_config(
    page_title="Scholarship Finder",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Transformers Pipelines
@st.cache_resource
def load_transformers():
    text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return text_generator, summarizer

text_generator, summarizer = load_transformers()

# Scholarship Data
data = {
    "Scholarship Name": ["Kuru Scholarship", "Alert1 Seniors Scholarship", "Blankstyle Opportunity"],
    "Date Due": ["2024-12-20", "2025-01-10", "2024-12-31"],
    "Summary": [
        "Awards $1,000 to high school seniors or college students.",
        "Provides $500 for students committed to senior care.",
        "A $1,000 scholarship to support college expenses.",
    ],
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Date Due"] = pd.to_datetime(df["Date Due"])

# Sidebar Navigation
st.sidebar.title("📚 Navigation")
nav_option = st.sidebar.radio("Go to:", ["🏠 Home", "🎓 Find Scholarships", "📅 Calendar View", "ℹ️ About"])

# Home Page
if nav_option == "🏠 Home":
    st.title("🎓 Welcome to Scholarship Finder!")
    st.write("Use this tool to find scholarships tailored to your profile.")

# Scholarship Finder
elif nav_option == "🎓 Find Scholarships":
    st.header("🎓 Find Scholarships")
    name = st.text_input("Name")
    gpa = st.slider("GPA", 0.0, 4.0, 3.0, step=0.1)
    major = st.text_input("Major")
    causes = st.multiselect("Causes", ["Community Service", "Diversity", "STEM", "Arts"])

    if st.button("Find Scholarships"):
        prompt = (
            f"Student: {name}, GPA: {gpa}, Major: {major}, Causes: {', '.join(causes)}.\n"
            f"Recommend scholarships and explain why they are a good fit."
        )
        with st.spinner("Generating recommendations..."):
            response = text_generator(prompt, max_length=200, num_return_sequences=1)
        st.success("Recommendations:")
        st.write(response[0]["generated_text"])

# Calendar View
elif nav_option == "📅 Calendar View":
    st.header("📅 Scholarship Calendar")
    for _, row in df.iterrows():
        st.write(f"{row['Scholarship Name']} - Due: {row['Date Due']}")

# About Page
elif nav_option == "ℹ️ About":
    st.title("ℹ️ About")
    st.write("Scholarship Finder helps students find funding for their education.")
