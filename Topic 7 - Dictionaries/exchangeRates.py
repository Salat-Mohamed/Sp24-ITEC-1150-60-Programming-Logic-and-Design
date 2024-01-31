# Define the dictionary of currency codes and exchange rates
rates = {
    'AUD': 1.5311,
    'BGN': 1.9558,
    'BRL': 4.9682,
    'CAD': 1.3351,
    'CHF': 0.9863,
    'CNY': 7.0894,
    'CZK': 24.422,
    'DKK': 7.4419,
    'EUR': 1,
    'GBP': 0.87478,
    'HKD': 7.7493,
    'HRK': 7.5353,
    'HUF': 401.15,
    'IDR': 15491.81,
    'ILS': 3.5065,
    'INR': 81.02,
    'ISK': 145.5,
    'JPY': 145.19,
    'KRW': 1397.7,
    'MXN': 19.2611,
    'MYR': 4.6872,
    'NOK': 10.2019,
    'NZD': 1.6769,
    'PHP': 57.672,
    'PLN': 4.6825,
    'RON': 4.8893,
    'RUB': 86.7666,
    'SEK': 10.8538,
    'SGD': 1.3891,
    'THB': 36.906,
    'TRY': 18.3845,
    'USD': 0.9872,
    'ZAR': 17.7983
}

# Get user input for currency code and amount
target_currency = input("Enter the currency code you want to convert to: ").upper()
euros_amount = float(input("Enter the amount in Euros you want to convert: "))

# Check if entered currency code is valid
if target_currency not in rates:
    print(f"Error: Unknown currency code '{target_currency}'. Please try again.")
else:
    # Get the exchange rate from the dictionary
    exchange_rate = rates[target_currency]

    # Calculate the converted amount
    converted_amount = euros_amount * exchange_rate

    # Print the result
    print(f"{euros_amount} EUR is equal to {converted_amount:.2f} {target_currency}.")
