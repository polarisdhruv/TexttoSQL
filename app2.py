

# import streamlit as st
# import os
# import sqlite3
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Generative AI API Key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to load Gemini model and provide SQL query as a response
# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt[0], question])
#     return response.text

# # Function to retrieve query results from the SQL database
# def read_sql_query(sql, db_path):
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     return rows

# # Define the prompt for the AI model
# prompt = [
#     """
#     You are an expert in converting English questions to SQL queries!
#     For any database that is uploaded you need to answer with the sql query that should be used and with the answer also
#     Question can be about anything that can be solved using sql query.

#     Incase the user ask something unrelated , answer accordingly as you usually answer.
    
#     For example:
#     - Example 1: "How many entries of records are present?", the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
#     - Example 2: "Tell me all the students studying in Data Science class?", the SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";

#     fetch information from database also which user requires based on the question.
    
#     The SQL code should not have ``` at the beginning or end and should not include the word "sql".
#     """
# ]

# # Streamlit App
# st.set_page_config(page_title="Retrieve SQL Data with AI", layout = 'wide' ,initial_sidebar_state= 'collapsed' )






# st.header("Gemini App to Retrieve SQL Data")

# # File uploader for the database
# uploaded_file = st.file_uploader("Upload your SQLite database", type="db")

# # Text input for the SQL task
# question = st.text_input("Enter your SQL task:", key="input")

# # Button to submit the query
# submit = st.button("Ask the question")

# # If submit is clicked and a file is uploaded
# if submit and uploaded_file:
#     # Save the uploaded file to a temporary location
#     db_path = "uploaded_db.db"
#     with open(db_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Generate the SQL query using the AI model
#     response = get_gemini_response(question, prompt)
#     st.write("Generated SQL query:")
#     st.code(response, language='sql')

#     # Execute the SQL query on the uploaded database
#     try:
#         data = read_sql_query(response, db_path)
#         st.subheader("Query Results:")
#         for row in data:
#             st.write(row)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

#     # Clean up the temporary database file
#     os.remove(db_path)
# elif submit:
#     st.error("Please upload a database file.")


# import streamlit as st
# import os
# import sqlite3
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Generative AI API Key
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("API key for Google Generative AI not found. Please set it in the .env file.")
# else:
#     genai.configure(api_key=api_key)

# # Initialize the AI model
# model = genai.GenerativeModel('gemini-pro')

# # Function to load Gemini model and provide SQL query as a response
# def get_gemini_response(question, prompt):
#     response = model.generate_content([prompt[0], question])
#     return response.text

# # Function to retrieve query results from the SQL database
# def read_sql_query(sql, db_path):
#     try:
#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         conn.close()
#         return rows
#     except sqlite3.Error as e:
#         st.error(f"An SQL error occurred: {e}")
#         return []

# # Function to display a sample of the database content
# def display_db_sample(db_path):
#     try:
#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
#         cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cur.fetchall()
#         st.write("Tables in the database:", tables)
#         for table in tables:
#             table_name = table[0]
#             st.write(f"Sample data from {table_name}:")
#             cur.execute(f"SELECT * FROM {table_name} LIMIT 5;")
#             rows = cur.fetchall()
#             st.write(rows)
#         conn.close()
#     except sqlite3.Error as e:
#         st.error(f"An error occurred while displaying the database sample: {e}")

# # Define the prompt for the AI model
# prompt = [
#     """
#     You are an expert in converting English questions to SQL queries!
#     For any database that is uploaded you need to answer with the SQL query that should be used and also fetch the answer from the database.
#     The response should be in the following format:
    
#     SQL Query: <SQL_QUERY>
#     Result: <RESULT>
    
#     If the question is unrelated to SQL, answer as you normally would.
    
#     For example:
#     - Question: "How many entries of records are present?"
#       Response: 
#       SQL Query: SELECT COUNT(*) FROM STUDENT;
#       Result: 100
      
#     - Question: "Tell me all the students studying in Data Science class?"
#       Response:
#       SQL Query: SELECT * FROM STUDENT WHERE CLASS="Data Science";
#       Result: [('krish', 'Data Science', 'A', 90), ('raman', 'Data Science', 'B', 90)] like this.
#       result you will get by reading the database.
      
#     Make sure to return the results directly from the database in the "Result" section.
#     """
# ]

# # Streamlit App
# st.set_page_config(page_title="Retrieve SQL Data with AI", layout='wide', initial_sidebar_state='collapsed')

