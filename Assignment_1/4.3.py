# WAP to add all the numbers from 1 to n and n is given by user.
n = int(input('Enter the number : '))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print('Sum is : ', sum)