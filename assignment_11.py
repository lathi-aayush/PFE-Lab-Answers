# 11.  There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards. Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

cards = []

N = int(input("Enter N : "))
sum_list = 0

for i in range(1, N):
    card = int(input("Enter Card Number starting from 1, 2, 3... : "))
    cards.append(card)
    sum_list = cards[i - 1] + sum_list

sum = (N * (N + 1)) / 2

lost_num = sum - sum_list

print(f"The lost Card has Number - '{lost_num}' on it")
