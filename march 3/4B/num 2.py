import csv

currency_rates = {}

with open("currency.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if len(row) == 3:
            code, name, rate = row
        elif len(row) == 2:
            code, rate = row
        else:
            continue

        currency_rates[code.upper()] = float(rate)

usd_amount = float(input("How much dollar do you have right now?: "))
currency_code = input("What currency do you want to have?: ").upper()

if currency_code in currency_rates:
    converted_amount = usd_amount * currency_rates[currency_code]
    print(f"\nDollar: {usd_amount} USD")
    print(f"{currency_code}: {converted_amount:.6f}")
else:
    print("Sorry, that currency is not available.")
