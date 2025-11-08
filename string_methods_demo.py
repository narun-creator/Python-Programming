# lower method
original = "Hello World"
Lowered = original.lower()
print("Lowercase: ", Lowered)

# upper method
Uppered = original.upper()
print("Uppercase: ", Uppered)

# strip() method
messy = " Python "
cleaned = messy.strip()
print("After strip: ", cleaned)

# replace() method
text = "Java is powerful"
updated = text.replace("Java","Python")
print("After replace: ", updated)

# split() method
sentence = "Python is easy to learn"
words = sentence.split()
print("After split: ", words)

# find() method
text = "Learning Python is fun"
postion = text.find("Python")
print("Found at index: ", postion)

# title() method
heading = "Welcome to Python Programming"
formatted = heading.title()
print("Title case: ", formatted)

# capitalize() method
msg = "hello WORLD"
cleaned = msg.capitalize()
print("Capitalize case: ", cleaned)

#startswith() method
greeting = "Hello everyone"
print(greeting.startswith("Hello"))
print(greeting.startswith("Hi"))

# endswith() method
print(greeting.endswith("everyone"))
print(greeting.endswith("Hello"))

# count()method
sentence = "Python is easy. Python is powerful. Python is popular."
count = sentence.count("Python")
print("total count: ", count)

# isalpha() method
name = "Python"
print(name.isalpha())

