centuries = int(input())

# 1 year = 365.2422 days
years = 100 * centuries
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')