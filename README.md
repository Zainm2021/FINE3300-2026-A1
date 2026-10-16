# FINE3300 Assignment 1 Part 1: Exchange Rate Calculator

## Overview
This repository contains my FINE3300 Assignment 1. The assignment includes a Python CAD to USD (or USD to CAD) exchange rate calculator. By using a class called Exchange rate I was able to create the calculator. 

## Files
1. Exchange rate calculator.py : Part 1 code
2. ExchangeRateAI : Part 2 code 
3. BankOfCanadaExchangeRate.2026.csv : Bank of Canada annual exchange rates

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

## Output for part 1:
'''
How much would you like to convert? 100,000
What currency are you starting with (pick between USD or CAD)? usd
What currency do you require (pick between USD or CAD)? cad
$100,000.00 US dollars is equal to $139,780.00 Canadian dollars

How much would you like to convert? 100,000
What currency are you starting with (pick between USD or CAD)? cad
What currency do you require (pick between USD or CAD)? usd
$100,000.00 Canadian dollars is equal to $71,540.99 US dollars
'''

# FINE3300 Assignment 1 Part 2: AI Exchange Rate Calculator
## The model I used 
For part 2 of the assignment I used the AI model Opus 5.5 from Claude. 
## The prompt I used
After uploading the assignment description and CSV file I used the following prompt:
    Using all of this information from my assignment please create an exchange rate calculator that specifically only exchanges amounts from CAD to USD or vice versa. Following the instructions from my professor please make sure you incorporate a user interactivity component so that the amount and currencies used for the conversion come from the users responses. Make sure that all of the amounts are rounded to 2 decimal places and that the program references the CSV file I have uploaded. If you require further context or explanation let me know.

The code it provided me from the first prompt was not bad however if I attempted to input the amount with a comma the code would break so I asked it to fix that using this prompt:
    The code you have provided me is good, however it does not let me input commas places for the amount, can you change that?

## Output for part 2:
'''
Enter the amount to convert (e.g. 1234.56): 100,000
Convert from (USD or CAD): CAD
Convert to (USD or CAD): USD 

Exchange rate used (2025-01-01): 1 USD = 1.3978 CAD
$100,000.00 CAD = $71,540.99 USD

Enter the amount to convert (e.g. 1234.56): 100,000
Convert from (USD or CAD): USD
Convert to (USD or CAD): CAD

Exchange rate used (2025-01-01): 1 USD = 1.3978 CAD
$100,000.00 USD = $139,780.00 CAD
'''
# FINE3300 Assignment 1 Part 1&2 Comparison
When comparing my code to the code the AI created, both programs share the same core structure. They both include a class named ExchangeRates that reads the Bank of Canada file using csv.DictReader, they both use the rate from the FXAUSDCAD column, they both multiply for USD to CAD and divide for CAD to USD, and they both produce the same results. The main differences between the two are in the design and style of the code. In my class I stored the exchange rate as a private member, while the AI used public attributes and moved the file reading into a separate helper method. To find the most recent rate, my code uses a for loop that goes through every row and keeps the last value, while the AI reads all of the rows into a list and takes the last one directly using rows[-1]. The AI also opens the file with a specific encoding to handle a hidden character at the start of the CSV file, which my code did not need since I never used the Date column. The AI’s convert method also uses fewer if statements because it checks whether the two currencies are the same in one condition, and it only returns the rounded result. The printing and the input prompts are then handled in a separate function called main(). In my code, the convert method both calculates and prints the result, and it includes a branch for invalid currencies. For formatting, the AI used an f-string while I used the format() function, but both outputs show dollar signs, commas and two decimal places. The AI’s version also prints the exchange rate and date used, removes extra characters like dollar signs and spaces from the input, and uses an if __name__ == "__main__": safeguard so the program only runs when the file is executed directly. Overall, the AI’s code is more modular, while my code keeps the logic in fewer places and follows the class structure we covered in lectures.
