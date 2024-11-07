#welcome to tip calculator 
#what was the total bill?
#what percentage tip would you like to give? 10,12 or 15 ?
#how many people to spilit the bill ?
#each person should pay:

print("Welcome to tip calculator")
bill = float(input ("what was the total bill?"))
tip =int(input("what percentage tip would you like to give?"))
people = int(input("how many people split the bill?"))

tip_as_per = tip/100
total_tip_amount = bill * tip_as_per
total_bill = bill + total_tip_amount 
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: {final_amount} ")