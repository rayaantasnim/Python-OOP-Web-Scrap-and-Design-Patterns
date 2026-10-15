#Final project for webscraping and automation
#Final Project - Auto Gmail Sending for Currency & Book Info with Weather also 🌍📩

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import smtplib
from email.message import EmailMessage
import schedule
import time

# Email sending function (takes body, subject, receiver)
def mail_sender(name, body, subject, receiver):
    sender = "jobayerhasanshiplu@gmail.com"
    app_password = "eovd ozwp uyud pskh"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    body = f"Hello {name} 👋, \n\nGlad to see you here 😊. We hope that you are also well 💙.  \nThis Electronic mail (E-mail) is being sent as a project of Python programming Web and API scrapping 🧠💻. As you asked to know, we are here to assist you always with updated detabase and informations 📊✨. Here you go:\n\n" + body + "\nEveryday you will get updates via Gmail from us.\nThank you for taking our service! Please visit us again 🙏. We are all ears for you to assist 🤝.\n\nExplore more of our projects 🌐: https://rayaantasnim.github.io/username.github.io-IDAI-company-/Intro.html \n\nBest Regards,\nRayaan Tasnim ✍️\nPython Programmer"
    msg.set_content(body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, app_password)
    server.send_message(msg)
    server.quit()
    print("📧 Email sent successfully! ✅")


# Currency exchange rate function 💰
def currency_auto():
    api_key = "cur_live_bHpelBdV9C9b3x9X7BXJysHbEKU5e7nqf0sQIlKT"
    url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&base_currency=USD&currencies=BDT,EUR,INR,GBP,CAD,AUD,JPY,CNY,SAR,AED,CHF,PKR,NZD,SGD,HKD,KRW,THB,MYR,RUB,TRY,ZAR,NGN,EGP"

    response = requests.get(url)
    data = response.json()

    bangladeshi_taka = data["data"]["BDT"]["value"]
    euro = data["data"]["EUR"]["value"]
    indian_rupee = data["data"]["INR"]["value"]
    british_pound = data["data"]["GBP"]["value"]
    canadian_dollar = data["data"]["CAD"]["value"]
    australian_dollar = data["data"]["AUD"]["value"]
    japanese_yen = data["data"]["JPY"]["value"]
    chinese_yuan = data["data"]["CNY"]["value"]
    saudi_riyal = data["data"]["SAR"]["value"]
    uae_dirham = data["data"]["AED"]["value"]
    swiss_franc = data["data"]["CHF"]["value"]
    pakistani_rupee = data["data"]["PKR"]["value"]
    new_zealand_dollar = data["data"]["NZD"]["value"]
    singapore_dollar = data["data"]["SGD"]["value"]
    hong_kong_dollar = data["data"]["HKD"]["value"]
    south_korean_won = data["data"]["KRW"]["value"]
    thai_baht = data["data"]["THB"]["value"]
    malaysian_ringgit = data["data"]["MYR"]["value"]
    russian_ruble = data["data"]["RUB"]["value"]
    turkey = data["data"]["TRY"]["value"]
    south_african_rand = data["data"]["ZAR"]["value"]
    nigerian_naira = data["data"]["NGN"]["value"]
    egyptian_pound = data["data"]["EGP"]["value"]

    print("\n\n")
    print("\n💰 Current Currency Exchange Rates (USD Base) 📊:\n")
    print(f"🇧🇩 Bangladeshi Taka: {bangladeshi_taka}")
    print(f"🇪🇺 Euro: {euro}")
    print(f"🇮🇳 Indian Rupee: {indian_rupee}")
    print(f"🇬🇧 British Pound: {british_pound}")
    print(f"🇨🇦 Canadian Dollar: {canadian_dollar}")
    print(f"🇦🇺 Australian Dollar: {australian_dollar}")
    print(f"🇯🇵 Japanese Yen: {japanese_yen}")
    print(f"🇨🇳 Chinese Yuan: {chinese_yuan}")
    print(f"🇸🇦 Saudi Riyal: {saudi_riyal}")
    print(f"🇦🇪 UAE Dirham: {uae_dirham}")
    print(f"🇨🇭 Swiss Franc: {swiss_franc}")
    print(f"🇵🇰 Pakistani Rupee: {pakistani_rupee}")
    print(f"🇳🇿 New Zealand Dollar: {new_zealand_dollar}")
    print(f"🇸🇬 Singapore Dollar: {singapore_dollar}")
    print(f"🇭🇰 Hong Kong Dollar: {hong_kong_dollar}")
    print(f"🇰🇷 South Korean Won: {south_korean_won}")
    print(f"🇹🇭 Thai Baht: {thai_baht}")
    print(f"🇲🇾 Malaysian Ringgit: {malaysian_ringgit}")
    print(f"🇷🇺 Russian Ruble: {russian_ruble}")
    print(f"🇹🇷 Turkish Lira: {turkey}")
    print(f"🇿🇦 South African Rand: {south_african_rand}")
    print(f"🇳🇬 Nigerian Naira: {nigerian_naira}")
    print(f"🇪🇬 Egyptian Pound: {egyptian_pound}")

    report = f"""
Currency Exchange Rates (USD Base) 💰:

Bangladeshi Taka: {bangladeshi_taka}
Euro: {euro}
Indian Rupee: {indian_rupee}
British Pound: {british_pound}
Canadian Dollar: {canadian_dollar}
Australian Dollar: {australian_dollar}
Japanese Yen: {japanese_yen}
Chinese Yuan: {chinese_yuan}
Saudi Riyal: {saudi_riyal}
UAE Dirham: {uae_dirham}
Swiss Franc: {swiss_franc}
Pakistani Rupee: {pakistani_rupee}
New Zealand Dollar: {new_zealand_dollar}
Singapore Dollar: {singapore_dollar}
Hong Kong Dollar: {hong_kong_dollar}
South Korean Won: {south_korean_won}
Thai Baht: {thai_baht}
Malaysian Ringgit: {malaysian_ringgit}
Russian Ruble: {russian_ruble}
Turkish Lira: {turkey}
South African Rand: {south_african_rand}
Nigerian Naira: {nigerian_naira}
Egyptian Pound: {egyptian_pound}
"""

    mail_sender(name, report, "Currency Exchange Rates 💰", gmail)
    print("\n✔ Currency report sent to your Gmail 📩!")
    return(bangladeshi_taka, euro, indian_rupee, british_pound, canadian_dollar, australian_dollar, japanese_yen, chinese_yuan, saudi_riyal, uae_dirham, swiss_franc, pakistani_rupee, new_zealand_dollar, singapore_dollar, hong_kong_dollar, south_korean_won, thai_baht, malaysian_ringgit, russian_ruble, turkey, south_african_rand, nigerian_naira, egyptian_pound)

