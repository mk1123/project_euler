"""
Project Euler Problem 84
========================

In the game, Monopoly, the standard board is set up in the following way:

             GO   A1  CC1  A2  T1  R1  B1  CH1  B2   B3  JAIL
             H2                                          C1
             T2                                          U1
             H1                                          C2
             CH3                                         C3
             R4                                          R2
             G3                                          D1
             CC3                                         CC2
             G2                                          D2
             G1                                          D3
             G2J  F3  U2   F2  F1  R3  E3  E2   CH2  E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice
to determine the number of squares they advance in a clockwise direction.
Without any further rules we would expect to visit each square with equal
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the
player to go to directly jail, if a player rolls three consecutive
doubles, they do not advance the result of their 3rd roll. Instead they
proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a
player lands on CC or CH they take a card from the top of the respective
pile and, after following the instructions, it is returned to the bottom
of the pile. There are sixteen cards in each pile, but for the purpose of
this problem we are only concerned with cards that order a movement; any
instruction not concerned with movement will be ignored and the player
will remain on the CC/CH square.

  * Community Chest (2/16 cards):

      1. Advance to GO
      2. Go to JAIL

  * Chance (10/16 cards):

      1. Advance to GO
      2. Go to JAIL
      3. Go to C1
      4. Go to E3
      5. Go to H2
      6. Go to R1
      7. Go to next R (railway company)
      8. Go to next R
      9. Go to next U (utility company)
     10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for
which the probability of finishing on it is zero, the CH squares will have
the lowest probabilities, as 5/8 request a movement to another square, and
it is the final square that the player finishes at on each roll that we
are interested in. We shall make no distinction between "Just Visiting"
and being sent to JAIL, and we shall also ignore the rule about requiring
a double to "get out of jail", assuming that they pay to get out on their
next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we
can concatenate these two-digit numbers to produce strings that correspond
with sets of squares.

Statistically it can be shown that the three most popular squares, in
order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
(3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.
"""

from collections import Counter
from random import choices, randint
from typing import List, Dict, Tuple

# dice_rolls = choices(
#     range(1, 9), [0, 1 / 16, 2 / 16, 3 / 16, 4 / 16, 3 / 16, 2 / 16, 1 / 16], k=10 ** 5
# )

possible_dice_rolls = [(x, y) for x in range(1, 5) for y in range(1, 5)]
dice_rolls = choices(possible_dice_rolls, k=10 ** 7)

squares = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JAIL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2",
]

num_squares = len(squares)

prev_3_rolls: List[Tuple[int, int]] = []
visited_idxs: Dict[int, int] = Counter()

square_to_idx = dict((y, x) for (x, y) in enumerate(squares))
idx_to_square = dict(enumerate(squares))

is_double = lambda tup: tup[0] == tup[1]
chance_idx = 0
cc_idx = 0

curr_idx = 0

for roll in dice_rolls:
    if len(prev_3_rolls) > 2:
        prev_3_rolls.pop(0)
    prev_3_rolls.append(roll)
    if (
        len(prev_3_rolls) > 2
        and is_double(prev_3_rolls[0])
        and is_double(prev_3_rolls[-1])
        and is_double(prev_3_rolls[-2])
    ):  # going to jail, doubles 3 times in a row
        curr_idx = square_to_idx["JAIL"]
    else:
        curr_idx = (curr_idx + sum(roll)) % num_squares
        square = idx_to_square[curr_idx]
        if square == "G2J":
            curr_idx = square_to_idx["JAIL"]
        square = idx_to_square[curr_idx]
        if "CH" in square:  # chance
            chance_idx = (chance_idx + 1) % 16
            if chance_idx == 0:
                curr_idx = square_to_idx["GO"]
            elif chance_idx == 1:
                curr_idx = square_to_idx["JAIL"]
            elif chance_idx == 2:
                curr_idx = square_to_idx["C1"]
            elif chance_idx == 3:
                curr_idx = square_to_idx["E3"]
            elif chance_idx == 4:
                curr_idx = square_to_idx["H2"]
            elif chance_idx == 5:
                curr_idx = square_to_idx["R1"]
            elif 5 < chance_idx < 8:
                while "R" not in idx_to_square[curr_idx]:
                    curr_idx = (curr_idx + 1) % num_squares
            elif chance_idx == 8:
                while "U" not in idx_to_square[curr_idx]:
                    curr_idx = (curr_idx + 1) % num_squares
            elif chance_idx == 9:
                curr_idx = (curr_idx - 3) % num_squares
        square = idx_to_square[curr_idx]
        if "CC" in square:  # community chest
            cc_idx = (cc_idx + 1) % 16
            if cc_idx == 0:
                curr_idx = square_to_idx["GO"]
            elif cc_idx == 1:
                curr_idx = square_to_idx["JAIL"]

    visited_idxs[curr_idx] += 1

most_visited_squares = sorted(
    visited_idxs.items(), key=lambda item: item[1], reverse=True
)[:3]

print("".join([str(x[0]).zfill(2) for x in most_visited_squares]))
# print(most_visited_squares)

