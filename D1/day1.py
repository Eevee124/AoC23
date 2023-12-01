

file_path = "day1.txt"

with open(file_path, "r") as f:
    content = f.read()
    text = content.split('\n')

#print(text)

def task_1():
    first = -1
    last = -1
    temp = False
    numbers = []

    for line in text:
        for char in line:
            if char.isdigit() and not temp:
                first = char
                last = char
                temp = True
            elif char.isdigit():
                last = char
        temp = False
        numbers.append(int(first + last))
    
    return sum(numbers)


def task_2_firstattempt():

    #bugs when encountering eightwo

    dict = {'one': '1', 'two': '2', 'three': '3', 
            'four': '4', 'five': '5', 'six':'6',
            'seven': '7', 'eight': '8', 'nine':'9'}
        
    first = -1
    last = -1
    temp = False
    numbers = []
    check = ''

    for line in text:
        for element in dict:
            if element in line:
                line = line.replace(element, dict[element])
        for char in line:
            check += char
            if char.isdigit() and not temp:
                first = char
                last = char
                temp = True
            elif char.isdigit():
                last = char
            
        temp = False
        numbers.append(int(first + last))

def task_2():

    dict = {'one': '1', 'two': '2', 'three': '3', 
            'four': '4', 'five': '5', 'six':'6',
            'seven': '7', 'eight': '8', 'nine':'9'}
    
    firsts = []
    temp = ''
    check = False
    first = -1
    last = -1
    
    for line in text:
        for n in range(0, len(line)):
            if line[n].isdigit() and not check:
                first = line[n]
                check = True
            
            temp += line[n]

            for el in dict:
                if el in temp and not check:
                    first = dict[el]
                    check = True
        check = False
        firsts.append(first)
        temp = ''
    
    seconds = []
    
    for line in text:
        for n in range(1, len(line) + 1):
            if line[-n].isdigit() and not check:
                last = line[-n]
                check = True
            
            temp = line[-n] + temp
            #print(temp)

            for el in dict:
                if el in temp and not check:
                    last = dict[el]
                    check = True
        check = False
        seconds.append(last)
        temp = ''
    
    numbers = []

    for i in range(0, len(firsts)):
        numbers.append(int(firsts[i] + seconds[i]))

    #print(numbers)

    return sum(numbers)


print(task_1())
print(task_2())
