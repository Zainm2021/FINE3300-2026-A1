import csv


class ExchangeRates:
    def __init__(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                rate = float(line["FXAUSDCAD"])
        self.__exchange_rate = rate
        self.__file_name = file_name

    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            conversion = amount * self.__Exchange_rate
            print("$" + str(amount) + " US dollars is equal to " +
                  "$" + str(round(conversion, 2)) + " Canadian dollars")
        elif from_currency == "CAD" and to_currency == "USD":
            conversion = amount / self.__Exchange_rate
            print("$" + str(amount) + " Canadian dollars is equal to " +
                  "$" + str(round(conversion, 2)) + " US dollars")
        elif from_currency == "CAD" and to_currency == "CAD":
            conversion = amount
            print("The currency has not been exchanged, it equals " +
                  "$" + str(amount) + " Canadian dollars")
        elif from_currency == "USD" and to_currency == "USD":
            conversion = amount
            print("The currency has not been exchanged, it equals " +
                  "$" + str(amount) + " US dollars")
        else:
            print("The currency is not valid")
            conversion = 0
        return conversion


exchanging_currency = ExchangeRates(file_name='BankOfCanadaExchangeRate.2026.csv')
amount = float(input("How much would you like to convert? ")) 
from_currency = input("What currency are you starting with(pick between USD or CAD? ")
to_currency = input("What currency do you require(pick between USD or CAD? ")
exchanging_currency.convert(amount=amount, from_currency=from_currency, to_currency=to_currency)
