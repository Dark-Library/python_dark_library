def sub(n1, *numbers):
    """ This function created by
    <-- DarkLib developers  --> """ 

    List = [n1]               
    for num in numbers:
        List.append(num)
        n1 -= num
    return n1

# ----------------------------------------------- 1

def sum(*numbers):
    """ This function created by
    <-- DarkLib developers  --> """ 
    sum =0
    for number in numbers:
        sum +=number
    return sum

#----------------------------------------------- 2

def mult(n1, *numbers):
    """ This function created by
    <-- DarkLib developers  --> """ 
    for i in numbers:
        n1 *= i
    return n1

#----------------------------------------------- 3

def div(n1, *numbers):
    """ This function created by
    <-- DarkLib developers  --> """ 
    for i in numbers:
        try :            
            n1 /= i
        except ZeroDivisionError:
            return '"Zero Division Error"\nYou can not divide by zero'
        return n1

#----------------------------------------------- 4

def create_list(f_num, l_num,step):
    l = []
    for i in range(f_num, l_num + 1,step):
        l.append(i)
    return l 

#----------------------------------------------- 5

def reverse_str(string=str):
    return string[-1::-1]

#-----------------------------------------------  6

def indexc(List, element):
    for i in range(0, len(List)):
        if List[i] == element:
            return i

#-----------------------------------------------  7

def len_c(List):
    u=0
    for i in List:
        u += 1
        i = i
    return u
  
#----------------------------------------------- 8

def power(number, po_number):
    reslut = number ** po_number
    return reslut

#----------------------------------------------- 9

def cout(text,typecolor="w"):
    if typecolor=="r":
        print(f"\033[;31;m{text}\033[;37;m")
    elif typecolor=="w":
        print(f"\033[;37;m{text}")
    elif typecolor=="g":
        print(f"\033[;32;m{text}\033[;37;m")
    elif typecolor=="y":
        print(f"\033[;33;m{text}\033[;37;m")
    elif typecolor=="b":
        print(f"\033[;34;m{text}\033[;37;m")
    elif typecolor=="m":
        print(f"\033[;35;m{text}\033[;37;m")
    elif typecolor=="c":
        print(f"\033[;36;m{text}\033[;37;m")
    elif typecolor=="bl":
        print(f"\033[;30;m{text}\033[;37;m")
    else:
        print ("[error] -----> \033[;31;mtypecolor is wrong\033[;37;m")

#----------------------------------------------- 10

def capitalaize(text, small_capital='c'):
    t= text.split()
    x= " "
    for i in t:
        if small_capital == 's':
            x = x + str(i[0]).lower()
        else:
            x = x + str(i[0]).upper()
    return x
print(capitalaize('ha dsa sa'))

#----------------------------------------------- 11

def find(List,element):
    if element in List:
        return True
    else:
        return False

#----------------------------------------------- 12

def longest_word(phrase=str):
       x = phrase.split()
       List = [ ]
       for i in x:
             length = len(i)
             List.append(length)
       c = List.index(max(List))
       return x[c]

#----------------------------------------------- 13

def timeToSec(hour=0, minutes=0):
    return (hour*3600)+(minutes*60)

#----------------------------------------------- 14

def secToTime(s):
    return s/3600

#----------------------------------------------- 15

def shortest_word(phrase=str):
       x = phrase.split()
       List = [ ]
       for i in x:
             length = len(i)
             List.append(length)
       c = List.index(min(List))
       return x[c]

#----------------------------------------------- 16

