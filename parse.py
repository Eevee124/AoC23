

file_path = "day1.txt"

with open(file_path, "r") as f:
    content = f.read()
    text = content.split('\n')

#print(text)

def task_1():
    print(text)

def task_2():
    pass


print(task_1(), task_2())
