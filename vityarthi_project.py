import math
import sys
from decimal import Decimal, InvalidOperation, getcontext
import cmath
import time

getcontext().prec = 10

def inp_calc(x):
    while True:
        val = input(x)
        try:
            d=Decimal(val)
            return d
        except InvalidOperation:
            print("Invalid decimal number. Please try again.")


def calc():
    print("Available operations: +, -, *, /")
    q1=input("Enter the symbol from above: ")
    if q1 not in ['+', '-', '*', '/']:
        print("Invalid operation.")
        return

    a=inp_calc("Enter first number: ")
    b=inp_calc("Enter second number: ")

    try:
        if q1=='+':
            r0=a+b
        elif q1=='-':
            r0=a-b
        elif q1=='*':
            r0=a*b
        elif q1=='/':
            if b==0:
                print("Division by zero is undefined. Please try again.")
                return
            r0=a/b
        print(f"Result: {r0}\n")
    except Exception as e:
        print("Error during calculation:", e)


def calc_2d():
    print("\nChoose shape for area/perimeter calculation:")
    print("1. Square\n2. Rectangle\n3. Triangle\n4. Circle")
    q2=input("Enter no. corresponding to abive shape (1-4): ")

    #Square
    if q2=='1':
        s=inp_calc("Enter side length: ")
        if s<=0:
            print("Side length must be positive.")
            return
        ar=s**2
        p=s*4
        print(f"Area: {ar}, Perimeter: {p}\n")

    #Rectangle
    elif q2=='2':
        l=inp_calc("please enter length of rectangle: ")
        w=inp_calc("please enter width of rectangle: ")
        if l<=0 or w<=0:
            print("Length and width must be positive.")
            return
        ar= l*w
        p=2*(l+w)
        print(f"Area: {ar}, Perimeter: {p}\n")

    #Triangle
    elif q2=='3':
        q3=input("Type 1 for Heron's fromula and type 2 for Right Angled Triangle: ")
        #Triangle using Henro's

        if q3=='1':
            a=inp_calc("Please enter length of side a: ")
            b=inp_calc("please enter length of side b: ")
            c=inp_calc("please enter length of side c: ")

            # Check if triangle is valid
            if (a+b<=c) or (a+c<=b) or (b+c<=a) or a<=0 or b<=0 or c<=0:
                print("Invalid triangle sides. Triangle inequality must hold.")
                return

            s = (a+b+c) / 2  # semi-perimeter
            # Use math.sqrt for square root but convert Decimal to float safely
            ar=Decimal(math.sqrt(float(s*(s-a)*(s-b)*(s-c))))
            p=a+b+c
            print(f"Area: {ar}, Perimeter: {p}\n")

        elif q3=='2':
            b=inp_calc('Enter length of base: ')
            h=inp_calc('Enter length of height: ')
            hyp=((b**2)+(h**2))**Decimal('0.5')
            if (b+h<=hyp) or (b+hyp<=h) or (hyp+h<=b) or hyp<=0 or b<=0 or h<=0:
                print("Invalid triangle sides. Triangle inequality must hold.")
                return

            ar=Decimal(0.5)*b*h
            p=b+h+hyp
            print(f"Area: {ar}, Perimeter: {p}\n")

    #Circle
    elif q2=='4':
        rd=inp_calc("Please enter radius of the circle: ")
        if rd<=0:
            print("Radius must be positive. Try again.")
            return
        ar=Decimal(math.pi)*rd**2
        cf=2*Decimal(math.pi)*rd
        print(f"Area:{ar}, Circumference: {cf}\n")
    else:
        print("Invalid choice.")


