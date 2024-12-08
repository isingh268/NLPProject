# -*- coding: utf-8 -*-
"""SCU Scholarship Finder"""

import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_calendar import calendar

# Configure the page
st.set_page_config(
    page_title="SCU Scholarship Finder",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Scholarship data
data = {
    "Scholarship Name": [
        "🎓 Kuru Footsteps to Your Future Scholarship",
        "💡 Alert1 Students for Seniors Scholarship",
        "⭐ Blankstyle Scholarship Opportunity #1",
        "🚀 Innovation In Education Scholarship",
        "📘 The Bert & Phyllis Lamb Prize in Political Science",
        "🌍 New Beginnings Immigrant Scholarship",
    ],
    "Date Due": [
        "2024-12-20",
        "2025-01-10",
        "2024-12-31",
        "2024-10-15",
        "2025-02-14",
        "2024-10-18",
    ],
    "Summary": [
        "This scholarship awards $1,000 to high school seniors or college students pursuing their academic goals. To apply: Prepare a personal statement highlighting your ambitions and submit your application by December 20, 2024.",
        "A $500 award for students committed to improving senior care. Action: Write a 300-word essay about your aspirations in this field. Submit your application by January 10, 2025.",
        "A $1,000 bi-annual scholarship to support college expenses. Actionable Steps: Share your accomplishments and explain how this scholarship will help you achieve your goals. Deadline: December 31, 2024.",
        "This $500 scholarship recognizes students with innovative projects that benefit their community. Action: Describe your project in detail and submit supporting documentation by October 15, 2024.",
        "The Bert & Phyllis Lamb Prize honors excellence in Political Science. Action: Submit a well-researched paper (up to 6,000 words) and an abstract by February 14, 2025.",
        "This scholarship supports first-generation immigrant students. Action: Write an essay about your immigrant experience and career aspirations. Deadline: October 18, 2024.",
    ],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)
df["Date Due"] = pd.to_datetime(df["Date Due"])

# Sidebar navigation
st.sidebar.title("📚 Navigation")
nav_option = st.sidebar.radio("Go to:", ["🏠 Home", "🎓 Find Scholarships", "📅 Calendar View", "ℹ️ About"])

# Home Page
if nav_option == "🏠 Home":
    st.title("🎓 Welcome to SCU Scholarship Finder!")
    st.subheader("Hello!👋")
    st.markdown("""
    **Discover scholarships tailored for Santa Clara University students.**
    Use this platform to explore funding opportunities, get personalized recommendations, and plan for upcoming deadlines.
    """)
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    - [SCU Financial Aid Office](https://www.scu.edu/financialaid/)
    - [SCU Financial Aid Deadlines](hhttps://www.scu.edu/financialaid/deadlines/)
    - [SCU Career Center](https://www.scu.edu/careercenter/)
    """)
    st.markdown("### 💡 Scholarship Tips")
    st.markdown("""
    - **Start Early**: Begin your search and application process well in advance of deadlines.
    - **Tailor Your Applications**: Customize essays and responses to match each scholarship's requirements.
    - **Leverage SCU Resources**: Reach out to the financial aid office or academic advisors for guidance.
    """)
    st.balloons()

# Scholarship Finder Page
elif nav_option == "🎓 Find Scholarships":
    st.header("🎓 Find Scholarships")
    st.subheader("📚 SCU Student Information")
    scu_id = st.text_input("Enter your SCU Student ID:")
    scu_email = st.text_input("Enter your SCU Email Address:")
    major = st.selectbox("Select your academic major:", [
        "Computer Science", "Business Analytics", "Engineering", "Psychology", "Biology", "Undeclared", "Other"
    ])
    school_year = st.selectbox("Select your school year:", [
        "Freshman", "Sophomore", "Junior", "Senior", "Graduate Student", "Alumni"
    ])
    department = st.selectbox("Select your department:", [
        "Arts and Sciences", "Business", "Engineering", "Other"
    ])
    gpa = st.slider("Enter your GPA:", 0.0, 4.0, 3.0, step=0.1)
    honors = st.selectbox("Are you a member of the Honors Program?", ["Yes", "No"])
    financial_need = st.selectbox("Do you require need-based financial aid?", ["Yes", "No"])
    FAFSA_filed = st.selectbox("Have you filed your FAFSA for this year?", ["Yes", "No"])
    residency = st.selectbox("What is your residency status?", [
        "California Resident", "Out-of-State", "International Student"
    ])
    scholarship_type = st.multiselect(
        "Select scholarship types you are interested in:", [
            "Merit-Based", "Need-Based", "Graduate Assistantships",
            "Diversity Scholarships", "Department-Specific Aid", "SCU-Sponsored Scholarships"
        ]
    )
    causes = st.multiselect(
        "Select causes or values important to you:", [
            "Sustainability", "Community Service", "Diversity", "Social Justice", "STEM", "Arts"
        ]
    )
    if st.button("🔍 Find Scholarships"):
        st.success("Scholarships matching your preferences will be displayed here!")

# Calendar View Page
elif nav_option == "📅 Calendar View":
    st.title("📅 Scholarship Calendar")

    # Split the layout into two columns
    col1, col2 = st.columns([2, 1])

    # State to track the currently displayed month and year
    if "current_month" not in st.session_state:
        st.session_state.current_month = datetime.now().month
    if "current_year" not in st.session_state:
        st.session_state.current_year = datetime.now().year

    # Prepare calendar events
    events = {}
    for _, row in df.iterrows():
        event_date = row["Date Due"].strftime("%Y-%m-%d")
        if event_date not in events:
            events[event_date] = []
        events[event_date].append(row["Scholarship Name"])

    # Combine events for display
    events = {date: "\n".join(scholarships) for date, scholarships in events.items()}

    # Render calendar in the left column
    with col1:
        st.subheader("📆 Calendar")
        selected_event = calendar(events)

        if selected_event and "currentStart" in selected_event:
            new_start_date = selected_event["currentStart"].split("T")[0]
            new_start_datetime = pd.Timestamp(new_start_date)
            st.session_state.current_month = new_start_datetime.month
            st.session_state.current_year = new_start_datetime.year

    # Display all scholarships in the right column
    with col2:
        st.subheader("📋 All Scholarships")
        for _, row in df.iterrows():
            st.markdown(
                f"**{row['Scholarship Name']}**  \n"
                f"🗓 **Due Date**: {row['Date Due'].strftime('%B %d, %Y')}"
            )

    # Show detailed summary for selected date
    st.subheader("🎯 Selected Date Details")
    if selected_event and "dateClick" in selected_event:
        selected_date = selected_event["dateClick"]["date"].split("T")[0]
        selected_scholarships = df[df["Date Due"] == pd.Timestamp(selected_date)]
        if not selected_scholarships.empty:
            for _, row in selected_scholarships.iterrows():
                st.markdown(
                    f"""
                    ### {row['Scholarship Name']}
                    - **Due Date**: {row['Date Due'].strftime('%B %d, %Y')}
                    - **Details**: {row['Summary']}
                    """
                )
        else:
            st.write(f"No scholarships due on {selected_date}.")
    else:
        st.write("Click on a date in the calendar to view details.")

# About Page
elif nav_option == "ℹ️ About":
    st.header("ℹ️ About This App")
    st.markdown("""
    **SCU Scholarship Finder** is designed to assist Santa Clara University students in finding and applying for scholarships.

    ### Features:
    - Explore SCU-specific scholarships.
    - View calendar with scholarship due dates and details.
    - Receive tailored recommendations based on your profile.

    Built with ❤️ for SCU students.
    """)
    st.markdown("[Visit SCU Financial Aid Office](https://www.scu.edu/financialaid/)")
