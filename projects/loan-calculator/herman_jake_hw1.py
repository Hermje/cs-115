# Name: Jake Herman
# Section: CIS 115C
# Description: this program calculates monthly, annual, and lifetime payments on a loan
#              given a specific interest rate. Then, advice is offerred.

import math

principal = input("How much money did you borrow? ")

if '$' in principal:
    principal = float(principal.split('$')[1])
else:
    principal = float(principal)

years = float(input("How many years? "))
interest_rate = input("What is the interest rate? ")

if '%' in interest_rate:
    interest_rate = float(interest_rate.split('%')[0])/100
else:
    interest_rate = float(interest_rate)

annual_income = input("What is your annual income?" )

if '$' in annual_income:
    annual_income = float(annual_income.split('$')[1])
else:
    annual_income = float(annual_income)

monthly_income = annual_income/12

annual_payment = round((math.pow((1+interest_rate), years) * principal * interest_rate)/(math.pow((1+interest_rate),years) - 1), 2)
monthly_payment = round((math.pow((1+interest_rate), (years/12)) * principal * interest_rate)/(math.pow((1+interest_rate),(years/12)) - 1), 2)
lifetime_payment = annual_payment * years

print("Annual Payment: " + str(annual_payment))
print("Monthly Payment: " + str(monthly_payment))
print("Lifettime Payment: " + str(lifetime_payment))

if monthly_income < monthly_payment:
    if interest_rate > .05:
        print("you should refinance this loan")
    else:
        print("seek financial counseling")
else:
    print("stick to your payments, and your loan will be paid off in time")
