def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a×b
def div(a,b):
	return a÷b
def mod(a,b):
	return a%b
def exp(a,b):
	return a**b
def flo(a,b):
	return a//b

print("simple calculator")
choice=input("enter your operator ")
num1=input("enter your first operand")
num2=input("enter your second operand")
if choice == '+':
	print (add(num1,num2))
elseif choice == '-':
	print(sub(num1,num2))
elseif choice == '×':
	print(mul(num1,num2))
elseif choice == '÷':
	print(div(num1,num2))
elseif choice == '%':
	print(mod(num1,num2))
elseif choice== '**':
	print(exp(num1,num2))
else 
  print("invalid operator")