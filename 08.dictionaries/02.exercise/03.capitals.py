counties = input().split(', ')
capitals = input().split(', ')

pairs = {coun: cap for coun, cap in zip(counties, capitals)}

for country, capital in pairs.items():
    print(f'{country} -> {capital}')
