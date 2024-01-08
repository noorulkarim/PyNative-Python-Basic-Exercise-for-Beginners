# Exercise 12: Calculate income tax for the given income by adhering to the rules below

income=int(input("Enter your Income: "))

if(income>0 and income<=10000):
    print("Your Tax is $ 0")
elif(income>10000 and income <=20000):
    print("Your Tax is $",income*0.1)
elif(income>=20000):
    tax=((income-20000)*0.2) + 1000
    print("Your Tax is $",int(tax))