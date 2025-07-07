a = float(input("Enter a number: "))
b= float(input("Enter another number: "))
add = a+b
sub = a-b
mul = a*b
if b!=0:
    div = a/b
    mod_div = a%b
    floor_div=a//b
else:
    div = "undefined"
    mod_div = "undefined"
    floor_div = "undefined"
print("\nRESULTS:")
print("1) Addition = ",a ,"+ ",b ,"= ", add )
print("2) Subtraction = ",a ,"- ",b ,"= ", sub )
print("3) Multiplication = ",a ,"X ",b ,"= ",mul )
print("4) Division = ",a ,"/ ",b ,"= ",div )
print("5) Modulo Division = ",a ,"% ",b ,"= ",mod_div )
print("6) Floor Division = ",a ,"// ",b ,"= ",floor_div )