days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for current_day in range(1, days_of_plunder + 1):

    total_plunder += daily_plunder

    if current_day % 3 == 0:
        total_plunder += 0.5 * daily_plunder

    if current_day % 5 == 0:
        total_plunder *= 0.70

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder * 100) / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")