def search_box(bangladeshi_taka, euro, indian_rupee, british_pound, canadian_dollar, australian_dollar, japanese_yen, chinese_yuan, saudi_riyal, uae_dirham, swiss_franc, pakistani_rupee, new_zealand_dollar, singapore_dollar, hong_kong_dollar, south_korean_won, thai_baht, malaysian_ringgit, russian_ruble, turkey, south_african_rand, nigerian_naira, egyptian_pound):
    while True:
        search_field = input("\n🔎 Search currency (bdt, eur, inr, gbp, cad, aud, jpy, cny, sar, aed, chf, pkr, nzd, sgd, hkd, krw, thb, myr, rub, try, zar, ngn, egp) or type break 🚪: ").strip().lower()

        if search_field == "break":
            print("Search Completed! ✅")
            break

        elif search_field == "bdt":
            print(f"🇧🇩 Bangladeshi Taka: {bangladeshi_taka}")

        elif search_field == "eur":
            print(f"🇪🇺 Euro: {euro}")

        elif search_field == "inr":
            print(f"🇮🇳 Indian Rupee: {indian_rupee}")

        elif search_field == "gbp":
            print(f"🇬🇧 British Pound: {british_pound}")

        elif search_field == "cad":
            print(f"🇨🇦 Canadian Dollar: {canadian_dollar}")

        elif search_field == "aud":
            print(f"🇦🇺 Australian Dollar: {australian_dollar}")

        elif search_field == "jpy":
            print(f"🇯🇵 Japanese Yen: {japanese_yen}")

        elif search_field == "cny":
            print(f"🇨🇳 Chinese Yuan: {chinese_yuan}")

        elif search_field == "sar":
            print(f"🇸🇦 Saudi Riyal: {saudi_riyal}")

        elif search_field == "aed":
            print(f"🇦🇪 UAE Dirham: {uae_dirham}")

        elif search_field == "chf":
            print(f"🇨🇭 Swiss Franc: {swiss_franc}")

        elif search_field == "pkr":
            print(f"🇵🇰 Pakistani Rupee: {pakistani_rupee}")

        elif search_field == "nzd":
            print(f"🇳🇿 New Zealand Dollar: {new_zealand_dollar}")

        elif search_field == "sgd":
            print(f"🇸🇬 Singapore Dollar: {singapore_dollar}")

        elif search_field == "hkd":
            print(f"🇭🇰 Hong Kong Dollar: {hong_kong_dollar}")

        elif search_field == "krw":
            print(f"🇰🇷 South Korean Won: {south_korean_won}")

        elif search_field == "thb":
            print(f"🇹🇭 Thai Baht: {thai_baht}")

        elif search_field == "myr":
            print(f"🇲🇾 Malaysian Ringgit: {malaysian_ringgit}")

        elif search_field == "rub":
            print(f"🇷🇺 Russian Ruble: {russian_ruble}")

        elif search_field == "try":
            print(f"🇹🇷 Turkish Lira: {turkey}")

        elif search_field == "zar":
            print(f"🇿🇦 South African Rand: {south_african_rand}")

        elif search_field == "ngn":
            print(f"🇳🇬 Nigerian Naira: {nigerian_naira}")

        elif search_field == "egp":
            print(f"🇪🇬 Egyptian Pound: {egyptian_pound}")

        else:
            print("❌ Not found in the detabase!")

