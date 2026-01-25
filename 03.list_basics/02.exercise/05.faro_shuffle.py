deck_of_cards = input().split()
shuffles_num = int(input())

half_deck = len(deck_of_cards) // 2

final_deck_order = []

left_deck = []
right_deck = []

for shuffle in range(shuffles_num):

    for card in range(len(deck_of_cards)):

        if card < half_deck:
            left_deck.append(deck_of_cards[card])
        else:
            right_deck.append(deck_of_cards[card])

    for _ in range(len(left_deck)):

        final_deck_order.append(left_deck[_])
        final_deck_order.append(right_deck[_])

    deck_of_cards = final_deck_order.copy()
    final_deck_order.clear()
    left_deck.clear()
    right_deck.clear()

print(deck_of_cards)