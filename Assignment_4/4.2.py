#  WAP to print the table of n and n is given by user.
n = int(input('Enter the number: '))
print(' ')
print('Table of ' , n , ' : ')
for i in range (1,11):
    print(n , 'x' , i , '=' , n*i)