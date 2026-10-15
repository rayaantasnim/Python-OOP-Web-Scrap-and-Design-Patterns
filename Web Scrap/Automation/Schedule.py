import schedule
import time
def task():
    print("The task is okay!")

schedule.every().day.at("21:05").do(task)

while True:
    time.sleep(1)
    schedule.run_pending()