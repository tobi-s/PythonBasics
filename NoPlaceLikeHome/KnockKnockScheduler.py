import datetime
import os
import sched
import time
from NoPlaceLikeHome import KnockKnock

s = sched.scheduler(time.time, time.sleep)
knockknockintervall= os.environ['KNOCKKNOCKINTERVALL']

def log(str):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str)


def doKnockKnock():
    log("--- Start --- Wake Up! KnockKnock...")
    try:
        KnockKnock.runNockNock()
    except:
        log("ERROR: Failed to run NockNock")
    nextExecution = datetime.datetime.now() + datetime.timedelta(hours=int(knockknockintervall))
    log("Next Execution: " + nextExecution.strftime("%Y-%m-%d %H:%M:%S"))
    log("--- End --- ... was fun. Going to sleep. Bye.")
    s.enterabs(nextExecution.timestamp(), 1, doKnockKnock)


def main():
    log("Start KnockKnockScheduler")
    log("Intervall is set to: " + knockknockintervall)
    s.enter(0, 1, doKnockKnock)
    s.run()


if __name__== "__main__":
    main()