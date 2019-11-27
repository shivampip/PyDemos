from datetime import datetime, timedelta
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def tick():
    scheduler.print_jobs()                     
    print('Tick! The time is: %s' % datetime.now())





if(__name__ == '__main__'):
    scheduler.start()
    
    print("adding jobs")
    #scheduler.add_job(tick, 'interval', seconds=3)
    j1= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 3))
    j2= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 4))
    j3= scheduler.add_job(tick, "date", next_run_time= datetime.now()+ timedelta(seconds= 6))
    print(j1.id) 
    scheduler.remove_job(j1.id)
    scheduler.remove_job(j3.id) 
    
    #print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        while True: # This is here to simulate application activity (which keeps the main thread alive).
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() # Not strictly necessary if daemonic mode is enabled but should be done if possible
        