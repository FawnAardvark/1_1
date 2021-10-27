while True:
  try:
    num1 = int(input("give a number"))
    num2 = int(input("give another number"))

except ValueError:
  print('Please input an integer only')
  continue
rem = num1%num2
if rem !=0:
  print('not divisable by 2, please try again')
  continue
else:
  print(rem)
break