# Python Password Generator - Functional Approach

Welcome to the Python Password Generator project - Functional Programming approach! This program generates three types of passwords using functional programming constructs such as functions, instead of classes (Object-Oriented Programming).

The password generator creates:

1. Random Passwords
2. Memorable Passwords
3. Pin Codes

## How It Works

The password generator uses Python's `random` and `string` modules to generate passwords based on user preferences. The generator consists of three distinct functions, each representing a different type of password generation:

1. `generate_random_password` creates a random password with specified length, and includes numbers and/or special characters based on your preference.
2. `generate_memorable_password` generates a password composed of a number of random words selected from an English language corpus. You can specify the separator and whether the words should be capitalized.
3. `generate_pin` produces a numeric pin code of a specified length.

## Requirements

- Python 3.7+

That's all you need to know to get started with this project. Enjoy generating passwords!

## Testing

The `main.py` file includes test cases for each function, which print out a test password for each made by each function, and run checks to ensure the password meets the expected format.

## User Inputs

By editing the values in the main function, you can specify the length of the password for each type of password to generate. You can also decide whether to include numbers or symbols for the random password generator, or the number of words and if words should be capitalized for the memorable password generator. 