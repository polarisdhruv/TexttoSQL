

import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and provide SQL query as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query results from the SQL database
def read_sql_query(sql, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define the prompt for the AI model
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    For any database that is uploaded you need to answer with the sql query that should be used and with the answer also
    Question can be about anything that can be solved using sql query.

    Incase the user ask something unrelated , answer accordingly as you usually answer.
    
    For example:
    - Example 1: "How many entries of records are present?", the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    - Example 2: "Tell me all the students studying in Data Science class?", the SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    
    The SQL code should not have ``` at the beginning or end and should not include the word "sql".
    """
]

# Streamlit App
st.set_page_config(page_title="Retrieve SQL Data with AI", layout = 'wide' ,initial_sidebar_state= 'collapsed' )






st.header("Gemini App to Retrieve SQL Data")

# File uploader for the database
uploaded_file = st.file_uploader("Upload your SQLite database", type="db")

# Text input for the SQL task
question = st.text_input("Enter your SQL task:", key="input")

# Button to submit the query
submit = st.button("Ask the question")

# If submit is clicked and a file is uploaded
if submit and uploaded_file:
    # Save the uploaded file to a temporary location
    db_path = "uploaded_db.db"
    with open(db_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Generate the SQL query using the AI model
    response = get_gemini_response(question, prompt)
    st.write("Generated SQL query:")
    st.code(response, language='sql')

    # Execute the SQL query on the uploaded database
    try:
        data = read_sql_query(response, db_path)
        st.subheader("Query Results:")
        for row in data:
            st.write(row)
    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Clean up the temporary database file
    os.remove(db_path)
elif submit:
    st.error("Please upload a database file.")


