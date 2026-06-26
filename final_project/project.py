# --- project.py ---
#
# --- Bitcoin Profit Calculator ---


from datetime import date
import csv
import requests


FIRST_CSV_DATE: date = date(2010, 1, 1)
LAST_CSV_DATE: date = date(2026, 2, 8)
FILE_NAME: str = "Final_Project/bitcoin.csv"
TITLE: str = "₿-₿-₿-₿-₿-₿  Bitcoin Profit Calculator  ₿-₿-₿-₿-₿-₿"
LINE = len(TITLE) * "="


def main() -> None:
    while True:
        try: 
            print(LINE)
            print(TITLE) 
            print(LINE)
            print("'Ctrl + C' quits the program at any time\n")

            purchase_date: date = get_purchase_date()
            sell_date: date = get_sell_date(purchase_date)

            purchase_price = get_price_from_csv(purchase_date, FILE_NAME)

            if sell_date == date.today():
                sell_price = get_sell_price_api()
            else: 
                sell_price = get_price_from_csv(sell_date, FILE_NAME)

            if purchase_price is None or sell_price is None:
                print("Error: Could not retrieve price data for those dates.\nPlease try again")
                continue

            amount_invested = get_amount_invested()
            profit, roi = calculate_profit_loss(purchase_price, sell_price, amount_invested)
            
            print(f"\nProfit: ${profit:,.2f}")
            print(f"Return: {roi:,.2f}%")

            repeat: str = input("\nDo you want to repeat or quit? (r/q): ")
            if repeat == "r":
                continue
            else:
                print("Quitting program ...")
                break
        
        except KeyboardInterrupt:
            print("\nQuitting program ...")
            break


def get_purchase_date():
    while True: 
        try:
            date_str: str = input("Purchase Date (YYYY-MM-DD): ")
            year, month, day = date_str.split("-")
            start: date = date(int(year), int(month), int(day))
        except ValueError:
            print("Invalid format! Use YYYY-MM-DD")
            continue
    
        if start < FIRST_CSV_DATE:
            print(f"Warning: Bitcoin data is limited before {FIRST_CSV_DATE}.")
            choice: str = input(f"Use earliest date ({FIRST_CSV_DATE}) or retry? (e/r): ").strip().lower()
            if choice == "e":
                return FIRST_CSV_DATE
            else:
                continue
        elif start >= date.today():
            print("Invalid: Date cannot be today or in the future")
            continue

        return start


def get_sell_date(purchase_date: date):
    while True:
        try:
            date_str: str=  input("Sell Date (YYYY-MM-DD): ")
            year, month, day = date_str.split("-")
            sell: date = date(int(year), int(month), int(day))
        except ValueError:
            print("Invalid format!")
            continue

        if sell <= purchase_date:
            print("Invalid! Sell date cannot be before purchase date.")
            continue
        elif sell > date.today() or sell > LAST_CSV_DATE:
            if sell > LAST_CSV_DATE:
                print(f"Sell date {sell} is after last CSV data ({LAST_CSV_DATE}).")
            else:
                print("Invalid: Date cannot be in the future")

            use_live = input("Use live price instead? (y/n): ").strip().lower()
            if use_live == "y":
                return date.today()
            continue

        return sell


def get_price_from_csv(target_date: date, file_name: str):
    date_str: str = target_date.isoformat() 
    try: 
        with open(file_name, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Date"] == date_str:
                    return float(row["Close"])
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        return None
    
    return None


def get_sell_price_api():
    try:
        response = requests.get(
                "https://rest.coincap.io/v3/assets/bitcoin?apiKey=769ea3a914610b80e80f4a36024228f5ebd40a8ff39defdac86686403354fba4")
        
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        return price
    except requests.RequestException:
        return None


def get_amount_invested():
    print("How much money ($) did or would you have invested? ")
    while True: 
        try:
            amount_invested = float(input("Investment: $"))
            if amount_invested <= 0:
                print("Invalid: Investment must be greater than $0!")
                continue
            return amount_invested
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue


def calculate_profit_loss(purchase_price: float, sell_price: float, amount_invested: float):
    net_profit = ((sell_price / purchase_price) * amount_invested) - amount_invested
    percentage_return = ((sell_price - purchase_price) / purchase_price) * 100    
    return net_profit, percentage_return


if __name__ == "__main__":
    main()