num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))

product = num1 * num2 
print (f" {num1} x {num2} = {product}")

if product == 0:
    print("the result is positive and negative")
elif product < 0 : 
    print("the result is negative")
elif product > 0 :
    print("the result is positive") 
    
