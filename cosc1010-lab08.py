# Logan Cabanaw
# UWYO COSC 1010
# 11/5/2024
# Lab XX
# Lab Section: 16
# Sources, people worked with, help given to:
# your
# comments
# here

# Q1:
def integer_or_flt(num):
    list(num)
    dec_count = 0
    symbol_count = 0
    index = 0
    outcome = []
    for i in num:
        if i.isdigit() and i != ".":
            outcome.append("1")
        elif i == ".":
            dec_count += 1
            if dec_count > 1 or index == len(num):
                return False, 
            outcome.append("2")
        elif i == "-" or i == "+":
            if index > 0:
                return False
        elif i.isalpha():
            return False
        else:
            return False
        index += 1
    if "2" in outcome and "1" in outcome:
        return(float(num))
    elif "1" in outcome:
        return(int(num))
    else:
        return False, print("5")

print("*" * 75)

# Q2:
def slope_intercept(m,b,lx,ux):
    Domain_Range = {}
    for x in range(lx,ux):
        Domain_Range[x] = m*x+b
    return(Domain_Range)

while True:
    m = integer_or_flt(input("(type 'exit' here to exit) m = "))
    b = integer_or_flt(input("b = "))
    lx = integer_or_flt(input("Lower x bound: "))
    ux = integer_or_flt(input("Upper x bound: "))
    if m is False or b is False or type(lx) == float or type(ux) == float:
        print("One of your inputs are not compatable with the slope_intercept function")
    elif m == "exit":
        break
    else:
        Domain_Range = {"x","y"}
        Domain_Range = slope_intercept(m,b,lx,ux)
        for n in Domain_Range:
            print(f"{n}    {Domain_Range[n]}")

# Q3:

while True:
    a = integer_or_flt(input("(type 'exit' to exit) a = "))
    b = integer_or_flt(input("(type 'exit' to exit) b = "))
    c = integer_or_flt(input("(type 'exit' to exit) c = "))
    if a is  False or b is  False or c is  False:
        print("Something went wrong!")
    if a == "exit" or b == "exit" or c == "exit":
        break
    else:
        Disc = ((b**2) - (4*a*c))
        x1 = round((-1*b + Disc**(1/2))/(2*a),4)
        x2 = round((-1*b - Disc**(1/2))/(2*a),4)
        print(f"{x1}, {x2}")
