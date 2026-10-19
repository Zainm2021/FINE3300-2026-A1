'''
This is my FINE3300 Assignment 1 Part 1
Below is my exchange rate calculator that converts between CAD and USD or vice versa using the most recent USD/CAD rate from the Bank of Canada
'''

# Imports the CSV module so we can read the exchange rate CSV file
import csv


class ExchangeRates:
    # Reads the exchange rate file and stores the latest USD/CAD Exchange rate
    def __init__(self, file_name):
        # Tells Python to open the file whose name is passed when the object is instantiated
        with open(file_name) as csv_file:
            # DictReader lets us look up each row's values using column name as a key
            csv_reader = csv.DictReader(csv_file)

            # This loop goes through each row and sets the 'rate' variable = to the value in the FXAUSDCAD column
            # Each row overwrites 'rate', so after the loop it holds the last row's value, which is the most recent exchange rate
            for line in csv_reader:
                rate = float(line["FXAUSDCAD"])

        # Saves the rate and file name on the object as private members, this allows other methods to use them
        self.__exchange_rate = rate
        self.__file_name = file_name

    # Converts an amount between USD and CAD and prints the formatted result.
    # The rate is CAD per 1 USD, so we multiply for USD -> CAD
    # and divide for CAD -> USD.
    def convert(self, amount, from_currency, to_currency):
        # Converts USD to CAD
        if from_currency == "USD" and to_currency == "CAD":
            conversion = amount * self.__exchange_rate
            print("$" + format(amount, ",.2f") + " US dollars is equal to " + "$" + format(conversion, ",.2f") + " Canadian dollars")

        # Converts CAD to USD
        elif from_currency == "CAD" and to_currency == "USD":
            conversion = amount / self.__exchange_rate
            print("$" + format(amount, ",.2f") + " Canadian dollars is equal to " + "$" + format(conversion, ",.2f") + " US dollars")

        # Converts CAD to CAD, no conversion needed
        elif from_currency == "CAD" and to_currency == "CAD":
            conversion = amount
            print("The currency has not been exchanged, it equals " + "$" + format(amount, ",.2f") + " Canadian dollars")

        # Converts USD to USD, no conversion needed
        elif from_currency == "USD" and to_currency == "USD":
            conversion = amount
            print("The currency has not been exchanged, it equals " + "$" + format(amount, ",.2f") + " US dollars")

        # Acts as a safety net ensuring 'conversion' always has a value before returning,
        # even though the assignment assumes only USD or CAD will be entered
        else:
            print("The currency is not valid")
            conversion = 0
        return conversion


# This part of the program instantiates an ExchangeRates object and tells it to reference the bank of canada exchange rate file
exchanging_currency = ExchangeRates(file_name='BankOfCanadaExchangeRate.2026.csv')

# Prompts the user to share the amount of currency they would like to convert and which currency they’re converting from and to, it then stores these values in the variables amount, from_currency and to_currency.
# The upper method allows the user to type CAD/USD in upper or lower case.
# The strip method ensures that if there are spaces included with the currency they are ignored.
amount = float(input("How much would you like to convert? ").replace(",", ""))
from_currency = input("What currency are you starting with (pick between USD or CAD)? ").strip().upper()
to_currency = input("What currency do you require (pick between USD or CAD)? ").strip().upper()

# Pass the user's inputs into convert to calculate and print the result
exchanging_currency.convert(amount=amount, from_currency=from_currency, to_currency=to_currency)
