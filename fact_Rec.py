def recu(n):
	if n==1:
		return n
	else:
		return n*recu(n-1)
num=int(input("Enter the number"))
if(num<0):
	print("Factorial doesn't exist for negative numbers")
elif num==0:
	print("Factorial of",num,"is","1")
else:
	print("Factorial of",num,"is",recu(num))
