class Calculate:
    # Addition
    def add(self, *args):
        return sum(args)

    # Subtraction
    def sub(self, data1, data2):
        if(data1>data2):
            return (data1 - data2)
        
        elif(data1<data2):
            return (data2 - data1)
        
        else:
            return (data1 - data2)

    # Multiplication
    def multi(self, *args):
        c = 1
        for i in args:
            c =c*i
        return (c)

    # Division
    def div(self, data1, data2):
        if(data1==0 or data2==0):
            return ("cannot be proceed as you entered 0.")
        
        elif(data1>data2):
            return (data1 / data2)
        
        elif(data1<data2):
            return (data2 / data1)
        
        else:
            return (data1 / data2)


#User Input calculator project.
obj1 = Calculate()
print("Choose your function order number:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
answer = input("Enter your function: ")
ans = answer.lstrip()

#Proceed the user input.
if(ans == "1" or ans.lower() == "addition" or ans == "3" or ans.lower() == "multiplication"):
    number = []
    #add or multiplication process
    while(True):
        print("Enter your data one by one to proceed or enter 'none' to express you have entered all data. ")
        a = input("Enter data: ")
        print("")

        if(a.lower() == "none"):
            break
        number.append(int(a))   

    #Addition
    if(ans== "1" or ans.lower() == "addition"):
        print("The result is:", obj1.add(*number))
        print("")
    
    #Multiplication
    else:
        print("The result is:", obj1.multi(*number))
        print("")

#Division or subtract process.
elif(ans == "2" or ans.lower() == "subtraction" or ans == "4" or ans.lower() == "division"):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    #Subtraction
    if(ans == "2" or ans.lower() == "subtraction"):
        print("The result is", obj1.sub(a, b))
        print("")
    
    #Division
    else:
        print("The result is", obj1.div(a, b))
        print("")

else:
    print("Invalid Choice")