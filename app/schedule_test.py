import schedule
import time
import threading


def job():
    print("I'm working...")


schedule.every(1).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)


def scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)


t = threading.Thread(target=scheduled_tasks)
t.start()
while True:
    time.sleep(1)
    print("main")
