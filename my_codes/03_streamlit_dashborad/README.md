# Password Generator Dashboard

## Project Overview
The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. It allows users to generate different types of passwords quickly, either randomly, as a memorable sequence of words, or as a pin code, based on their preferences.

## Project Structure
The project has the following structure:

- `src/password_generator.py`: A Python module containing the password generator classes; `RandomPasswordGenerator`, `MemorablePasswordGenerator`, and `PinCodeGenerator`.
- `src/app.py`: A Python script using Streamlit to create a web app interface for the password generators.
- `README.md`: Documentation for the project solution. You are currently reading this!

## Getting Started

Follow the instructions below to set up this project on your local machine.

### Prerequisites

- Python 3.6 or later
- Streamlit
- NLTK (Natural Language Toolkit)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies using the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the 'words' corpus for NLTK:
    ```python
    import nltk
    nltk.download('words')
    ```

## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```sh
streamlit run src/app.py
```

This will open a web page in your default browser running on your localhost.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [NLTK](https://www.nltk.org/)