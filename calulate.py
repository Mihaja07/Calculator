from math import *

def calculate(string:str):
    #opened parenthesis
    if string.count('(') < string.count(')'):
        string = '(' * (string.count(')') - string.count('(')) + string
    #closed parenthesis:
    if string.count('(') > string.count(')'):
        string = string + ')' * (string.count('(') - string.count(')'))
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
        if index - 1 > 0:
            if string[index-1].isdigit():
                string = string[:index] + '*' + string[index:]
    #power
    string.replace('^', '**')
    print(string)
    #Multiplication
    string.replace('x', '*')
    try:
        result = eval(string)
        return str(result)
    except Exception as e:
        print(e)
        return None