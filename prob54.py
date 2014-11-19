'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
'''
import time
start = time.time()

with open('poker.txt') as f:
    content = f.read().splitlines()

value_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

wins = 0

def hand_value(hand):
    flush = False
    straight = False
    values = []
    suits = []
    scores = []
    pair = 0
    three = 0
    for i in hand:
        values.append(i[0])
        suits.append(i[1])
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        flush = True
    values = [value_dict[x] for x in values]
    values.sort()
    if values[0]+4 == values[1]+3 == values[2]+2 == values[3]+1 == values[4]:
        straight = True
    if straight and flush:
        scores.append(135+values[0])
    if straight and not flush:
        scores.append(75+values[0])
    if not straight and flush:
        scores.append(90+max(values))
    for i in values:
        if values.count(i) == 4:
            scores.append(120+i)
        if values.count(i) == 3:
            scores.append(60+i)
            three += i
            if pair > 0:
                scores.append(105+i)
        if values.count(i) == 2:
            scores.append(30+i)
            pair += 1
            if pair > 2:
                scores.append(45+i)
            if three > 0:
                scores.append(105+three)
    scores.append(max(values))
    scores = list(set(scores))
    scores.sort(reverse = True)
    return scores

for game in content:
    cards = game.split()
    player1 = cards[:5]
    player2 = cards[5:]
    score1 = hand_value(player1)
    score2 = hand_value(player2)
    for i in range(9):
        if score1[i] > score2[i]:
            wins += 1
            break
        elif score1[i] < score2[i]:
            break
        else:
            pass

elapsed = time.time() - start
print 'Answer: ', wins, ' found in ', elapsed, ' seconds!'
