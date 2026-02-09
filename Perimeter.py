def square(x):
    perimeter=4*x
    print("Perimeter of the square is:",perimeter)

def rectangle(l,b):
    perimeter=2*(l+b)
    return perimeter

x=int(input("Enter the square's side length"))
square(x)
l=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadth of the rectangle"))
print(rectangle(l,b))