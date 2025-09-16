print("Enter a number (Numerator): ")
num1 = int(input())
print("Enter the second number (Denominator): ")
num2 = int(input())

if num1%num2==0:
    print("\n" + str(num1),  "is divisible by 8" + str(num2)) 
    
else:
    print("\n"+ str(num1), "is not divisible by "+ str(num2))
