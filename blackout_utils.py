#Leighton Coutinho Student ID:261016919 Coutinho Student ID:261016919
import math
import random

def do_op_for_numbers(op, num1, num2):
    '''(str,num,num --> num)
     Takes a string which represents a math opertor, and proceeds to do the operation
     with two integers that are also taken. If the operation is division, the result is rounded down
    to the nearest integer. If the operation is division and the result is infinity, return 0 instead.
    >>>do_op_for_numbers("+", 1, 2)
    3
    >>>do_op_for_numbers("/", 10, 7)
    1
    >>>do_op_for_numbers("x", 5, 10)
    50
    '''
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "x":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return 0
        else:
            result = math.floor(num1 / num2)
            return result
    elif op == "^":
        return num1 ** num2
    else:
        return "invalid operator"

def remove_from_list(my_list, indices):
    '''(list,list --> list)
     Takes a two lists, the second list is of indices that we want to remove. The function
     will create a new list of the first list without the indices which will then be returned.
    >>>remove_from_list([1,5,9,10,11,12], [0,2,4])
    [5,10,12]
    >>>remove_from_list(['I','like','you'], [0,2])
    ['like']
    >>>remove_from_list(['a','b','c','d'], [1,3])
    ['a','c']
    '''
    #i need to get this to work for when there are two of the same element but only one of their indices is present, nested brackets 
    copylist = []
    copyindices = []
    for element in my_list:
        copylist.append(element)
    for element in indices:
        copyindices.append(element)
    copyindices.sort()
    for i in range(len(copyindices)):
        for j in range(len(my_list)):
            if copyindices[i] == j:
                copylist.pop(copyindices[i])
                if i < (len(copyindices)-1):
                    for k in range(len(copyindices)):
                         copyindices[k] -= 1
                    
        
    return copylist
        


def find_last(my_list, x):
    '''(list,anytype --> num)
     Takes a lists and a value of any type, it will then return the last index of the given value of any type
     but if it cannot be found it will return None
    >>>find_last([1,5,9,10,11,12], 9)
    2
    >>>find_last(['I','like','you'], 'like')
    1
    >>>find_last(['a','b','c','b'], 'b')
    3
    '''
    index = len(my_list) - 1
    while index >= 0:
        if x == my_list[index]:
            return index
        index -= 1
    return None
    
    
def find_first(my_list, x):
    '''(list,anytype --> num)
     Takes a lists and a value of any type, it will then return the first index of the given value of any type
     but if it cannot be found it will return None
    >>>find_first([1,5,9,9,9,12], 9)
    2
    >>>find_first(['I','like','you'], 'like')
    1
    >>>find_first(['a','b','c','b'], 'b')
    1
    '''
    index = 0
    while index < len(my_list):
        if x == my_list[index]:
            return index
        index += 1
    return None


def generate_num_digits(pct_per_digit):
    '''(num --> num)
    generate a random number between 0 and 1 and check if it is greater than the input float. We start our int with
    1, if the number generated is not greater than the input float then we increase this number untill we gain
    a random number that is greater or equal to the float
    >>>random.seed(1337)
    >>>generate_num_digits(0)
    1
    >>random.seed(9001)
    >>generate_num_digits(0.5)
    3
    '''
    count = 1
    myrandompercent = random.random()
    while myrandompercent < pct_per_digit:
        count = count + 1
        myrandompercent = random.random()
    return count
        
def generate_number(pct_per_digit):
    '''(num --> num)
    generate a random number that contains the number of digits which are specified by the
    previous function and return this number
    >>>random.seed(1337)
    >>>generate_num_ber(0)
    9
    >>random.seed(9002)
    >>generate_number(0.5)
    41700
    '''
    mynumofdigits = generate_num_digits(pct_per_digit)
    start = 10**(mynumofdigits - 1)
    stop = (10**mynumofdigits) - 1
    return random.randint(start,stop)

def check_equivalency(tokens):
    '''(list --> bool)
    checks if 2 elements in a list which are separated by an equal to sign are
    indeed equal to eachother and returns the boolean
    >>>check_equivalency([2,'=',4])
    False
    >>check_equivalency([2,'x',4])
    False
    >>>check_equivalency([2,'=',2])
    True
    '''
    check3elements = False
    checkoperator = False
    checkequivalence = False
    if len(tokens) == 3:
        check3elements = True
    if tokens[1] == '=':
        checkoperator = True
    if tokens[0] == tokens[2]:
        checkequivalence = True
    if check3elements and checkoperator and checkequivalence:
        return True
    else:
        return False
    




    
               
            
        

