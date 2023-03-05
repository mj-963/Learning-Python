age = eval(input("Whats your age: "))

if age < 5:
    print("too young for school")
elif age == 5:
    print("You need to be in Kindergarten")
elif (age > 5 ) and (age <= 17):
    grade = age - 5
    print(f"You need to be in grade {grade}")
else:
    print("You need to be in college")
