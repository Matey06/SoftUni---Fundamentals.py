import re

destinations = input()

pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

matches = re.findall(pattern, destinations)

travel_points = 0
valid_places = []
for match in matches:
    place = match[1]
    valid_places.append(place)
    travel_points += len(place)

print(f"Destinations: {', '.join(valid_places)}")
print(f'Travel Points: {travel_points}')
