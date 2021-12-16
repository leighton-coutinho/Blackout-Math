import random
import blackout_utils
OPERATIONS = ['^', '/', 'x', '+', '-']

def  get_tokens_from_equation(line):
    '''(string --> list)
     Takes a string that contains digits from 0-9 and operators,
     it will then produce a list with these separated by a list
     and return the list
    >>>get_tokens_from_equation('1+2=5')
    [1,'+',2,'=',5]
    >>>get_tokens_from_equation('1+2=5/10')
    [1,'+',2,'=',5,'/',10]
    >>>get_tokens_from_equation("5^2++10=15")
    [5,'^',2,'+','^',10,'=',15]
    '''
    tokenlist = []
    numbers = []
    digit = ''
    end = len(line)
    for i in line:
        if i not in OPERATIONS and i != '=':
            digit += i
        if end == len(digit):
            tokenlist.append(int(digit))
        if i in OPERATIONS or i == '=':
            if digit != '':
                tokenlist.append(int(digit))
                end -= len(digit)
            tokenlist.append(i)
            end -= len(i)
            digit = ''
    return tokenlist


def  process_operations(ops, tokens):
    '''(list,list --> list)
     Takes two lists one with operations that should be performed
     from left to right and one with a list of tokens relating to an equation
     the funtion should return a list with the operations completed
    >>>process_operations(['+'],[1,'+',2,'-',5])
    [3,'-',5]
    >>>process_operations(['+','/'],[1,'+',2,'-',5,'/',10])
    [3,'-',0]
    >>> process_operations(['/'], [5, 'x', 4, '/', 2])
    [5,'x','2']
    '''
   
    completedops = []
    for i in tokens:
        completedops.append(i)
   
    j = 0
    while j < len(completedops):
        if completedops[j] in ops:
            if j == 0 or j == (len(completedops)-1):
                return completedops
            prevnum = completedops[j-1]
            prevnumi = j-1
            postnum = completedops[j+1]
            postnumi = j+1
            if completedops[j] == '/' and postnum == 0:
                    return completedops
            if type(prevnum) == int and type(postnum) == int:
                result = blackout_utils.do_op_for_numbers(completedops[j],prevnum,postnum)
                indices = [prevnumi,j,postnumi]
                completedops = blackout_utils.remove_from_list(completedops, indices)
                completedops.insert(prevnumi,result)
                j -= 2
        j += 1

    return completedops



def calculate(tokens):
    '''(list --> list)
     Takes one list which relates to mathematical tokens, this will have parentheses as well as
     as equal to sign, the order of math must be respected and we must evaluate everything
     on each side of the equal to sign
    >>>calculate([1,'+',2,'=',5,'/',10])
    [3,'=',0]
    >>> calculate([5, '=', 4, '/', 2])
    [5,'=','2']
    >>>calculate(['(',4, '/', 2,')','^',2,'=','(','(',7,'-',5,')','/',2,')','^',2])
    [4,'=',1]'''
    leftside = []
    rightside = []
    opsleft = []
    opsright = []
    opsbracl = []
    opsbracr = []
    copylist = []
    braclistl = []
    braclistr = []
    finallist = []
    bracketcheckl = False
    bracketcheckr = False
    
    equalindex = blackout_utils.find_first(tokens, '=')
    #checking for invalid equations
    if equalindex == None:
        return tokens
    if equalindex != blackout_utils.find_last(tokens, '='):
        return tokens
    for i in OPERATIONS:
        if equalindex == 0 or equalindex == (len(tokens)-1):
            return tokens
        if i == tokens[equalindex+1] or i == tokens[equalindex-1]:
            return tokens
        
    for i in tokens:
        copylist.append(i)
    leftside = copylist[:equalindex]
    rightside = copylist[(equalindex+1):]
    
    #evaluating things in brakcets on lefthand side 
    while bracketcheckl != None:
        if blackout_utils.find_first(leftside, '(') == None:
            bracketcheckl = None
        else:
            openbracl =  blackout_utils.find_last(leftside, '(')
            closebracl =  blackout_utils.find_first(leftside, ')')
            braclistl = leftside[(openbracl+1):closebracl]
            if '^' in braclistl:
                braclistl = process_operations(['^'],braclistl)
            if '/' or 'x' in braclistl:
                braclistl = process_operations(['/','x'],braclistl)
            if '+' or '-' in tokens:
                braclistl = process_operations(['+','-'],braclistl)
            differencel = []
            for i in range(openbracl,(closebracl+1)):
                differencel.append(i)
            leftside = blackout_utils.remove_from_list(leftside, differencel)
            leftside.insert(openbracl,braclistl[0])
            for i in opsbracl:
                opsbracl.remove(i)
        
        #evaluating things in brackets on righthand side
        while bracketcheckr != None:
            if blackout_utils.find_first(rightside, '(') == None:
                bracketcheckr = None
            else:
                openbracr =  blackout_utils.find_last(rightside, '(')
                closebracr =  blackout_utils.find_first(rightside, ')')
                braclistr = rightside[(openbracr+1):closebracr]
                if '^' in braclistr:
                    braclistr = process_operations(['^'],braclistr)
                if '/' or 'x' in braclistl:
                    braclistr = process_operations(['/','x'],braclistr)
                if '+' or '-' in tokens:
                    braclistr = process_operations(['+','-'],braclistr)
                differencer = []
                for i in range(openbracr,closebracr+1):
                    differencer.append(i)
                rightside = blackout_utils.remove_from_list(rightside, differencer)
                rightside.insert(openbracr,braclistr[0])
                for i in opsbracr:
                    opsbracr.remove(i)
      
      #evaluating left side
    if '^' in leftside:
        leftside = process_operations(['^'],leftside)
    if '/' or 'x' in leftside:
        leftside = process_operations(['/','x'],leftside)
    if '+' or '-' in tokens:
        leftside = process_operations(['+','-'],leftside)
        
    #evaluating right side
    if '^' in rightside:
        rightside = process_operations(['^'],rightside)
    if '/' or 'x' in tokens:
        rightside = process_operations(['/','x'],rightside)
    if '+' or '-' in tokens:
        rightside = process_operations(['+','-'],rightside)
    
    #creating final equation
    for i in leftside:
        finallist.append(i)
    finallist.append('=')
    for i in rightside:
        finallist.append(i)
        
    return finallist


