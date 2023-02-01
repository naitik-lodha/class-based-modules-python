import math_details  # Importing the module file to access its functions

n = int(input("Enter a number: "))
print(f"Factorial of {n} is : {math_details.factorial(n)}")
r = int(input("Enter r for permutation and combinations: "))
print(f"Permutation of {n} is : {math_details.permutation(n, r)}")
print(f"Combination of {n} is : {math_details.combination(n, r)}")
print(f"{n} is {math_details.armstrong(n)} number")
print(f"Reverse of {n} is : {math_details.reverse(n)}")
