a = 5
b = int(input("Enter a number"))

while(b!=a):
    if b<a:
     print(" Your number is lesser than the guess")
     b = int(input("Again,Enter a number"))
    else:
     print("Your number is Greater than the guess")
     b = int(input("Again,Enter a number"))
print(f"Ypur guessed it !")
