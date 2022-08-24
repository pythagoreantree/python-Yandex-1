n, k = map(int, input().split())
cards = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    if card not in cards_dict:
        cards_dict[card] = 0
    cards_dict[card] += 1

unique_cards = sorted(cards_dict.keys())
sp = 0
combinations = 0
more_than_one_card = 0

for i in range(len(unique_cards)):
    while sp < len(unique_cards) and unique_cards[sp] <= unique_cards[i]*k:
        if cards_dict[unique_cards[sp]] > 1:
            more_than_one_card += 1
        sp += 1
    # print(i, sp)
    if cards_dict[unique_cards[i]] >= 2:
        combinations += (sp - i - 1) * 3
    if cards_dict[unique_cards[i]] >= 3:
        combinations += 1
    combinations += (sp - i - 1) * (sp - i - 2) * 3
    if cards_dict[unique_cards[i]] >= 2:
        more_than_one_card -= 1
    combinations += more_than_one_card * 3
print(combinations)

