print("Enter your monthly income: ")
i= int(input())
print("Enter your total monthly expenses: ") 
x=int(input())
monthly_savings=i-x
projected_savings=monthly_savings*12+(monthly_savings*12*0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")
