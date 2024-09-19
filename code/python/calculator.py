#calculator
method = ""
a = ""
b = ""
def insert():
    #define a function to assign the variables
    a = float(input("Please insert the first number:"))
    b = float(input("Please insert the second number:"))
    return a, b
method = input("Which calculation do you want to do?(plus,minus,multiply or division,insert exit to exit)")

    #check the correction of the insert
if method in ["plus", "minus", "multiply", "division"]:
    while True:
    #define the calculation method
        if method == "plus":
            a, b = insert()
            r = a + b
            print("The result is:%.4f" % r)
    
        elif method == "minus":
            a, b = insert()
            r = a - b
            print("The result is:%.4f" % r)
    
        elif method == "multiply":
            a, b = insert()
            r = a * b
            print("The result is:%.4f" % r)
    
        elif method == "division":
            a, b = insert()
            if b != 0:
                r = a / b
                print("The result is:%.4f" % r)
            else:
                print("Division by 0 is not allowed!")
                continue
elif method == "exit":
        print("goodbye!")
else:
    print("Insert error!")