
import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/?format=json")

if response.ok == True:
    data = response.json()[0]       # The response is a list with one dictionary, so take the first element
    table_no = data["no"]
    date = data["effectiveDate"]
    rates = data["rates"]           # List of all currency rates with currency name, code, and mid value

    print("Tabela:", table_no)
    print("Date:", date)
    print("Number of currencies:", len(rates))

    usd_rate = next(r['mid'] for r in rates if r['code'] == 'USD')
    print("USD rate:", usd_rate)

    for r in rates:
        print(f"{r['code']}: {r['mid']}  ({r['currency']})")
else:
    # If request failed, print the HTTP status code
    print("Request error:", response.status_code)