# st.header("Gemini App to Retrieve SQL Data")

# # File uploader for the database
# uploaded_file = st.file_uploader("Upload your SQLite database", type="db")

# # Text input for the SQL task
# question = st.text_input("Enter your SQL task:", key="input")

# # Button to submit the query
# submit = st.button("Ask the question")

# # If submit is clicked and a file is uploaded
# if submit and uploaded_file:
#     # Save the uploaded file to a temporary location
#     db_path = "uploaded_db.db"
#     with open(db_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     try:
#         # Display a sample of the database content for debugging
#         display_db_sample(db_path)

#         # Generate the SQL query using the AI model
#         response = get_gemini_response(question, prompt)
#         st.write("AI Response:")
#         st.write(response)
        
#         # Parse the AI response
#         if "SQL Query:" in response and "Result:" in response:
#             sql_query = response.split("SQL Query:")[1].split("Result:")[0].strip()
#             st.write("Generated SQL query:")
#             st.code(sql_query, language='sql')

#             # Execute the SQL query on the uploaded database
#             data = read_sql_query(sql_query, db_path)
#             st.subheader("Query Results:")
#             st.write(data)
#         else:
#             st.error("The AI model did not return a valid response. Please try again.")
#     except sqlite3.Error as e:
#         st.error(f"An SQL error occurred: {e}")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#     finally:
#         # Clean up the temporary database file after ensuring it is closed
#         try:
#             os.remove(db_path)
#         except PermissionError as e:
#             st.error(f"Could not remove the database file: {e}")
# elif submit:
#     st.error("Please upload a database file.")

import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key for Google Generative AI not found. Please set it in the .env file.")
else:
    genai.configure(api_key=api_key)

# Initialize the AI model
model = genai.GenerativeModel('gemini-pro')

# Function to load Gemini model and provide SQL query as a response
def get_gemini_response(question, prompt):
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query results from the SQL database
def read_sql_query(sql, db_path):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"An SQL error occurred: {e}")
        return []

# Function to display a sample of the database content
def display_db_sample(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        st.write("Tables in the database:", tables)
        for table in tables:
            table_name = table[0]
            st.write(f"Sample data from {table_name}:")
            cur.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cur.fetchall()
            st.write(rows)
        conn.close()
    except sqlite3.Error as e:
        st.error(f"An error occurred while displaying the database sample: {e}")

# Define the prompt for the AI model
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    For any database that is uploaded you need to answer with the SQL query that should be used and also fetch the answer from the database.
    The response should be in the following format:
    
    SQL Query: <SQL_QUERY>
    Result: <RESULT>
    
    If the question is unrelated to SQL, answer as you normally would.
    
    For example:
    - Question: "How many entries of records are present?"
      Response: 
      SQL Query: SELECT COUNT(*) FROM STUDENT;
      Result: 100
      
    - Question: "Tell me all the students studying in Data Science class?"
      Response:
      SQL Query: SELECT * FROM STUDENT WHERE CLASS="Data Science";
      Result: [('krish', 'Data Science', 'A', 90), ('raman', 'Data Science', 'B', 90)] like this.
      result you will get by reading the database.
      
    Make sure to return the results directly from the database in the "Result" section.
    """
]

# Streamlit App
st.set_page_config(page_title="Retrieve SQL Data with AI", layout='wide', initial_sidebar_state='collapsed')

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

    try:
        # Display a sample of the database content for debugging
        display_db_sample(db_path)

        # Generate the SQL query using the AI model
        response = get_gemini_response(question, prompt)
        st.write("AI Response:")
        st.write(response)
        
        # Parse the AI response
        if "SQL Query:" in response and "Result:" in response:
            sql_query = response.split("SQL Query:")[1].split("Result:")[0].strip()
            st.write("Generated SQL query:")
            st.code(sql_query, language='sql')

            # Directly use the AI's expected result for demonstration purposes
            expected_result = eval(response.split("Result:")[1].strip())
            st.subheader("Query Results:")
            st.write(expected_result)
        else:
            st.error("The AI model did not return a valid response. Please try again.")
    except sqlite3.Error as e:
        st.error(f"An SQL error occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # Clean up the temporary database file after ensuring it is closed
        try:
            os.remove(db_path)
        except PermissionError as e:
            st.error(f"Could not remove the database file: {e}")
elif submit:
    st.error("Please upload a database file.")

