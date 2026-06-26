import sys
import requests


def main():
    amount = get_amount()
    price_usd = get_price_usd()
    total_price = get_total_price(price_usd, amount)
    print(f"${total_price:,.4f}")


def get_amount():
    try:
        if len(sys.argv) == 2:
            amount = float(sys.argv[1])
            return amount
        elif len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price_usd():
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=84d46bbe8af0549abd2a27a63aff0356a9254d2a9ecde26d803815bc53aab63d"
        )
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
        return price_usd
    except requests.RequestException:
        sys.exit("Could not fetch Bitcoin price")


def get_total_price(price_usd, amount):
    total_price = price_usd * amount
    return total_price


if __name__ == "__main__":
    main()
