# Name: Jake Herman
# Section: CIS 115C
# Description: this program calculates monthly, annual, and lifetime payments on a loan
#              given a specific interest rate. Then, advice is offerred.

# importing math to use math.pow
import math
# principal is money borrowed
principal = input("How much money did you borrow? ")
# handle Value error that could occur when user types in ammount with dollar sign
if '$' in principal:
    # after splitting string, object needs to be casted back into a float to be used in calculations
    principal = float(principal.split('$')[1])
else:
    principal = float(principal)

years = float(input("How many years? "))
interest_rate = input("What is the interest rate? ")
# handle Value error that could occur when user types in ammount with percent sign
if '%' in interest_rate:
    interest_rate = float(interest_rate.split('%')[0])/100
else:
    interest_rate = float(interest_rate)

annual_income = input("What is your annual income?" )
# possible value error, handled same way are principal
if '$' in annual_income:
    annual_income = float(annual_income.split('$')[1])
else:
    annual_income = float(annual_income)

monthly_income = annual_income/12
# rounds to two decimal places, as values of money are being output
annual_payment = round((math.pow((1+interest_rate), years) * principal * interest_rate)/(math.pow((1+interest_rate),years) - 1), 2)
monthly_payment = round((math.pow((1+interest_rate), (years/12)) * principal * interest_rate)/(math.pow((1+interest_rate),(years/12)) - 1), 2)
lifetime_payment = annual_payment * years
# output of calculations, numbers must be casted to strings so they can be concatenated
print("Annual Payment: $" + str(annual_payment))
print("Monthly Payment: $" + str(monthly_payment))
print("Lifettime Payment: $" + str(lifetime_payment))
# offers advice specific to user's financial situation
if monthly_income < monthly_payment:
    if interest_rate > .05:
        print("you should refinance this loan")
    else:
        print("seek financial counseling")
else:
    print("stick to your payments, and your loan will be paid off in time")
