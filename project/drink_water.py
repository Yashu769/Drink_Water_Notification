import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Time to Hydrate !!",
            message = "Don't forget to drink water.You are basically a houseplant with more complicated emotions.",
            app_icon = "D:\projects\Drink_Water_Notification\drink_119593.ico",
            timeout = 10
        )
        time.sleep(60*60)