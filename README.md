# Text-to-SQL Streamlit App

## Overview
This project is a Text-to-SQL application built using Streamlit that allows users to interact with their database files through natural language queries. By leveraging the Gemini API, the app translates user prompts into SQL queries and provides both the results and the corresponding SQL code.

## Features
- **Upload Database File**: Users can upload their database files in SQLite format.
- **Natural Language Queries**: Users can input prompts in plain English to specify the data they want to fetch from the database.
- **SQL Query Generation**: The app generates the SQL query corresponding to the user's prompt.
- **Result Display**: The app displays the results fetched from the database based on the generated SQL query.

## Requirements
- Python 3.8 or higher
- Streamlit
- Gemini API access

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/texttosql-streamlit-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd texttosql-streamlit-app
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app2.py
    ```
2. Upload your SQLite database file when prompted.
3. Enter a natural language query in the text box.
4. The app will display the corresponding SQL query and the results fetched from the database.

## File Structure

- `app2.py`: Contains the core functionality of the application, including handling user inputs, interacting with the Gemini API, generating SQL queries, and displaying results.
- `requirements.txt`: Lists the Python packages required to run the application. This includes:
  - `streamlit`
  - `requests`
  - `pandas`
  - `sqlite3` (if not built-in)
  - Any other dependencies necessary for the Gemini API integration
- `README.md`: This file, providing an overview and instructions for the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.



