#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

total_bill=input("What was the total bill? ")

tip_percentage=input("What percentage tip would you like to give? 10, 12, or 15? ")

split_person=input("How many people to split the bill ")

tip_amount=(int(tip_percentage)/100*float(total_bill))/int(split_person)

split_amount=float(total_bill)/int(split_person)

individual_amount=split_amount+tip_amount

round_float = round(individual_amount,2)

round_float="{:.2f}".format(individual_amount)

print(f"Each person should pay : {round_float}")

#code written by me with help of google to round the float value to 2 decimal places