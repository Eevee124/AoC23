import re

file_path = "day2.txt"

with open(file_path, "r") as f:
    content = f.read()
    text = content.split('\n')

def task_1():
    counter = 8
    dict = {'red': 12, 'green': 13, 'blue': 14}
    invalid = []
    id = 0
    
    for i in range(0, len(text)):
        id += 1
        if i == 9 or i == 99:
            counter += 1
        text[i] = text[i][counter:]
        text[i] = re.split(';|, ', text[i])
        for j in range(0, len(text[i])):
            text[i][j] = text[i][j].split()
            #print(text[i][j])
            if not (dict[text[i][j][1]] >= int(text[i][j][0])):
                invalid.append(id)

    invalid = list(set(invalid))
    #print(len(text))
    #print(invalid)
    counter = 0

    for i in range(1, len(text) + 1):
        if not (i in invalid):
            counter += i

    return counter

def task_2():
    dict = {'red': 0, 'green': 0, 'blue': 0}
    counter = 8
    sum = 0
    
    for i in range(0, len(text)):
        if i == 9 or i == 99:
            counter += 1
        text[i] = text[i][counter:]
        text[i] = re.split(';|, ', text[i])
        for j in range(0, len(text[i])):
            text[i][j] = text[i][j].split()
            if dict[text[i][j][1]] < int(text[i][j][0]):
                dict[text[i][j][1]] = int(text[i][j][0])

        sum += dict['blue'] * dict['green'] * dict['red']
        dict = {'red': 0, 'green': 0, 'blue': 0}

    return sum

"""CAN ONLY RUN ONE OR THE OTHER"""

#print(task_1())
print(task_2())