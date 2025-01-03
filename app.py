import streamlit as st
import PyPDF2
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
    

def analyze_resume(resume_text, job_keywords):
    resume_text = resume_text.lower()
    job_keywords = job_keywords.lower().split(",") 
    
    keyword_matches = [keyword for keyword in job_keywords if keyword in resume_text]
    
    
    match_percentage = (len(keyword_matches) / len(job_keywords)) * 100
    return keyword_matches, match_percentage


def recommend_courses(skills):
    course_data = {
        "Data Science": ["Python", "Machine Learning", "Data Analysis"],
        "Web Development": ["HTML", "CSS", "JavaScript", "React"],
        "Machine Learning": ["Python", "TensorFlow", "AI", "Data Science"],
    }

    recommended_courses = []

    for course, required_skills in course_data.items():
        if any(skill in skills for skill in required_skills):
            recommended_courses.append(course)

    return recommended_courses


def run():
    st.title("AI-Powered Resume Analyzer")

    
    uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
    
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.write("Extracted Text from Resume:")
        st.write(resume_text[:1000])  

        job_keywords = st.text_input("Enter job-related keywords (comma-separated)", "Python, Machine Learning, Data Science")
        
        if job_keywords:
            
            keyword_matches = analyze_resume(resume_text, job_keywords)
            st.write("Keyword Matches Found:")
            st.write(keyword_matches)

            skills = st.text_input("Enter your skills (comma-separated)", "Python, Machine Learning, Data Analysis")
            if skills:
                recommended_courses = recommend_courses(skills)
                st.write("Recommended Courses Based on Skills:")
                st.write(recommended_courses)

        if job_keywords:
            keyword_matches, match_percentage = analyze_resume(resume_text, job_keywords)
            st.write("Keyword Matches Found:")
            st.write(keyword_matches)

          
            st.write(f"Match Percentage: {match_percentage:.2f}%")

if __name__ == "__main__":
    run()
