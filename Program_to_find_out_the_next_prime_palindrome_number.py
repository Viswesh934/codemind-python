# Python3 program to find next palindromic
# prime for a given number.
import math as mt

def isPrime(num):

	if (num < 2 or num % 2 == 0):
		return num == 2
	for i in range(3, mt.ceil(mt.sqrt(num + 1))):
		if (num % i == 0):
			return False
	return True

def primePalindrome(N):
	for x in range(1, 100000):
	
		s = str(x)
		d = s[::-1]
		y = int(s + d[1:])
	
		if (y>=N and isPrime(y)):
			return y
	
n=int(input())
print(primePalindrome(n))

    