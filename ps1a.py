'Data'
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_r=r/12
monthly_salary = annual_salary/12
m = 0

'Calculations'
while current_savings < total_cost*portion_down_payment:
  current_savings += current_savings * monthly_r + (monthly_salary*portion_saved)
print('Number of months: ' + str(m))

