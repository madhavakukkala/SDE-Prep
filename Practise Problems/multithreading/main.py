import threading
import time



def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking the {first}.")

    
def take_out_trash():
    time.sleep(2)
    print("You take out the Trash.")

def get_mail():
    time.sleep(4)
    print("You get the mail.")



work1 = threading.Thread(target=walk_dog, args=("Scoooby",))
work1.start()
work2 = threading.Thread(target=take_out_trash)
work2.start()
work3 = threading.Thread(target=get_mail)
work3.start()

work1.join()
work2.join()
work3.join()

print("All works are complete")

# walk_dog()
# take_out_trash()
# get_mail()



