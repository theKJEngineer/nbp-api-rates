# NBP API Rates

Python script that fetches and displays current currency exchange rates from the **National Bank of Poland (NBP) public API**.

## Features
- Retrieves the latest exchange rate table from NBP (table A).
- Displays table number, effective date, and a full list of currency rates.
- Shows the current USD rate.

## Requirements
- Python 3.7+
- [requests](https://pypi.org/project/requests/) library


## Example output
```text
Tabela: 195/A/NBP/2025
Date: 2025-09-21
Number of currencies: 35
USD rate: 4.12

USD: 4.12  (dolar amerykański)
EUR: 4.34  (euro)
GBP: 5.12  (funt szterling)
JPY: 0.027 (jen)
...
