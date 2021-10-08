import time


class Task:
    id = 0
    description = None
    timeReq = 0
    preTask = None
    percentComp = 0

    def __init__(self, id, description, timeReq, preTask: list, percentComp):
        self.id = id
        self.description = description
        self.timeReq = timeReq
        self.preTask = preTask
        self.percentComp = percentComp

    def log_time(self, total_time=0, percentage=0):
        if total_time != 0:
            self.percentComp = (total_time / self.timeReq) * 100
        elif percentage != 0:
            self.percentComp = percentage
        else:
            print("no parameter was given. please enter one parameter")

    def close(self):
        self.percentComp = 100
