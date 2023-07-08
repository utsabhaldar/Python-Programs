# int = age

age = int(input("enter your age:"))
# age=17
if age >=0 and age < 6:
    print("you are a child")

elif age >= 5 and age <18 :
    print("you are in school")
    
elif age >=18 and age <= 100:
    print ("You are an adult")
    print("You can vote")
    
else :
    print("invalid input")
    