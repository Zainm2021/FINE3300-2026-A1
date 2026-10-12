import csv


class ExchangeRates:
    def __init__(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                rate = float(line["FXAUSDCAD"])
        self.__Exchange_rate = rate
        self.__file_name = file_name

    def convert(self, amount=0, from_currency="USD", to_currency="CAD"):
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


Exchange = ExchangeRates(file_name='BankOfCanadaExchangeRate.2026.csv')
Exchange.convert(amount=94, from_currency="USD", to_currency="USD")