def currency():
    bangladeshi_taka, euro, indian_rupee, british_pound, canadian_dollar, australian_dollar, japanese_yen, chinese_yuan, saudi_riyal, uae_dirham, swiss_franc, pakistani_rupee, new_zealand_dollar, singapore_dollar, hong_kong_dollar, south_korean_won, thai_baht, malaysian_ringgit, russian_ruble, turkey, south_african_rand, nigerian_naira, egyptian_pound = currency_auto()

    search_box(
        bangladeshi_taka, euro, indian_rupee, british_pound,
        canadian_dollar, australian_dollar, japanese_yen,
        chinese_yuan, saudi_riyal, uae_dirham, swiss_franc,
        pakistani_rupee, new_zealand_dollar, singapore_dollar,
        hong_kong_dollar, south_korean_won, thai_baht,
        malaysian_ringgit, russian_ruble, turkey,
        south_african_rand, nigerian_naira, egyptian_pound
    )

# Book scraping function 📚
def book():
    url = "https://books.toscrape.com/"
    agent = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=agent)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.select(".image_container a")

    report = "Book List 📚:\n\n"
    print("\n📚 Best Seller Books 📖:\n")

    for i in div[:15]:
        href = i.get("href")
        full_link = urljoin(url, href)
        r = requests.get(full_link, headers=agent)
        s = BeautifulSoup(r.text, "html.parser")

        title = s.select_one(".product_main h1").text.strip()
        price = s.select_one(".price_color").text.strip()
        price = price.replace("Â£", "")
        price = price + " GBP 💷"
        availability = s.select_one(".instock.availability").text.strip()

        print(f"📘 Title: {title}\n💰 Price: {price}\n📦 Availability: {availability}\n")
        report += f"Title: {title}\nPrice: {price}\nAvailability: {availability}\n\n"

    mail_sender(name, report, "Book List Information 📚", gmail)
    print("\n✔ Book list sent to your Gmail 📩!")


