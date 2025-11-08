name = input("Enter your name:")
print("Hello, " + name + "!")

age = int(input("Enter your age:"))
print("You will be ", age + 1, " next year.")

price= float(input("Enter your price:"))
discount = price * 0.1
print("Discount is:", discount)

answer = input("Are you a student? yes or no:")
is_student = answer == "yes"
if is_student:
    print("Welcome Student.")
else:
    print("Hello Guest.")