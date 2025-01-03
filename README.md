# AI_Resume_Analyser

This project is an AI-driven resume analysis tool built with Python and Streamlit. The objective is to help job seekers match their resumes with specific job roles and recommend relevant courses to enhance their skills.

## Key Features:
- Resume Text Extraction: Uses `PyPDF2` to extract text from uploaded PDF resumes.
- Job Keyword Matching: Matches resume content with specific job-related keywords (e.g., skills, experience, qualifications) for evaluating relevance.
- Course Recommendations: Suggests relevant online courses based on skills identified in the resume to help users improve their profile.
- Cosine Similarity Scoring: Utilizes the cosine similarity method to match resume content with a job description and evaluate the degree of match.
  
## Technologies Used:
- Python: Primary programming language used for the backend logic.
- Streamlit: Framework for creating the interactive user interface.
- PyPDF2: For reading and extracting text from PDF resumes.
- scikit-learn: Used for text vectorization and cosine similarity calculation for keyword matching.
- pandas: For handling data and processing job-related keywords.

## Future Enhancements:
- Integrate a more advanced machine learning model for enhanced resume-job matching.
- Add support for other file formats like DOCX and TXT.
- Improve course recommendation using real-time data from online learning platforms like Coursera and Udemy.

