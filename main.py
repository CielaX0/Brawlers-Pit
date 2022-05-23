# Welcome player to the game
# Choose player to bet on
# Round start
# Both players roll d100; higher roll hits and rolls d20 for damage (taken from 100 health)
# Emotes (coming later)
# Back to top of the Round; Best 3 out of 5
# If player wins bet, they win their bet amount x 2; if player loses, they lose bet amount
import random

rounds = 0
bet_amount = 0
start = True

# Player must choose 1 of the 2 fighters; check if compare choice roll to bot roll

while start:
    print("Round Start!")
    rounds += 1

    if rounds == 5:
        print("And that's the Match!")
        break
    continue
