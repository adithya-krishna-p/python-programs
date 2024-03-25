# if else statements

a = int(input("enter your age:"))
print("your age is:",a)

# conditionaal operators
# >,<,>=,
# print(a>18)
# print(a!=18)
# print(a==18)
# print(a<=18)

if(a>18):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")
    print("no")



# if else 

num = int(input("enter a number: "))
if(num > 0):
    print("number is negative")
elif(num == 0):
    print("number is zero.")
elif(num == 999):
    print("number is special.")
else:
    print("I am happy now")
