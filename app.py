import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Student Grade Analyzer", layout="wide")

# Sidebar Navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Grade Input", "Grade Analysis", "Feedback", "About"])

st.sidebar.divider()

# Sidebar settings
st.sidebar.subheader("Settings")
show_chart = st.sidebar.checkbox("Show Charts", True)
grading_scale = st.sidebar.selectbox(
    "Grading Scale",
    ["Standard (90=A)", "Lenient (85=A)", "Strict (95=A)"]
)

st.sidebar.slider("Study Hours Goal", 1, 10, 4)

# ------------------ HOME PAGE ------------------

if page == "Home":
    st.title("🎓 Student Grade Analyzer")

    st.header("Student Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")
        student_id = st.text_input("Student ID")

    with col2:
        course = st.selectbox("Course", ["BSIT", "BSCS", "Engineering", "Business"])
        year_level = st.radio("Year Level", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

    st.success("Student profile loaded.")

# ------------------ GRADE INPUT PAGE ------------------

elif page == "Grade Input":

    st.title("📝 Enter Subject Grades")

    subject1 = st.number_input("Math Grade", 0, 100)
    subject2 = st.number_input("Programming Grade", 0, 100)
    subject3 = st.number_input("Database Grade", 0, 100)
    subject4 = st.number_input("Networking Grade", 0, 100)
    subject5 = st.number_input("Systems Analysis Grade", 0, 100)

    study_hours = st.slider("Weekly Study Hours", 0, 40)

    focus = st.select_slider(
        "Focus Level",
        options=["Low", "Medium", "High"]
    )

    notes = st.text_area("Notes about performance")

    uploaded = st.file_uploader("Upload grade sheet (optional)")

    if st.button("Save Grades"):
        st.success("Grades saved successfully!")

# ------------------ GRADE ANALYSIS PAGE ------------------

elif page == "Grade Analysis":

    st.title("📈 Grade Analysis")

    grades = {
        "Math": 85,
        "Programming": 92,
        "Database": 88,
        "Networking": 79,
        "Systems Analysis": 90
    }

    df = pd.DataFrame(list(grades.items()), columns=["Subject", "Grade"])

    st.subheader("Grade Table")
    st.dataframe(df)

    average = np.mean(df["Grade"])

    st.metric("Average Grade", round(average,2))

    if average >= 90:
        st.success("Excellent Performance 🎉")
    elif average >= 75:
        st.info("Good Performance 👍")
    else:
        st.warning("Needs Improvement ⚠")

    if show_chart:
        st.subheader("Grade Chart")
        st.bar_chart(df.set_index("Subject"))

# ------------------ FEEDBACK PAGE ------------------

elif page == "Feedback":

    st.title("💬 App Feedback")

    rating = st.slider("Rate this app", 1, 5)

    recommendation = st.radio(
        "Would you recommend this app?",
        ["Yes", "Maybe", "No"]
    )

    comment = st.text_area("Your feedback")

    if st.button("Submit Feedback"):
        st.balloons()
        st.success("Thank you for your feedback!")

# ------------------ ABOUT PAGE ------------------

elif page == "About":

    st.title("ℹ About This App")

    st.write("""
### What the App Does
The Student Grade Analyzer allows students to input their subject grades and view a quick analysis of their academic performance.

### Target Users
- College students
- Teachers monitoring student progress
- Academic advisors

### Inputs Collected
- Student name and ID
- Course and year level
- Subject grades
- Study hours and focus level
- Optional uploaded grade sheet
- User feedback

### Output Displayed
- Grade table
- Average grade calculation
- Performance evaluation
- Visual grade chart
""")
