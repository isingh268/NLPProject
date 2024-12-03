# -*- coding: utf-8 -*-
"""SCU Scholarship Finder"""

import streamlit as st
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="SCU Scholarship Finder",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("📚 Navigation")
nav_option = st.sidebar.radio("Go to:", ["🏠 Home", "🎓 Find Scholarships", "📊 Statistics", "ℹ️ About"])

# Home Page
if nav_option == "🏠 Home":
    st.title("🎓 Welcome to SCU Scholarship Finder!")
    
    # Personalized greeting based on time of day
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning!"
    elif current_hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    st.subheader(f"{greeting} 👋")

    # Introductory Text
    st.markdown("""
    **Discover scholarships tailored for Santa Clara University students.**  
    Use this platform to explore funding opportunities, get personalized recommendations, and plan for upcoming deadlines.
    """)

    # Quick Links Section
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    - [SCU Financial Aid Office](https://www.scu.edu/financial-aid/)
    - [Scholarship Application Tips](https://www.scholarships.com/resources/tips-for-applying/)
    - [SCU Career Center](https://www.scu.edu/careercenter/)
    """)

    # Scholarship Tips Section
    st.markdown("### 💡 Scholarship Tips")
    st.markdown("""
    - **Start Early**: Begin your search and application process well in advance of deadlines.
    - **Tailor Your Applications**: Customize essays and responses to match each scholarship's requirements.
    - **Leverage SCU Resources**: Reach out to the financial aid office or academic advisors for guidance.
    """)

    # Upcoming Deadlines
    st.markdown("### 📅 Upcoming Deadlines")
    st.markdown("""
    - **SCU Merit Scholarship**: December 15, 2024  
    - **Diversity in Tech Award**: December 20, 2024  
    - **Graduate Assistantship Grant**: January 10, 2025  
    """)

    # FAQs Section
    st.markdown("### ❓ FAQs")
    st.markdown("""
    - **Who can apply for scholarships?**  
      Most scholarships are available to SCU students who meet specific criteria, such as academic performance or financial need.
    - **Do I need to file FAFSA?**  
      Filing FAFSA is required for need-based scholarships and federal aid.
    - **Where can I get help with my application?**  
      Visit the [SCU Financial Aid Office](https://www.scu.edu/financial-aid/) or contact your academic advisor.
    """)

    st.balloons()

# Scholarship Finder Page
elif nav_option == "🎓 Find Scholarships":
    st.header("🎓 Find Scholarships")

    # SCU Student Information
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

    # Academic Performance
    st.subheader("📊 Academic Information")
    gpa = st.slider("Enter your GPA:", 0.0, 4.0, 3.0, step=0.1)
    honors = st.selectbox("Are you a member of the Honors Program?", ["Yes", "No"])

    # Financial Information
    st.subheader("💵 Financial Information")
    financial_need = st.selectbox("Do you require need-based financial aid?", ["Yes", "No"])
    FAFSA_filed = st.selectbox("Have you filed your FAFSA for this year?", ["Yes", "No"])
    residency = st.selectbox("What is your residency status?", [
        "California Resident", "Out-of-State", "International Student"
    ])

    # Scholarship Preferences
    st.subheader("🎯 Preferences")
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

    # Submit and Display Results
    if st.button("🔍 Find Scholarships"):
        st.success("Scholarships matching your preferences will be displayed here!")
        # Placeholder for scholarship results
        st.markdown("""
        **Example Scholarships:**
        - **SCU Merit Scholarship**: $5,000 (Deadline: 2024-12-15)
        - **Diversity in Tech Award**: $3,000 (Deadline: 2024-12-20)
        - **Graduate Assistantship Grant**: $10,000 (Deadline: 2024-12-10)
        """)

# Statistics Page
elif nav_option == "📊 Statistics":
    st.header("📊 Scholarship Statistics")
    st.markdown("Explore trends and insights related to SCU scholarships.")

    # Placeholder for simple text-based statistics
    st.markdown("""
    - **Merit-Based Scholarships**: 30% of total scholarships.
    - **Need-Based Scholarships**: 20%.
    - **Diversity Scholarships**: 15%.
    - **Graduate Aid**: 10%.
    """)

# About Page
elif nav_option == "ℹ️ About":
    st.header("ℹ️ About This App")
    st.markdown("""
    **SCU Scholarship Finder** is designed to assist Santa Clara University students in finding and applying for scholarships.

    ### Features:
    - Explore SCU-specific scholarships.
    - View simple statistics on funding opportunities.
    - Receive tailored recommendations based on your profile.

    Built with ❤️ for SCU students.
    """)
    st.markdown("[Visit SCU Financial Aid Office](https://www.scu.edu/financial-aid/)")
