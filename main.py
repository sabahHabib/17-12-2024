#print("My first program")
#price = 100
#qty = 50
#total = price*qty
#print("Total price is:", total)


# Print first 10 natural numbers using while loop
n = 1
while n < 11:
    print(n)
    n += 1

# Write a Python code to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n= 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")


# Calculate sum of all numbers from 1 to a given number
num = int(input("Enter number to get sum:"))
total = 0
for i in range(num+1):
    total = total + i
print(total)
# Print multiplication table of a given number
n = int(input("Enter number to get table:"))
for i in range(1, 11):
    print(i*n)
# Display numbers from a list using a loop
n=[1, 7, 9, 8, 6]
for i in n:
    print(i)
# Count the total number of digits in a number
n= int(input("Enter number to count:"))
counter = 0
while (n>0):
    counter+=1
    n=n//10

print(counter)
#Print list in reverse order using a loop

