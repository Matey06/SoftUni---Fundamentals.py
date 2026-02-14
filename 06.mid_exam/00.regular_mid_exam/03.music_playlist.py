songs = input().split()
number_of_commands = int(input())

for current_command in range(number_of_commands):

    command = input()

    if command == 'Play':
        order = '\n'.join(songs)
        print(f'Songs to Play:\n{order}')

    elif command == 'Sort':
        songs.sort(reverse=True)

    elif 'Add' in command:
        command = command.split(' * ')
        new_song = command[1]
        if new_song not in songs:
            songs.append(new_song)
            print(f'{new_song} successfully added')

    elif 'Delete' in command:
        command = command.split(' * ')
        number_of_songs = int(command[1])
        if number_of_songs < len(songs):
            deleted_songs = []
            for _ in range(number_of_songs):
                popped_song = songs.pop(0)
                deleted_songs.append(popped_song)
            deleted = ', '.join(deleted_songs)
            print(f'{deleted} deleted')

    elif 'Shuffle' in command:
        command = command.split(' * ')
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(songs) and 0 <= index2 < len(songs):
            songs[index1], songs[index2] = songs[index2], songs[index1]
            print(f'{songs[index1]} is swapped with {songs[index2]}')

    elif 'Insert' in command:
        command = command.split(' * ')
        new_song = command[1]
        index = int(command[2])
        if 0 <= index < len(songs):
            if new_song not in songs:
                songs.insert(index, new_song)
                print(f'{new_song} successfully inserted')
            else:
                print('Song is already in the playlist')
        else:
            print('Index out of range')