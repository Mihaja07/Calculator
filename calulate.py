from math import cos, sin, exp

def calculate(string:str):
    #opened parenthesis
    if string.count('(') < string.count(')'):
        string = '(' * (string.count(')') - string.count('(')) + string
    #closed parenthesis:
    if string.count('(') > string.count(')'):
        string = string + ')' * (string.count('(') - string.count(')'))
    #Multiplication
    string = string.replace('x', '*')
    #exponent
    index = 0
    while string.count('e') > string.count('exp'):
        index = string.find('e', index)
        last_digit_index = index+1
        for i in range(last_digit_index, len(string)):
            if not string[last_digit_index].isdigit():
                break
            last_digit_index = i
        string = string[:index+1] + "xp(" + string[index+1:last_digit_index+1] + ")" + string[last_digit_index+1:]
        if index - 1 >= 0:
            if string[index-1].isdigit():
                string = string[:index] + '*' + string[index:]
    #cos
    index = 0
    for i in range(0, string.count('cos')):
        index = string.find('cos', index)
        if index - 1 >= 0:
            if string[index-1].isdigit() or string[index-1] not in ('+', '-', '/', 'x'):
                string = string[:index] + '*' + string[index:]
    #sin
    index = 0
    for i in range(0, string.count('sin')):
        index = string.find('sin', index)
        if index - 1 >= 0:
            if string[index-1].isdigit() or string[index-1] not in ('+', '-', '/', 'x'):
                string = string[:index] + '*' + string[index:]
    #power
    string = string.replace('^', '**')
    
    print(string)

    try:
        result = eval(string)
        return str(result)
    except Exception as e:
        print(e)
        return None