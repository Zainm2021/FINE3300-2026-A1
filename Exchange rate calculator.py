import csv
# this imports the CSV module that allows us to manipulate CSV files
with open('BankOfCanadaExchangeRate.2026.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # this accesses the exchange rate file and names it CSV file. It also allows us to reference the different columns and rows as if they were a pair from a dictionary.
    for line in csv_reader:
        USD_to_CAD_ER = float(line["FXAUSDCAD"])

        # this loop goes through each item under the FXAUSDCAD column in the CSV file
    # this sets a variable named USD_to_CAD_ER equal to the final line of the column FXAUSDCAD since we are only interested in the most recent rate


class ExchangeRates:
    def __init__(self, Exchange_rate=USD_to_CAD_ER):
        self.__Exchange_rate = Exchange_rate
    # this defines the object Exchange rate that will be used to exchange currencies

    def convert(self, amount=0, from_currency="USD", to_currency="CAD"):
        if from_currency == "USD" and to_currency == "CAD":
            conversion = amount * self.__Exchange_rate
            print("$" + str(amount) + " US dollars is equal to " +
                  "$" + str(round(conversion, 2)) + " Canadian dollars")
        elif from_currency == "CAD" and to_currency == "USD":
            conversion = amount / self.__Exchange_rate
            print("$" + str(amount) + " Canadian dollars is equal to " +
                  "$" + str(round(conversion, 2)) + " US dollars")
        else:
            print("The currency is not valid")
        return conversion
        # this creates the method convert that holds that calculations for converting from 1 currency to another, based on which currency we are starting with


newexchange = ExchangeRates()
newexchange.convert(amount=94, from_currency="CAD", to_currency="USD")
