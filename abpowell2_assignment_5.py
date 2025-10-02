print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number:"))
step_count = 0
print(" Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ") #Ai was used to help get rid of the extra space after the final number(1) in the sequence my original code would produce this extra line
    if current_number % 2 == 0:
        current_number = current_number // 2
    elif current_number % 2 != 0:
        current_number = (current_number * 3) + 1
    step_count += 1 
print(current_number)
print(f"Steps:", end=" ") 
print(step_count, end="")
print("=== Challenge 2: Prime Number Checker ===")
prime = True # needed assistance in making the is or is not prime statment true or false this helped produce the correct output with no repeates 
n = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {n-1}...") 
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime (divisible by {i})")
        prime = False # needed assistance in making the is or is not prime statment true or false this helped produce the correct output with no repeates 
        break 
if prime: # needed assistance in making the is or is not prime statment true or false this helped produce the correct output with no repeates  
    print(f"{n} is prime!")