def calc_3d():
    print("Available 3D shapes:")
    print("1. Cube\n2. Cuboid\n3. Sphere\n4. Cylinder")
    q4=input("Please enter no. corresponding to above shape (1-4): ")

    #Cube
    if q4=='1':
        s=inp_calc("Please enter length of any one of the sides of the cube: ")
        if s<=0:
            print("Side length must be positive.")
            return
        sa=6*s**2
        v=s**3
        print(f"Surface Area: {sa}, Volume: {v}\n")

    #Cubiod
    elif q4=='2':
        l=inp_calc("PLease enter length of the cuboid: ")
        w=inp_calc("Please enter width of the cuboid: ")
        h=inp_calc("Please enter height of the cuboid: ")
        if l<=0 or w<=0 or h<=0:
            print("All dimensions must be positive.")
            return
        sa = 2 * (l*w + w*h + h*l)
        v=l*w*h
        print(f"Surface Area: {sa}, Volume: {v}\n")

    #Sphere
    elif q4=='3':
        rd=inp_calc("Please enter sphere's radius: ")
        if rd<=0:
            print("Radius must be positive. Try again.")
            return
        sa=4*Decimal(math.pi)*rd**2
        v=(Decimal(4)/Decimal(3))*Decimal(math.pi)*rd**3
        print(f"Surface Area: {sa}, Volume: {v}\n")

    #Cyclinder
    elif q4=='4':
        rd=inp_calc("Please enter radius of the Cylinder: ")
        h=inp_calc("Please enter height of the cylinder: ")
        if rd<=0 or h<=0:
            print("Radius and height must be positive.")
            return
        sa=2*Decimal(math.pi)*rd*(rd+h)
        v=Decimal(math.pi)*rd**2*h
        print(f"Surface Area: {sa}, Volume: {v}\n")
    else:
        print("Invalid choice.")

def quad_eq_calc():
    print('General Quadratic Equation : ax^2 + bx + c = 0')
    a=round(float(eval(input("Enter the coefficient of x^2 (a): "))), 2)
    b=round(float(eval(input("Enter the coefficient of x (b): "))), 2)
    c=round(float(eval(input("Enter the constant (c): "))), 2)
    D=(b**2)-(4*a*c)
    if D>0:
        r1=round(((-b)+(D**0.5))/(2*a),2)
        r2=round(((-b)-(D**0.5))/(2*a),2)
        print(f'The roots of the equation {a}x^2 + {b}x +{c} are {r1},{r2}')
    elif D==0:
        r1=round(-b/(2*a),2)
        r2=round(-b/(2*a),2)
        print(f'The roots of the equation {a}x^2 + {b}x +{c} are {r1},{r2}')
    elif D<0:
        r1=(-b+cmath.sqrt(D))/(2*a)
        r2=(-b-cmath.sqrt(D))/(2*a)
        print(f'The roots of the equation {a}x^2 + {b}x +{c} are {r1},{r2}\n note:- [j=√-1]')

def stopwatch():
    print("Press Enter to start the stopwatch.")
    input()
    t0=time.time()
    print("Press Enter to stop the stopwatch.")
    input()
    t_end=time.time()
    t=t_end-t0
    print(f"Elapsed time: {t:.2f} seconds")

def main_prog():
    while True:
        print("Welcome to the program")
        print("Tasks this program can perform:")
        print("1. Perform a calculation (+, -, *, /)")
        print("2. Calculate area and perimeter of 2D shapes (square, triangle, rectangle, circle)")
        print("3. Calculate surface area and volume of 3D shapes (cube, cuboid, sphere, cylinder)")
        print("4. Roots of Quadratic equations")
        print('5. Stopwatch')
        print('6. Exit')

        q5=input("Enter 1, 2, 3, 4, 5 or 6: ")

        if q5=='1':
            calc()
        elif q5=='2':
            calc_2d()
        elif q5=='3':
            calc_3d()
        elif q5 == '4':
            quad_eq_calc()
        elif q5 == '5':
            stopwatch()
        elif q5=='6':
            print("Thank you for using the program.")
            sys.exit()
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, 5 or 6.")
            print('')


if __name__ == "__main__":
    main_prog()
