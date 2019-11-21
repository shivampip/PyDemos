import signal
import sys

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to stop')

import time
for i in range(20):
    time.sleep(1)
    print("Count: {}".format(i))
#signal.pause()

