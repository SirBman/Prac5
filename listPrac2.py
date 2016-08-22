"""List Practice 2"""

numbers = []

numCount = int(input("How many numbers do you want to list?"))
for i in range (0,numCount,1):
    num = int(input("Please enter a number:"))
    numbers.append(num)

print("The first number is:", numbers[0])
print("The last number is: ", numbers[-1])
print("The smallest number is:", min(numbers))
print("The largest number is:", max(numbers))
print("The average of the numbers is:", sum(numbers)/len(numbers))




