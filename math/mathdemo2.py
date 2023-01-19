
principal = 55000
interestrate = .05
num = 12 #12 months per year, compounding monthly
timet = 5 #5 years

amount = principal*(1+interestrate/num)**(num*timet)

print("The accrued amount is:", round(amount,2))
