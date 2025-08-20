flag = False
num = 67545

#num = int(input("enter a number "))  --> u can also try this by asking input from user

if num <= 1:
	print("It is not a prime number")

elif num > 1:
	for i in range(2, num):
		if (num % i) == 0:
			flag = True
			break
	if not flag:
		print(num, "is a prime number")

	else:
		print(num, "is not a prime number")


def primen(add):
	pass

