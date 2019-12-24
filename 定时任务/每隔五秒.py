import threading
import datetime


def do_job():
    times = datetime.datetime.now()
    print('Just do it, time: %s' % times)
    global timer
    timer = threading.Timer(5, do_job)
    timer.start()

timer = threading.Timer(1, do_job)
timer.start()