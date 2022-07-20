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

def computing_shapes():  
    
    """ This function created by
    <-- DarkLib developers  --> """

    oper = int(input("what kind of operations you want?\nArea => 1\nCircumference => 2 : "))  
    shap = input("what is the shape?\nrectangle  r\nsquare => s\ncircle => c\ntriangle => t\nTrapezoidal => tr\nCylinder => cy\nParallelogram  => pa\n : ")  
    if shap == "r": 
        w = float(input("enter  the width: "))  
        l = float(input("enter the length: "))  
        if w < 0 or l < 0:  
            print("do not enter negative value")  
        elif oper == 1:  
            print(f"the area of rectangle = {w * l}")  
        elif oper == 2:  
                print(f"the circumference of rectangle = {2*(w + l)}")  
    elif shap == "s":  
        l = float(input("enter the rib: "))  
        if l < 0:  
            print("do not enter negative value")  
        elif oper == 1:  
                print(f"the area of square = {l ** 2}")  
        elif oper == 2:  
                print(f"the circumference of square = {l*4}")  
    elif shap == "c":  
        r = float(input("enter the radius: "))  
        if r < 0:  
                print("do not enter negative value")  
        elif oper == 1:  
                print(f"the area of circle = {3.14*(r**2)}")  
        elif oper == 2:  
            print(f"the circumference of circle = {2*3.14*r}")  
    elif shap == "t":  
        if oper == 1:  
            x = float(input("enter the triangles base: "))  
            y = float(input("enter the height: "))  
            if x < 0 or y < 0:  
                 print("do not enter negative value")  
            else:  
                print(f"the area of triangle = {0.5*x*y}")  
        elif oper == 2:  
            x = float(input("enter the first rib: "))  
            y = float(input("enter the second rib: "))  
            z = float(input("enter the third rib: "))  
            if x < 0 or y < 0 or z < 0:  
                print("do not enter negative value")  
            else:  
                print(f"the circumference of triangle = {x + y + z}") 
    elif shap == 'tr': 
        if oper == 1: 
            x = int(input('enter the first base: ')) 
            y = int(input('enter the second base: ')) 
            z = int(input('enter the height: ')) 
            if x == 0 or y == 0 or z == 0: 
                print("do not enter negative value")  
            else: 
                print(f'the area of Trapezoidal = {((x+y)/2) * z}') 
        elif oper == 2: 
            x1 = int(input('enter the fist rib: ')) 
            x2= int(input('enter the fist rib: ')) 
            x3 = int(input('enter the fist rib: ')) 
            x4 = int(input('enter the fist rib: ')) 
            if 0 in [x1, x2, x3, x4]: 
                print("do not enter negative value")  
            else: 
                print(f"the circumference of Trapezoidal = {x1 + x2 + x3 + x4}") 
    elif shap == "cy": 
        if oper == 1: 
            r = int(input("enter the radius of cylinders base: ")) 
            h = int(input("enter the height of cylinders side area: ")) 
            if r < 0 or h < 0: 
                print("do not enter negative value") 
            else: 
                area_of_base_for_cylinder = 3.14*(r**2) 
                side_area_of_cylinder = 2*3.14*r*h 
                print(f"the side area of cylinder = {side_area_of_cylinder}") 
                print(f"the total area of cylinder = {(2*area_of_base_for_cylinder) + (side_area_of_cylinder)}") 
    elif shap == "pa": 
        if oper == 1: 
            b = float(input("enter the parallelograms base: ")) 
            h = float(input("enter the parallelogram`s height: ")) 
            if b < 0 or h < 0: 
                print("do not enter negative value") 
            else: 
                print(f" the area of parallelogram = {b*h}") 
        elif oper == 2:
            x1 = float(input("enter the lenght of big rib: ")) 
            x2 = float(input("enter the lenght of small rib: "))
            if x1 < 0 or x2 < 0:
                print("do not enter negative values")
            else:
                print(f"the circumference of parallelogram = {2*(x1+x2)}")

#----------------------------------------------- 17

