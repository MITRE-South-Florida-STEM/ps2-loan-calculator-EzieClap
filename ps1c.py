# 'Data'
# annual_salary = float(input('Enter your annual salary: '))
# total_cost = 1000000
# semi_annual_raise = 0.07
# portion_down_payment = 0.25 * total_cost
# current_savings = 0
# r = 0.04
# monthly_salary = annual_salary/12
# m = 0

# 'Calculations'
# while m <= 36:
#   twoyr = annual_salary
#   if m == 24:
#     twoyr += annual_salary
#     print(str(m) + '-' + str(twoyr))
#   threeyr = annual_salary
#   if m == 36:
#     threeyr += twoyr
#     print(str(m) + '-' + str(threeyr))
#   m+=1
#   if m%6 == 0:
#     annual_salary += annual_salary * semi_annual_raise
#     print(str(m) + ' ' + str(annual_salary))


# # while current_savings < portion_down_payment:
# #   3yr = annual_salary * + current_savings*(r/12)
# #     m += 1
# #     if m%6 == 0:
# #         annual_salary += annual_salary * semi_annual_raise
  


# # print("Best saving rate: ", guess)
# # print("With current savings: ", current_savings)

'Data'
annual_salary_start = float(input('Enter your annual salary:'))
annual_salary = annual_salary_start
total_cost = 1000000
semi_annual_raise = 0.07

r = 0.04
portion_down_payment = 0.25*total_cost
current_savings  = 0.0
monthly_salary = annual_salary/12
num_of_month = 36

count = 0

start = 0
end = 10000
portion_saved = (start+end)/2    

'Calc'
while(((end-start)>1)and(current_savings>(portion_down_payment-100))):
    current_savings = 0
    for i in range(36):
        if ((i != 0)and(i%6 == 0)):
          