import json
import time

def publish_event(event):

    event["time"] = time.time()

    with open("events.log", "a") as f:
        f.write(json.dumps(event) + "\n")