'''
Description
Print the last digit of the given number.

Sample Input: 256

 

Sample Output: 6


'''

# Python Program to find the Last Digit in a Number

number = int(input("Please Enter any Number:"))

last_digit= number%10

print("The Last Digit in a Given Number %d = %d"%(number,last_digit))
