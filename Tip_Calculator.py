print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split=int(input("How many people to split the bill?"))
total=tip/100*bill+bill
per_person=total/split
total_bill="{:.2f}".format(per_person)
print(f"Each person should pay $ {total_bill}")