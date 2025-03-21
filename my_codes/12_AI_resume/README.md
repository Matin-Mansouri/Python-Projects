# Resume Parser and Reviewer

ResumeAI is an advanced tool that leverages the power of Large Language Models (LLMs) to analyze and improve resumes. This project allows users to upload their resumes in PDF format, parse the content, and receive suggestions for improvements based on a provided job description.

## Features

- **Resume Parsing**: Extracts text from PDF resumes and converts it into a structured YAML format.
- **Resume Reviewing**: Analyzes the resume content and provides suggestions for improvements.
- **Job Description Alignment**: Reviews the resume against a provided job description and suggests modifications to better align with the job requirements.
- **Streamlit Interface**: User-friendly web interface for uploading resumes, entering job descriptions, and viewing analysis results.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload your resume in PDF format and optionally enter a job description.

4. Click the "Run Analysis" button to parse and review your resume.

5. Navigate through the sections of your resume to view the original and revised content along with suggestions for improvements.

## Project Structure

- `app.py`: Main application file for the Streamlit interface.
- `resume_formatter.py`: Functions for formatting resume sections into Markdown.
- `src/constants.py`: Contains example job descriptions.
- `src/prompts.py`: Prompts used for interacting with the LLM.
- `src/utils/pdf.py`: Utility functions for extracting text from PDF files.
- `src/utils/llm.py`: Functions for calling the LLM to parse and review resumes.
- `src/utils/yaml.py`: Utility functions for extracting YAML content from text.
- `src/utils/helpers.py`: Helper functions for formatting values and converting schema to Markdown.

## Requirements

- Python 3.10+
- Streamlit 1.38.0
- OpenAI 1.13.4
- PyPDF2 3.0.1
- PyYAML 6.0.2

## License

This project is licensed under the MIT License.