def brute_force_blackout(line):
    '''(str --> list)
     Takes one string and continuously tries to remove two different characters to make
     the equality true, if it finds one then return the equation without the characters
     as a list of tokens, if it cannot then return None
     >>> brute_force_blackout('6-5=15^4/2')
    [6, '-', 5, '=', 1, '^', 42]
    >>> brute_force_blackout('288/24x6=18x13x8')
    [288, '/', 4, 'x', 6, '=', 18, 'x', 3, 'x', 8]
    >>> result = brute_force_blackout('4-3=0')
    >>> print(result)
    None
    '''
    firstchar = ''
    secondchar = ''
    chars= []
    for i in range(len(line)):
        for j in range(len(line)):
            firstchar = line[i]
            secondchar = line[j]
            linewofirst = line[:i] + line[(i+1):]
            linewochars = linewofirst[:j] + linewofirst[(j+1):]
            chars = get_tokens_from_equation(linewochars)
            listresult = calculate(chars)
            if len(listresult) == 3:
                isequivalent = blackout_utils.check_equivalency(listresult)
            else:
                isequivalent = False
            if isequivalent:
                return chars
            chars = []
    return None




def create_equation(n, pct_per_digit):
    '''(str --> list)
     Takes one postive odd integer and one float between one and zero,
     it will then return a randonly created math equation as a list of n elements.
     The second number will be the percent that a number in the equation will have
     more than one digit
    >>> create_equation(9, 0.0)
    [1, '/', 3, '=', 9, '^', 1, '^', 4]
    '''
    equationlist = []
    randomindex = 2
    equationlist.append(blackout_utils.generate_number(pct_per_digit))
    for i in range((n//2)):
        randomoperator = OPERATIONS[random.randint(0,4)]
        equationlist.append(randomoperator)
        nextnum = blackout_utils.generate_number(pct_per_digit)
        equationlist.append(nextnum)
    
    while (randomindex%2) == 0:
        randomindex = random.randint(0,(n-1))
    
    equationlist = blackout_utils.remove_from_list(equationlist, [randomindex])
    equationlist.insert(randomindex,'=')
        
        
    return equationlist
         

def find_solvable_blackout_equation(num_tries, n, pct_per_digit):
    '''(str --> list)
    Takes one postive integer, one positive odd integer and one float between one and zero,
    it will then return a solvab;e randonly created math equation as a list of n elements.
    The second number will be the percent that a number in the equation will have
    more than one digit. However, it will only try to create the equation with the
    number of tries given by the first argument
    >>> find_solvable_blackout_equation(1000, 7, 0.2)
    [37, '+', 9, '=', 1, 'x', 6]
    '''
    count = 0
    for i in range(num_tries):
        test = None
        trial_list = []
        trial_line = ''
        trial_list = create_equation(n, pct_per_digit)
        for element in trial_list:
            trial_line += str(element)
        print(i)
        test = brute_force_blackout(trial_line)
        if test != None:
            return trial_list
    return None

def menu():
    '''( --> )
    Takes no arguments, but will create a menu that will ask the user
    what they want to do, whether it be create and equation or try
    to solve an equation
    >>> menu()
    Please choose from the following:
     1 Solve equation
     2 Create equation
    Your choice: 2
    Enter number of tries: 1
    Enter length: 15
    Enter % of additional digit: 0
    No equation could be generated with the given inputs.
    Have a nice day!
    
    >>> menu()
    Welcome to Blackout Math!
    Please choose from the following: 
     1 Solve equation 
     2 Create equation 
     Your choice:1
    Please enter the equation without spaces: 5+10
    No solution found.
    Have a nice day!
    
    >>>menu
    Welcome to Blackout Math!
    Please choose from the following: 
     1 Solve equation 
     2 Create equation 
     Your choice:2
    Enter number of tries:10
    Enter % of additional digit:0
    Enter length: 15
    Equation:  [1, '^', 7, 'x', 7, '/', 6, 'x', 9, '=', 1, 'x', 4, '/', 8]
    Have a nice day!
    '''
    
    print('Welcome to Blackout Math!')
    print('Please choose from the following: \n1    Solve equation \n2    Create equation')
    user_choice = input('Your choice:')
    if user_choice == '1':
        userline = input('Please enter the equation without spaces: ')
        mysolution = brute_force_blackout(userline)
        if mysolution == None:
            print('No solution found.')
        else:
            print('Solution found: ', mysolution)
    elif user_choice == '2':
        num_tries = int(input('Enter number of tries: '))
        length = int(input('Enter length: '))
        pct = float(input('Enter % of additional digit: '))
        myresult = find_solvable_blackout_equation(num_tries, length, pct)
        if myresult == None:
            print('No equation could be generated with the given inputs.')
        else:
            print('Equation:', myresult)
    else:
        print("Invalid choice.")
    print("Have a nice day!")
    



