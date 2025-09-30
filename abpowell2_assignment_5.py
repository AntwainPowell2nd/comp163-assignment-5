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
