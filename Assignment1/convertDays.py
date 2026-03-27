total_days = int(input("Enter days :"))

years = total_days // 365
weeks = (total_days % 365) // 7
days = (total_days % 365) % 7


print(f'years: {years}')
print(f'weeks: {weeks}')
print(f'days: {days}')