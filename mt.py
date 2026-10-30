import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


thread1 = threading.Thread(target=walk_dog)
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()



thread1.join()
thread2.join()
thread3.join()


print("all done")

