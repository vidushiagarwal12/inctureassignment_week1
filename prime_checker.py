# Function to check prime number
def check_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Loop to check factors
    for i in range(2, int(number ** 0.5) + 1):
         # If divisible, then not prime
        if number % i == 0:
            return False

    # If no factor is found
    return True
    
num = int(input("Enter a number: "))
result = check_prime(num)
if result:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")