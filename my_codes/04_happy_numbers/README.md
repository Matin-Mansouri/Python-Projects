# Happy Number Project

This project contains a Python script to determine if a given number is a happy number.

## What is a Happy Number?

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits in base-ten, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy numbers.

## Example

- 19 is a happy number:
  - 1² + 9² = 1 + 81 = 82
  - 8² + 2² = 64 + 4 = 68
  - 6² + 8² = 36 + 64 = 100
  - 1² + 0² + 0² = 1

- 2 is not a happy number:
  - 2² = 4
  - 4² = 16
  - 1² + 6² = 1 + 36 = 37
  - 3² + 7² = 9 + 49 = 58
  - 5² + 8² = 25 + 64 = 89
  - 8² + 9² = 64 + 81 = 145
  - 1² + 4² + 5² = 1 + 16 + 25 = 42
  - 4² + 2² = 16 + 4 = 20
  - 2² + 0² = 4 (cycle repeats)

## Usage

To check if a number is happy, run the script `main.py` with the number as an argument.

```sh
python src/main.py