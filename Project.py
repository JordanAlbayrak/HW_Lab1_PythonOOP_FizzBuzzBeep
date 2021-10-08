from Task import Task


class Project:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.taskList = []

    def addTask(self, t: Task):
        self.taskList.append(t)
        print("Task added with id: " + str(t.id))

    def list_task(self):
        for task in self.taskList:
            print("Task Id: " + str(task.id))

    def total_time(self):
        total_time = 0
        for task in self.taskList:
            total_time += task.timeReq
        return total_time

    def time_left(self):
        time_left = 0
        for task in self.taskList:
            time_left += task.timeReq - (task.percentComp * task.timeReq) / 100
        return time_left

    def percentage_complete(self):
        return ((self.total_time() - self.time_left()) / self.total_time()) * 100

    def get_task_and_children(self, project_id: int, list_prereq: list):
        for task in self.taskList:
            if task.id == project_id:
                list_prereq.append(task.id)
                for x in task.preTask:
                    if x not in list_prereq:
                        self.get_task_and_children(x, list_prereq)
            else:
                list_prereq.sort()

    def close_all(self, id, list):
        pass
