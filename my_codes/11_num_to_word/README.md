# Num to Word

## Overview

The "Num to Word" project is a Python-based application that converts numerical values into their corresponding English words. This can be particularly useful for applications such as writing checks, generating invoices, or any other scenario where numbers need to be represented in word form.

## Goal

The goal of this project was to practice and demonstrate the use of recursion in solving problems.

## Features

- Converts numbers from 0 to billions into English words.
- Handles special cases for numbers under 20 and multiples of ten.
- Supports large numbers by breaking them down into manageable chunks.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Matin-Mansouri/Python-Projects/tree/main/my_codes.git
    ```
2. Navigate to the project directory:
    ```sh
    cd num_to_word
    ```
3. (Optional) Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

To use the "Num to Word" converter, you can run the main script and input the number you wish to convert:

```sh
python main.py
```

You will be prompted to enter a number, and the script will output the corresponding English words.

## Example

```sh
Enter a number: 12345
Output: Twelve Thousand Three Hundred Forty-Five
```

## Project Structure

```
num_to_word/
│
├── src/
│   ├── main.py          # Main script to run the converter
│   ├── constants.py     # Constants used for conversion
│   └── converter.py     # Conversion logic
│
├── tests/
│   └── test_converter.py # Unit tests for the converter
│
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by various number-to-word conversion algorithms available online.
- Special thanks to the Python community for their valuable resources and support.
