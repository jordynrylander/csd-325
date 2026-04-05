# Jordyn Rylander
# Module 11.2
# Recursive vs Non-Recursive Number Printing Program
# 3/15/2026


# Recursive Function - prints numbers from 1 up to n using recursion.
# the function will print numbers from 1 to n
# The base case stops the recursion when n = 1.

def recursive_print(n):

    # base case 
    if n == 1:
        print(1)

    # recursive case
    else:
        recursive_print(n - 1)  # call function again with smaller number
        print(n)                # print current number

# Non-Recursive Function
# The function will print numbers from 1 up to n using a loop.
# Instead of calling itself, it uses a for-loop to count upward from 1 to n.

def loop_print(n):

    
    for i in range(1, n + 1):
        print(i)

# This part asks the user for input and checks number is valid

# Ask user for a number
num = int(input("Enter a positive integer: "))

# Input validation loop
# This prevents 0 or negative numbers
while num <= 0:
    print("Error: Please enter a number greater than 0.")
    num = int(input("Enter a positive integer: "))


# Call Recursive Function
print("Starting Recursive Function")

recursive_print(num)

print("End Recursive Function")


# Call Non-Recursive Function

print("Starting Non-Recursive Function")

loop_print(num)

print("End Non-Recursive Function")
