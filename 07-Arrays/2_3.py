###
# Weekly expenses for different categories
# [Food, Transport, Utilities]
#
monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

food = 0
transport = 0
utilities = 0
total = 0
weekly_totals = []

for week in monthly_expenses:
    food += week[0]
    transport += week[1]
    utilities += week[2]

    week_total = sum(week)
    weekly_totals.append(week_total)
    total += week_total

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('---------------')
print('TOTAL:', total)