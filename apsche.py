## https://apscheduler.readthedocs.io/en/3.0/userguide.html

from datetime import datetime, timedelta
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


scheduler = BackgroundScheduler()


def tick(text):
    print(f"{datetime.now()}: RUN: {text}")


def my_listener(event):
    if(event.exception):
        print(f'{event.job_id} The job crashed :(')
    else:
        print(f'{event.job_id} The job worked :)')


def circle():
    print("Circling.....")
    j1= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 3), kwargs= {"text": "Hello World 1"})
    j2= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 4), kwargs= {"text": "Hello World 2"})
    print("Two jobs added")



if(__name__ == '__main__'):
    scheduler.start()
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    
    
    print("adding jobs")

    scheduler.add_job(circle, "interval", minutes= 1)


    #scheduler.add_job(tick, 'interval', seconds=3)
    #j1= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 3), kwargs= {"text": "Hello World 1"})
    #j2= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 4), kwargs= {"text": "Hello World 2"})
    #j3= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 6), kwargs= {"text": "Hello World 3"})
    #print(j1.id) 
    #scheduler.remove_job(j1.id)
    #scheduler.remove_job(j3.id) 
    
    #scheduler.print_jobs()                     
    
    #print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        while True: # This is here to simulate application activity (which keeps the main thread alive).
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() # Not strictly necessary if daemonic mode is enabled but should be done if possible
        