planned_stops = input()

command = input()

while command != 'Travel':

    command = command.split(':')

    if 'Add Stop' in command:
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(planned_stops):
            planned_stops = planned_stops[:index] + string + planned_stops[index:]
        print(planned_stops)

    elif 'Remove Stop' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(planned_stops) and 0 <= end_index < len(planned_stops):
            planned_stops = planned_stops[:start_index] + planned_stops[end_index + 1:]
        print(planned_stops)

    elif 'Switch' in command:
        old_string = command[1]
        new_string = command[2]
        if old_string in planned_stops:
            planned_stops = planned_stops.replace(old_string, new_string)
        print(planned_stops)

    command = input()

print(f'Ready for world tour! Planned stops: {planned_stops}')
