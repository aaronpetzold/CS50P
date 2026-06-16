# ₿ BITCOIN PROFIT CALCULATOR ₿
#### Video Demo: 

#### Description:
This is a Command Line Interface (CLI) tool built in Python for my CS50P Final Project. It helps users calculate how much money they made or lost by investing in Bitcoin between two specific dates. It shows the total net profit or loss in US Dollars and also calculates the Return on Investment (ROI) as a percentage.

The program uses two different sources for its price data. For older dates, it reads from a local file named `bitcoin.csv`. This file contains the daily closing prices of Bitcoin from January 1, 2010, up to early 2026. If a user wants to check a calculation up to the current day, the program automatically connects to the internet and fetches the live price using the CoinCap REST API.

This live-pricing mechanism was heavily inspired by Week 4's Problem Set: Bitcoin Price Index (`bitcoin.py`). However, this final project significantly expands upon that foundation. While my original assignment from Week 4 was limited to taking a command-line argument and multiplying it by the current price from the CoinCap API, this final application upgrades the concept. It integrates a historical CSV database alongside the live API. By cross-referencing past records with current live endpoints, the calculator computes actual investment trajectories, net profit/loss margins, and percentage returns (ROI) over custom-defined time horizons.


### Project Structure and Files

The project folder is organized with the following files:

1. **`project.py`**: This is the main file containing the program logic and all the functions:
   - `main()`: Runs the main loop of the application. It prints the text banner, handles the sequence of the program, and formats the final financial output. It keeps running in a loop so the user can do multiple calculations without restarting, and shuts down cleanly if the user presses `Ctrl + C`.
   - `get_purchase_date()`: Asks the user for the buy date. It checks for a valid format and warns the user if the date is older than the CSV data. It also includes a shortcut to default to the earliest available date.
   - `get_sell_date()`: Asks for the sell date and makes sure it is not before the purchase date. If the user picks a date after the CSV timeline, it asks them if they want to switch to the live API price instead.
   - `get_price_from_csv()`: Opens and searches the local `bitcoin.csv` file using Python's built-in `csv` module to find the closing price for a specific day.
   - `get_sell_price_api()`: Connects to the internet and uses the `requests` library to fetch the live Bitcoin price in USD.
   - `get_amount_invested()`: Makes sure the user enters a valid number for their investment that is greater than zero.
   - `calculate_profit_loss()`: The math engine that calculates the exact profit/loss and the ROI percentage.

2. **`test_project.py`**: Contains the automated tests that are run with `pytest`. It tests the math formulas in `calculate_profit_loss`, makes sure `get_price_from_csv` handles missing files without crashing, and checks the data type of the API response.

3. **`requirements.txt`**: A simple text file that lists the `requests` library. This is needed so that anyone else can install the necessary external library using `pip install -r requirements.txt`.

4. **`bitcoin.csv`**: The local spreadsheet file that contains the historical dates and prices for Bitcoin.

### Design Choices
One thing I had to think about was how to test the program with `pytest`. Functions that have `while True` loops and `input()` prompts inside them are very hard to test because `pytest` just freezes and waits for a human to type something. 

Since CS50P only requires testing at least three helper functions, I chose to keep the inputs and loops inside the date and investment functions so the terminal interaction stays clean and simple. Then, I focused my tests entirely on the functions that do not use `input()`, like `calculate_profit_loss`, `get_price_from_csv`, and `get_sell_price_api`. This allowed me to keep my original program structure while still fully meeting the `pytest` requirements for the course.
