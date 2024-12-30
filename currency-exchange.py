import requests

# Defining API URL and Key
API_KEY = "449337857207d3371c171dc7" 
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# getting current exchange rates
def get_exchange_rates():
    response = requests.get(BASE_URL) #requesting to the API
    
     # Checking if the response is successful (HTTP Status Code 200)
    if response.status_code == 200:
        data = response.json()
        return data["conversion_rates"]
    else:
        print("Error Ocurred!")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    
    if not rates: # If no exchange rates were found, exit the function
        print("Unable to fetch exchange rates.")
        return
    
    if from_currency == "USD":
        base_rate = 1 #setting the base rate to 1 
    else:
        base_rate = rates.get(from_currency)
    
    target_rate = rates.get(to_currency)
    
    #If either the base or target rate is invalid, print an error
    if base_rate is None or target_rate is None:
        print("Invalid currency code.")
        return
    
    # Performing the currency conversion 
    converted_amount = (amount / base_rate) * target_rate
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    
    return converted_amount

# Function to show exchange rate for a currency pair
def get_exchange_rate(from_currency, to_currency):
    rates = get_exchange_rates()
    
    if not rates:
        print("Not Found!")
        return
    
    if from_currency == "USD":
        base_rate = 1
    else:
        base_rate = rates.get(from_currency)
    
    target_rate = rates.get(to_currency)
    
    if base_rate is None or target_rate is None:
        print("Invalid currency code!")
        return
     # Calculating the exchange rate between the two currencies
    rate = target_rate / base_rate
    print(f"Exchange rate {from_currency} -> {to_currency} = {rate:.4f}")
    
    return rate

# Function to list all available currencies
def list_currencies():
    rates = get_exchange_rates()
    
    if not rates:
        print("Not Found!")
        return
    
    print("Available currencies and their rates against USD:")
    for currency, rate in rates.items():
        print(f"{currency}: {rate:.4f}")

# Main function
def main():
    print("Welcome to the Currency Converter!")
    print("List - List all available currencies and their rates.")
    print("Convert - Convert between two currencies.")
    print("Rate - Get the exchange rate between two currencies.")
    
    while True: # Starting an infinite loop to continuously accept user input
        command = input("Enter a command (q to quit): ").lower()
        
        if command == "q":
            break
        elif command == "list":
            list_currencies()
        elif command == "convert":
            from_currency = input("Enter the currency you have (e.g., USD, EUR): ").uppper()
            amount = input(f"Enter an amount in {from_currency}: ")
            
            try:
                amount = float(amount)
            except ValueError:
                print("Invalid amount")
                break
            
            to_currency = input("Enter the currency you want to exchange to (e.g., USD, EUR): ").upper()
            
            convert_currency(amount, from_currency, to_currency)
        elif command == "rate":
            from_currency = input("Enter your currency (e.g., USD, EUR):").upper()
            to_currency = input("Enter the currency you want to exchange to (e.g., USD, EUR): ").upper()
            get_exchange_rate(from_currency, to_currency)
        else:
            print("Unrecognized command! Please try again.")

if __name__ == "__main__": # Checking if it is being run directly and call the main function
    main()
