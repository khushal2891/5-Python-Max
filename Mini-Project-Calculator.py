a=input("Enter First number")
a=int(a)
op=input("Enter Operator / , * , + , - ")
b=input("Enter Second Number")
b=int(b)
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*" :
    print(a*b)
else :
    print("Invalid Operator")