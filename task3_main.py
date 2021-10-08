from Project import Project
import time

from Task import Task


def main():
    print("Program started")


p1 = Project(1, "Project 1")
t1 = Task(1, "Task 1", 30, [], 0)
t2 = Task(2, "Task 2", 60, [1], 0)
t3 = Task(3, "Task 3", 240, [2], 0)


tasklist = [t1, t2, t3]
for x in tasklist:
    p1.addTask(x)

print("Total Time of all tasks: " + str(p1.total_time()) + " Hours")
t1.log_time(30) #Basically completing task 1 by logging 30 when task 1 is only 30 seconds
t2.close() #completes t2 by setting its percentage complete to 100%
print("Task 2 has been closed.")
print("Time left of the project: " + str(p1.time_left()) + " Hours")
print("Project Percentage Complete: %{:3.2f}".format(p1.percentage_complete()))


randomList = []
p1.get_task_and_children(1,randomList)
print("For task 1 the parent and children: " + str(randomList))
p1.get_task_and_children(2,randomList)
print("For task 2 the parent and children: " + str(randomList))
p1.get_task_and_children(3,randomList)
print("For task 3 the parent and children: " + str(randomList))