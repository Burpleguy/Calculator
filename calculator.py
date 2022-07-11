print("Basic  Calculator")
#non functionalprint("choose from the following options")
#non functional print("+,*,-,/")
print("choose 1 ofthe following options: +,-,/,*")
option = input()

if(option != '+'and option != '-' and option !=  '/'  and option != '*'):
  
  print("error!,please try again")
  a = int (input("enter first number:"))
  b = int (input("enter second number:"))

else:
  a = int (input("enter first number:"))
  b = int (input("enter second number:"))
  

if(option == '+'):
  print(a + b)
elif(option == '-'):
  print(a - b)
elif(option == '/'):
  print(a / b)
elif(option == '*'):
  print(a * b)
