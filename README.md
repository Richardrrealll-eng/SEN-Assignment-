# SEN-Assignment-

PROJECT: NAIRA CURRENCY CONVERTER
STUDENT: Okechukwu Richard Somtechukwu
MATRIC NO: 24/16001

This software is a Python-based utility designed to convert 
Nigerian Naira (NGN) into international and regional 
currencies using fixed exchange rates. It features a simple 
Command Line Interface (CLI) and handles numerical formatting 
for professional financial reporting.

2. SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)

PHASE 1: REQUIREMENT ANALYSIS
- The goal was to build a tool that solves the problem of 
  calculating exchange values manually. 
- Key Requirement: The software must accept Naira as a float 
  input and provide a conversion to USD, EUR, GBP, or GHS.

PHASE 2: DESIGN
- Logic Flow: [Input] -> [Dictionary Lookup] -> [Calculation] -> [Output].
- Data Structure: A Python 'Dictionary' was chosen to store 
  rates for high-speed retrieval and easy future updates.

PHASE 3: IMPLEMENTATION (CODING)
- Developed using the Python programming language.
- Key Functions used:
    * input(): To collect data from the user.
    * .upper(): To handle case-insensitivity.
    * f-strings: Used for currency formatting (₦1,000.00).



PHASE 4: TESTING
- Positive Test: Inputting 1000 NGN for USD gave the correct 
  mathematical result (0.70 USD).
- Edge Case Test: Inputting lowercase "usd" was successfully 
  handled by the program logic.
- Error Test: Inputting an unsupported currency (e.g., YEN) 
  triggered the "Currency choice not recognized" fallback.

PHASE 5: DEPLOYMENT
- The code is packaged as a single .py script for easy 
  execution on any system with a Python interpreter.
