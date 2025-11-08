age = 18
if age >= 18:
    print("You are old enough to vote.")
    has_id = True
    if has_id:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are not old enough to vote.")

mark = 91
if mark >= 50:
    if mark >= 90:
        print("You passed with distinction.")
    else:
        print("You passed the test.")
else:
    print("You failed the test.")

a = 2
b = 6
c = 5
if a > b:
    if a > c:
        print("a is the greatest of the three.")
    else:
        print("c is the greatest of the three.")
else:
    if b > c:
        print("b is the greatest of the three.")
    else:
        print("c is the greatest of the three.")