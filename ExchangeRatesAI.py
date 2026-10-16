"""
ExchangeRatesAI.py
FINE 3300 - Assignment 1, Part 2 (Vibe Coding)
 
Exchange rate calculator that converts amounts between CAD and USD using
annual exchange rates published by the Bank of Canada.
 
The rate comes from the FXAUSDCAD column of the provided CSV file
(BankOfCanadaExchangeRate.2026.csv). FXAUSDCAD is the number of Canadian
dollars per 1 US dollar. The last row of the file holds the latest rate.
 
Source of data: Bank of Canada annual exchange rates (file provided on Canvas).
"""
 
import csv
 
 
class ExchangeRates:
    """Reads a Bank of Canada exchange rate file and converts between CAD and USD."""
 
    def __init__(self, file_name):
        # Store the file name and load the latest USD/CAD rate from it
        self.file_name = file_name
        self.date, self.usd_cad = self._read_latest_rate()
 
    def _read_latest_rate(self):
        """Return (date, rate) from the last row of the file's FXAUSDCAD column."""
        # 'utf-8-sig' strips the hidden byte-order mark at the start of the file,
        # which would otherwise make the first header read as '﻿Date'
        with open(self.file_name, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
 
        last_row = rows[-1]  # the last row of data is the latest exchange rate
        return last_row["Date"], float(last_row["FXAUSDCAD"])
 
    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
 
        if from_currency == to_currency:
            converted = amount                    # nothing to convert
        elif from_currency == "USD" and to_currency == "CAD":
            converted = amount * self.usd_cad     # USD -> CAD: multiply by CAD per USD
        else:
            converted = amount / self.usd_cad     # CAD -> USD: divide by CAD per USD
 
        return round(converted, 2)                # round to the nearest penny
 
 
def main():
    # Create the converter from the Bank of Canada data file
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
 
    # Prompt the user for the amount and the 'from' and 'to' currencies
    # (per the assignment, inputs are assumed valid, so no validation checks)
    # Remove any '$' signs, commas and spaces so entries like "$1,234.56"
    # are read as the decimal number 1234.56
    amount_text = input("Enter the amount to convert (e.g. 1234.56): ")
    amount = float(amount_text.replace("$", "").replace(",", "").strip())
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()
 
    # Perform the conversion
    result = rates.convert(amount, from_currency, to_currency)
 
    # Display the result with dollar signs, commas, 2 decimals and currency codes
    print(f"\nExchange rate used ({rates.date}): 1 USD = {rates.usd_cad} CAD")
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
 
 
# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
 