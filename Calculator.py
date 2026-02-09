def add(P,Q):
    P+Q
def subtract(P,Q):
    P-Q
def multiply(P,Q):
    P*Q
def divide(P,Q):
    P/Q   

print("select the operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice=int(input("Please enter 1, 2, 3, or 4:"))

num_1=int(input("Please enter the first number"))
num_2=int(input("Please enter the second number"))

if choice==1:
    print(num_1,'+', num_2, '=', add(num_1,num_2))

elif choice==2:
    print(num_1,'-', num_2, '=', subtract(num_1,num_2))

elif choice==3:
    print(num_1,'*', num_2, '=', multiply(num_1,num_2))

elif choice==4:
    print(num_1,'/', num_2, '=', divide(num_1,num_2))
else:
    print("This input is invalid")