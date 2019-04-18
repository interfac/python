def in1():
 a=input("Enter the 1st number")
 b=input("Enter the 2nd number")
 return a,b
def mod():
 c, d=in1()
 print "The addition is ",c%d
def add():
 c, d=in1()
 print "The addition is ",c+d
def sub():
 c, d=in1()
 print "The subtraction is ",c-d
def mul():
 c, d=in1()
 print "The multiplication is ",c*d
def div():
 c, d=in1()
 print "The division is ",c/d
def pow():
 c,d=in1()
 print "The power is ", c**d

while True:
 print("Enter 1 for add")
 print("Enter 2 for sub")
 print("Enter 3 for mul")
 print("Enter 4 for div")
 print("Enter 5 for power")
 print("Enter 6 for mod")
 print("Enter 7 for quit")
 x=input("Choose Now\n")
 print(x)
 if x==1:
  add()
 elif x==2:
  sub()
 elif x==3:
  mul()
 elif x==4:
  div()
 elif x==5:
  pow()
 elif x == 6:
  mod()
 elif x == 7:
  break
 else:
  print("Wrong Choice")
