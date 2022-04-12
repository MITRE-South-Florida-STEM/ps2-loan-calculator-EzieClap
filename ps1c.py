'Data'
annual_salary = float(input('Enter your annual salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
m = 0

'Calculations'
while m <= 36:
  twoyr = annual_salary
  if m == 24:
    twoyr += annual_salary
    print(str(m) + '-' + str(twoyr))
  threeyr = annual_salary
  if m == 36:
    threeyr += twoyr
    print(str(m) + '-' + str(threeyr))
  m+=1
  if m%6 == 0:
    annual_salary += annual_salary * semi_annual_raise
    print(str(m) + ' ' + str(annual_salary))


# while current_savings < portion_down_payment:
#   3yr = annual_salary * + current_savings*(r/12)
#     m += 1
#     if m%6 == 0:
#         annual_salary += annual_salary * semi_annual_raise
  


# print("Best saving rate: ", guess)
# print("With current savings: ", current_savings)