# Weather function 🌦️
def weather(data):
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    max_temp = data["main"]["temp_max"]
    min_temp = data["main"]["temp_min"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    weather_main = data["weather"][0]["main"]
    weather_desc = data["weather"][0]["description"]
    country = data["sys"]["country"]
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    visibility = data.get("visibility", "Unknown")
    clouds = data["clouds"]["all"]

    suggestions = []

    if temp >= 35:
        suggestions.append("• Extremely hot weather 🔥 Drink water 💧")

    elif temp >= 25:
        suggestions.append("• Warm weather ☀️ Light clothes recommended")

    elif temp >= 15:
        suggestions.append("• Pleasant weather 😊 Normal clothing fine")

    elif temp >= 5:
        suggestions.append("• Cool weather 🧥 Light jacket needed")

    else:
        suggestions.append("• Cold weather 🥶 Stay warm")

    if feels_like > temp + 3:
        suggestions.append("• Feels hotter than actual temperature 🌡️")

    if humidity >= 80:
        suggestions.append("• High humidity 💦 Stay hydrated")

    elif humidity <= 30:
        suggestions.append("• Dry air 🌵 Drink water")

    if wind_speed >= 10:
        suggestions.append("• Strong winds 🌬️ Be careful")

    if pressure < 1000:
        suggestions.append("• Low pressure ⚠️ Weather may change")

    if visibility != "Unknown" and visibility < 3000:
        suggestions.append("• Low visibility 🚗 Drive carefully")

    if clouds >= 80:
        suggestions.append("• Cloudy sky ☁️ Rain possible")

    if "rain" in weather_desc.lower():
        suggestions.append("• Carry umbrella ☔")

    if "thunderstorm" in weather_desc.lower():
        suggestions.append("• Thunderstorm ⛈️ Stay indoors")

    if "snow" in weather_desc.lower():
        suggestions.append("• Snow ❄️ Be careful")

    if "mist" in weather_desc.lower() or "fog" in weather_desc.lower():
        suggestions.append("• Fog 🌫️ Visibility low")

    suggestion_text = "\n".join(suggestions)

    print(f"\n🌡️ Temperature: {temp}°C")
    print(f"🤗 Feels Like: {feels_like}°C")
    print(f"🔺 Max Temperature: {max_temp}°C")
    print(f"🔻 Min Temperature: {min_temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"📊 Pressure: {pressure} hPa")
    print(f"👁️ Visibility: {visibility}")
    print(f"☁️ Cloud Coverage: {clouds}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
    print(f"🧭 Wind Direction: {wind_deg}°")
    print(f"🌍 Weather: {weather_main}")
    print(f"📝 Description: {weather_desc}")
    print(f"🌅 Sunrise: {sunrise}")
    print(f"🌇 Sunset: {sunset}")

    print("\n💡 Suggestions:")
    for item in suggestions:
        print(item)

    report = f"""
Weather Report 🌦️ for {country}

Temperature: {temp}°C
Feels Like: {feels_like}°C
Max Temperature: {max_temp}°C
Min Temperature: {min_temp}°C
Humidity: {humidity}%
Pressure: {pressure} hPa
Visibility: {visibility}
Cloud Coverage: {clouds}%
Wind Speed: {wind_speed}
Wind Direction: {wind_deg}
Weather: {weather_main}
Description: {weather_desc}
Sunrise: {sunrise}
Sunset: {sunset}

Suggestions:
{suggestion_text}
"""

    mail_sender(name, report, f"Weather Update 🌦️ - {city}", gmail)
    print("\n✔ Weather report sent to your Gmail 📩!")

def weather_auto(weather_city):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={weather_city}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    data = response.json()
    weather(data)

# Starting 
print("------------------------------ Welcome! 👋 ------------------------------")
name = input("👤 Enter your name pls: ").title().strip()
gmail = input("📧 Enter your G-mail account: ").strip()

while(True):
    if (gmail == "jobayerhasanshiplu@gmail.com"):
        print("❌ The sender and receiver can't be same 😅")
        gmail = input("📧 Try again pls: ").strip()

    elif "@" in gmail and "." in gmail:
        print("✅ Thank you!! \nWe will send you updates 😊 if you order 📩")
        break

    else:
        gmail = input("❌ Wrong gmail provided! Try again 📧: ").strip()
gmail = gmail.lower()

# Menu
while(True):
    print("\n📋 Menu:")
    print("1.   Current Currency Exchange Rate 💰")
    print("2.   Best Seller Book List 📚")
    print("3.   Today Current Weather Update 🌦️")

    order = input("👉 Enter menu number: ").strip()
    print("------------------------------⚙️ Processing... ⚙️ ------------------------------")

    if order == "1":
        currency()
        break

    elif order == "2":
        book()
        break

    elif order == "3":
        city = input("Enter your desired location pls:").title().strip()
        api_key = "d3e32d448f57160e352fefe7e60766e9"

        while True:
            api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(api_url)
            data = response.json()

            if str(data.get("cod")) != "200":
                print("\n❌ City not found! Try again 😢")
                city = input("Enter again: ")
            else:
                print("\n🌤️ Let's Explore!!! 🚀\n")
                weather(data)
                break
        break

    else:
        print("❌ Invalid order given! Try again 😢")


print("\n------------ Task Completed! 🎉 ------------")
print("📩 Check your Gmail Inbox")
print("Everyday at 12:00 pm ⏰, you will get email for updates.")
print("🙏 Thank you for taking our service 💕")
print("🤝 We are always here to accompany you!")

# ---------------- SCHEDULE (12:00 PM DAILY) ----------------
def job():
    if order == "1":
        currency_auto()

    elif order == "2":
        book()

    elif order == "3":
        weather_auto(city)

schedule.every().day.at("12:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(5)