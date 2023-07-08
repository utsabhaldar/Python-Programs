# "()" this is for "tupple" object
# it is optional. It means it can be written without "()"
# it is by default
# names = ["Utsab", "Abhishek", "Shreya", "Amrita", "Anu", "Anand"] - this is not tupple object
# names = ("Utsab", "Abhishek", "Shreya", "Amrita", "Anu", "Anand") - this is a tupple object
# scores = (2,4,5,7,7,9)-this is a tupple object
# scores = [2,4,5,7,7,9]-this is not a tupple object

names = ("Utsab", "Akshay", "Subhadip", "Abhishek", "Shreya", "Amrita", "Anu", "Anand")

# "tupple" object does not support item assignment

print(names.index("Utsab"))
print(names.index("Anu"))
print(names.index("Anand"))

print(names.count("Shreya"))
print(names.count("Amrita"))
print(names.count("Akshay"))



scores = (2,4,5,7,7,9)

print(scores.index(2))
print(scores.index(9))
print(scores.index(7))

print(scores.count(4))
print(scores.count(7))
print(scores.count(9))


