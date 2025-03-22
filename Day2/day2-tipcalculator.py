# Tip Calculator

print('Welcome to the tip calculator.')
total = float(input('What was the total bill? $')) #100
people = int(input('How many people to split the bill? '))
percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
total_divided = total / people
# total minus the tip
each_total = total_divided + (percentage/100) * total_divided
print(f'Each person should pay: ${each_total:.1f}')