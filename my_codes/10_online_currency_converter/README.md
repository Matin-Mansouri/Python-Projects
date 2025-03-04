
# Online Currency Converter

A real-time currency converter web application built with Streamlit that provides instant currency conversion with up-to-date exchange rates.

## Features

- Real-time currency conversion
- Support for multiple international currencies
- Automatic rate updates every 5 minutes
- Clean and intuitive user interface
- Cached API responses for better performance
- Visual display of conversion results
- Last updated timestamp in human-readable format

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/Matin-Mansouri/Python-Projects/tree/main/my_codes>
cd 10_online-currency-converter
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- streamlit==1.28.2
- currencies==2020.12.12
- cachetools==5.3.2
- requests
- humanize

## Usage

1. Start the Streamlit application:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Use the interface to:
   - Select the base currency
   - Select the target currency
   - Enter the amount to convert
   - View the converted amount and exchange rate in real-time

## Project Structure

```
online-currency-converter/
├── src/
│   ├── app.py              # Main Streamlit web application
│   └── currency_converter.py # Currency conversion logic and API handling
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Technical Details

- Uses the ExchangeRate-API for real-time exchange rates
- Implements caching with TTL (Time To Live) of 5 minutes
- Responsive Streamlit interface with real-time updates
- Error handling for API failures
- Human-readable timestamps for last update information

## API Usage

The application uses the ExchangeRate-API to fetch current exchange rates. The response is cached for 5 minutes to optimize performance and reduce API calls.

## License

This project is licensed under the MIT License.
