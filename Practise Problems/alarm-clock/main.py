# import time
# import datetime
# import pygame

# def set_alarm(alarm_time):
#     print(f"Alarm time set succesfully")
#     sound_file = "music.mp3"
#     isrunning = True

#     while isrunning:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print('\r'+ current_time,end="")

#         if current_time == alarm:
#             print("\nWake up 🙉")
            
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#             try:
#                 while pygame.mixer.music.get_busy():
#                     time.sleep(1)
#             except KeyboardInterrupt:
#                 print("Alarm Stopped")
        
#             isrunning = False

#         time.sleep(1)

# if __name__ == '__main__':
#     alarm = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm)




import time, datetime, pygame

def set_alarm(alarm):
    print("Alarm set successfully")
    set_alarm(alarm)

alarm = input("Enter the alarm time (HH:MM:SS): ")
isrunning = True

while isrunning:
    currenttime = datetime.datetime.now().strftime('%H:%M:%S')
    print(currenttime)
    time.sleep(1)
    
    if currenttime == alarm:
        print("Wake Up 🙉")
        



        isrunning = False


if __name__ == '__main__':