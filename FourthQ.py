import random
import time

def status_endpoint():
    if random.random() < 0.5:
        return False
    return True

def poll_status():
    log = []
    for attempt in range(3):
        ok = status_endpoint()
        if ok:
            log.append("success on attempt " + str(attempt + 1))
            return log
        else:
            log.append("fail on attempt " + str(attempt + 1))
            time.sleep(attempt + 1)
    log.append("gave up")
    return log


print(poll_status())