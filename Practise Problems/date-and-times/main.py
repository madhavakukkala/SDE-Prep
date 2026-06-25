import datetime
import time

date = datetime.date.today
# print(date())

try:
    while True:
        yes = datetime.datetime.now()
        yes = yes.strftime("%H:%M:%S %m-%d-%Y")
        time.sleep(1)
        print("\r"+ yes , end="")
except KeyboardInterrupt:
    print("\nClock Stopped")