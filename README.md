# FINE3300 Assignment 1: Exchange Rate Calculator

## Overview
This repository contains my FINE3300 Assignment 1. The assignment includes a Python CAD to USD (or USD to CAD) exchange rate calculator. By using a class called Exchange rate I was able to create the calculator. 

## Files
-Exchange rate calculator.py : Part 1 code
-ExchangeRateAI : Part 2 code 
-BankOfCanadaExchangeRate.2026.csv : Bank of Canada annual exchange rates

## How It Works
### The ExchangeRates Class
I created a class named ExchangeRates which defines the object ExchangeRates allowing users to select a specific file they would like to use to determine the exchange rate. The class then uses a for loop to go through each row in the file and look for the most recent USD to CAD exchange rate and uses this rate.
### The convert method
Within the class I also created the method convert which based off of the 3 parameters of amount, from_currency and to_currency applies a conversion to the amount using the exchange rate from the CSV file. This method accounts for the 2 ways an exchange can occur, from USD to CAD or vice versa. It also formats the output of the currency exchanged to two decimal places.
### User Input
I then instantiated the object to begin exchanging currency, and selected the BankOfCanadaExchangeRate file to pull data from. Using the input function I then prompt the user to select the amount they would like to convert, the currency they are beginning with and the currency they want. The code is then finalized by taking the inputs from the user and placing them into the convert method on the object I created.

## How to run
1. Clone this repository
2. Open the folder in Visual Studio Code
3. Run `Exchange rate calculator.py`
4. Enter the amount, then USD or CAD for each currency when prompted