monthly_income = int(input("Enter your monthly income: ")) #request user to input their monthly income
monthly_expenses = int(input("Enter your total monthly expenses: ")) #request user to input their monthly expenses

monthly_savings = monthly_income - monthly_expenses #calculate monthly savings by subtracting expenses from income
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05) #project annual savings assuming a 5% savings rate

print("Your monthly savings are $",monthly_savings) #display monthly savings
print("Projected savings after one year, with interest, is: $",projected_annual_savings)