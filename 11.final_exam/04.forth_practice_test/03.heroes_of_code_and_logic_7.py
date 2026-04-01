number_of_heroes = int(input())
book_of_heroes = {}

for hero in range(number_of_heroes):
    hero_name, hit_points, mana = input().split()
    hit_points = int(hit_points)
    mana = int(mana)
    book_of_heroes[hero_name] = [hit_points, mana]

command = input()

while command != 'End':
    if 'CastSpell' in command:
        _, name, needed_mana, spell_name = command.split(' - ')
        needed_mana = int(needed_mana)
        if needed_mana <= book_of_heroes[name][1]:
            book_of_heroes[name][1] -= needed_mana
            remaining_mana = book_of_heroes[name][1]
            print(f'{name} has successfully cast {spell_name} and now has {remaining_mana} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

    elif 'TakeDamage' in command:
        _, name, damage, attacker = command.split(' - ')
        damage = int(damage)
        book_of_heroes[name][0] -= damage
        if book_of_heroes[name][0] > 0:
            remaining_health = book_of_heroes[name][0]
            print(f'{name} was hit for {damage} HP by {attacker} and now has {remaining_health} HP left!')
        else:
            del book_of_heroes[name]
            print(f'{name} has been killed by {attacker}!')

    elif 'Recharge' in command:
        _, name, mana_amount = command.split(' - ')
        mana_amount = int(mana_amount)
        if book_of_heroes[name][1] + mana_amount <= 200:
            book_of_heroes[name][1] += mana_amount
            print(f'{name} recharged for {mana_amount} MP!')
        else:
            recovered_mana = 200 - book_of_heroes[name][1]
            book_of_heroes[name][1] += recovered_mana
            print(f'{name} recharged for {recovered_mana} MP!')

    elif 'Heal' in command:
        _, name, health_amount = command.split(' - ')
        health_amount = int(health_amount)
        if book_of_heroes[name][0] + health_amount <= 100:
            book_of_heroes[name][0] += health_amount
            print(f'{name} healed for {health_amount} HP!')
        else:
            recovered_health = 100 - book_of_heroes[name][0]
            book_of_heroes[name][0] += recovered_health
            print(f'{name} healed for {recovered_health} HP!')

    command = input()

for current_hero, stats in book_of_heroes.items():
    print(current_hero)
    print(f'  HP: {stats[0]}')
    print(f'  MP: {stats[1]}')
