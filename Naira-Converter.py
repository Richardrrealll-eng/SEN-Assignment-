# Name: Okechukwu Richard Somtechukwu
# Matric No: 24/16001
def currency_converter():
    # Approximate exchange rates for 1 NGN (Jan 2026)
    rates = {
        "USD": 0.00070,  # US Dollar
        "EUR": 0.00065,  # Euro
        "GBP": 0.00054,  # British Pound
        "GHS": 0.01100   # Ghanaian Cedi
    }
    
    print("--- Currency Converter ---")
    naira = float(input("Enter amount in Naira (₦): "))
    target = input("Convert to (USD, EUR, GBP, GHS): ").upper()

    if target in rates:
        result = naira * rates[target]
        print(f"₦{naira:,} is approximately {result:,.2f} {target}")
    else:
        print("Currency choice not recognized.")

currency_converter()
