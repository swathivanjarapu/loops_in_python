num=int(input('enter the num'))
temp=num
sum=0
digit=0
while temp>0:
	digit=temp%10
	sum=sum+digit**3
	temp=temp//10
if sum==num:
	print(num,'armstrog num')
else:
	print(num,'not armstrong num')
	