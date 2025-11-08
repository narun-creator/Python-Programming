principal = int(input("Please enter your principal: "))
rate_of_interest =int(input("Please enter your rate_of_interest: "))
time_period = int(input("Please enter your time_period: "))
simple_interest = (principal * rate_of_interest * time_period)/100
print("Your simple interest is: ", simple_interest)
amount = principal + simple_interest
print("Total amount:", amount)