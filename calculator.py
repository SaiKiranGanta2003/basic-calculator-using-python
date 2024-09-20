
def inp():
    try:
        num1=int(input('enter 1st element - '))
        num2=int(input('enter 2nd element - '))
    except:
        print('enter Numbers only')
        inp()
    print()
    print()
    return num1,num2

def add():
    a,b=inp()
    print(f'the Sum of {a} , {b} = {a+b}')
    print('---------------------------------------------------')
    print()
    print()

def sub():
    a,b=inp()
    print(f'the subration of {a} , {b} = {a-b}')
    print('---------------------------------------------------')
    print()
    print()

def mul():
    a,b=inp()
    print(f'the product of {a} , {b} = {a*b}')
    print('---------------------------------------------------')
    print()
    print()

def div():
    a,b=inp()
    if b==0:
        print('2nd number should not be zero try again')
        div()

    print(f'the division of {a} , {b} = {a/b}')
    print('---------------------------------------------------')
    print()
    print()

def floor():
    a,b=inp()
    if b==0:
        print('2nd number should not be zero try again')
        floor()
    print(f'the floor division of {a} , {b} = {a//b}')
    print('---------------------------------------------------')
    print()
    print()

def mod():
    a,b=inp()
    if b==0:
        print('2nd number should not be zero try again')
        mod()
    print(f'the modulo divison of {a} , {b} = {a%b}')
    print('---------------------------------------------------')
    print()
    print()


def power():
    try:
        a=int(input('which number you want to apply power -'))
        b=int(input('what is the power value -'))
    except:
        print('enter Numbers only')
        power()
    print(f'the power of {a} , {b} = {a**b}')
    print('---------------------------------------------------')
    print()
    print()

def Squareroot():
    import math
    try:
        num1=int(input('for which number you want to apply the square root -'))
    except:
        print('enter Numbers only')
        Squareroot()
    print(f'the square root value of the {num1} is {math.sqrt(num1)}')
    print('---------------------------------------------------')
    print()
    print()


def table():
    try:
        num1=int(input('which number table you want - '))
    except:
        print('enter Numbers only')
        table()
    for i in range(1,11):
        print(f' {num1} * {i} = {num1*i}')
    print('---------------------------------------------------')
    print()
    print()

def round1():
    try:
        num1=float(input('enter the float digit'))
    except:
        print('enter Numbers only')
        round1()
    print(f'the rounded value of the {num1} is {round(num1,2)}')
    print('---------------------------------------------------')
    print()
    print()

    


def main():
    print()
    print()
    print('Welcome to the calculator')
    print('---------------------------------------------------')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Floor Division')
    print('6.Modulo Division')
    print('7.Power')
    print('8.Square root')
    print('9.Table')
    print('10.Round')
    print()
    print()

    try:
        operator=int(input('enter the opeartion you want - '))
        if operator>10:
            print('Invalid Operator')
        else:
            pass
        print()
        print()
        if operator==1:
            add()
        elif operator==2:
            sub()
        elif operator==3:
            mul()
        elif operator==4:
            div()
        elif operator==5:
            floor()
        elif operator==6:
            mod()
        elif operator==7:
            power()
        elif operator==8:
            Squareroot()
        elif operator==9:
            table()
        elif operator==10:
            round1()
        
    except:
        print('invalid operator')
   
   
main()