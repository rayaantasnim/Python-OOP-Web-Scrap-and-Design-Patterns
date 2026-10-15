import schedule
import requests
import time 
import smtplib
from email.message import EmailMessage

def temp_scrap():
    city_name= "Dhaka"
    api_key = "d3e32d448f57160e352fefe7e60766e9"

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    data = response.json()

    temp = data["main"]["temp"]
    maximum = data["main"]["temp_max"]
    minimum = data["main"]["temp_min"]
    
    print("Returning informations")
    return(temp, maximum, minimum)

def send_email(temp, maximum, minimum):
    sender = "instructor076@gmail.com"
    app_password = "mkql fzpp wauk gxph"
    receiver = ["rayaantasnim@gmail.com",
                "jobayerhasanshiplu@gmail.com",
                "AHANAFShabab@gmail.com",
                "shahanazsultana86@gmail.com",
                "rifahtasnia312@gmail.com"]

    a=0
    for i in receiver:
        a +=1
        msg = EmailMessage()
        msg['Subject'] = "This is a test email"
        msg['From'] = sender
        msg['To'] = i
        msg.set_content(f"As you wanted to know, here is the informations for you to use: Temperature: {temp} °C \nMaximum Temperature: {maximum} °C \nMinimum Temperature: {minimum} °C")

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, app_password)
        server.send_message(msg)
        server.quit()
        print(f"Mission successful for the client {a}.")
    
    print("Mission Successful!")

def temp_alert():
    temp, maximum, minimum = temp_scrap()
    if temp is not None:
        send_email(temp, maximum, minimum)

    else:
        print("Fail to send")


schedule.every().day.at("09:00").do(temp_alert)
while True:
    schedule.run_pending()
    time.sleep(5)