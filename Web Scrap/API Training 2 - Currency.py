import requests
api_key = "cur_live_bHpelBdV9C9b3x9X7BXJysHbEKU5e7nqf0sQIlKT"
url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&base_currency=USD&currencies=EUR,BDT,INR,GBP,CAD,AUD,JPY,CNY,SAR,AED,CHF,PKR,NZD,SGD,HKD,KRW,THB,MYR,RUB,TRY,ZAR,NGN,EGP"

response = requests.get(url)
print(response.status_code)
data = response.json()

bdt = data["data"]["BDT"]["value"]
print(f"The current value of BDT (Bangladeshi Taka) converted from USD: {bdt}")

eur = data["data"]["EUR"]["value"]
print(f"The current value of EUR (Euro) converted from USD: {eur}")

inr = data["data"]["INR"]["value"]
print(f"The current value of INR (Indian Rupee) converted from USD: {inr}")

gbp = data["data"]["GBP"]["value"]
print(f"The current value of GBP (British Pound) converted from USD: {gbp}")

cad = data["data"]["CAD"]["value"]
print(f"The current value of CAD (Canadian Dollar) converted from USD: {cad}")

aud = data["data"]["AUD"]["value"]
print(f"The current value of AUD (Australian Dollar) converted from USD: {aud}")

jpy = data["data"]["JPY"]["value"]
print(f"The current value of JPY (Japanese Yen) converted from USD: {jpy}")

cny = data["data"]["CNY"]["value"]
print(f"The current value of CNY (Chinese Yuan) converted from USD: {cny}")

sar = data["data"]["SAR"]["value"]
print(f"The current value of SAR (Saudi Riyal) converted from USD: {sar}")

aed = data["data"]["AED"]["value"]
print(f"The current value of AED (UAE Dirham) converted from USD: {aed}")

chf = data["data"]["CHF"]["value"]
print(f"The current value of CHF (Swiss Franc) converted from USD: {chf}")

pkr = data["data"]["PKR"]["value"]
print(f"The current value of PKR (Pakistani Rupee) converted from USD: {pkr}")

nzd = data["data"]["NZD"]["value"]
print(f"The current value of NZD (New Zealand Dollar) converted from USD: {nzd}")

sgd = data["data"]["SGD"]["value"]
print(f"The current value of SGD (Singapore Dollar) converted from USD: {sgd}")

hkd = data["data"]["HKD"]["value"]
print(f"The current value of HKD (Hong Kong Dollar) converted from USD: {hkd}")

krw = data["data"]["KRW"]["value"]
print(f"The current value of KRW (South Korean Won) converted from USD: {krw}")

thb = data["data"]["THB"]["value"]
print(f"The current value of THB (Thai Baht) converted from USD: {thb}")

myr = data["data"]["MYR"]["value"]
print(f"The current value of MYR (Malaysian Ringgit) converted from USD: {myr}")

rub = data["data"]["RUB"]["value"]
print(f"The current value of RUB (Russian Ruble) converted from USD: {rub}")

Turkey = data["data"]["TRY"]["value"]
print(f"The current value of TRY (Turkish Lira) converted from USD: {Turkey}")

zar = data["data"]["ZAR"]["value"]
print(f"The current value of ZAR (South African Rand) converted from USD: {zar}")

ngn = data["data"]["NGN"]["value"]
print(f"The current value of NGN (Nigerian Naira) converted from USD: {ngn}")

egp = data["data"]["EGP"]["value"]
print(f"The current value of EGP (Egyptian Pound) converted from USD: {egp}")


currency = input("\nEnter a currency code to search again (e.g. INR, EUR, BDT): ").upper()
a = currency.strip()

if a in data["data"]:
    value = data["data"][a]["value"]
    print(f"The current value of {a} converted from USD: {value}")

else:
    print(" Currency code not found!")