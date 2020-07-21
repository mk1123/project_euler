"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

from typing import Tuple, List, Union, Callable
from typing_extensions import Literal
from collections import Counter

face_card_replace = dict(T=10, J=11, Q=12, K=13, A=14)

RANK_TYPE = Tuple[int, ...]
SUIT_TYPE = Tuple[str, ...]
CARD_FUNC_TYPE = Tuple[RANK_TYPE, SUIT_TYPE]

# PROCESSING FUNCTIONS


def hand_separator(cards):
    # type: (List[str]) -> CARD_FUNC_TYPE
    ranks, suits = tuple(zip(*cards))
    return (
        tuple(
            face_card_replace.get(
                rank, rank not in face_card_replace.keys() and int(rank)
            )
            for rank in ranks
        ),
        suits,
    )


def line_processor(line: str) -> Tuple[CARD_FUNC_TYPE, CARD_FUNC_TYPE]:
    cards = line.split(" ")
    first_player, second_player = cards[:5], cards[5:]
    return (hand_separator(first_player), hand_separator(second_player))


# HAND EVALUATORS

HAND_DETECTOR_RETURN_TYPE = Union[bool, Tuple[int, ...]]


def is_straight(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    sorted_ranks = sorted(ranks)
    return (
        len(set(ranks)) == len(ranks)
        and sorted_ranks[-1] - sorted_ranks[0] == len(ranks) - 1
        and (sorted_ranks[-1],)
    )


assert is_straight((1, 2, 3, 4, 5), ("H", "S", "S", "S", "C"))


def is_flush(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    return len(set(suits)) == 1 and tuple(sorted(ranks, reverse=True))


assert is_flush((1, 2, 3, 4, 5), ("H", "H", "H", "H", "H"))


def is_straight_flush(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    return is_straight(ranks, suits) and is_flush(ranks, suits)


assert is_straight_flush((1, 2, 3, 4, 5), ("H", "H", "H", "H", "H"))


def is_four_of_a_kind(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return common_vals[0][1] == 4 and list(zip(*common_vals))[0]  # type: ignore


assert is_four_of_a_kind((1, 2, 2, 2, 2), ("H", "S", "S", "S", "C"))


def is_pair(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return (
        len(common_vals) > 1  # type: ignore
        and common_vals[0][1] == 2
        and common_vals[1][1] != 2
        and list(zip(*common_vals))[0]
    )


assert is_pair((2, 2, 3, 4, 5), ("H", "S", "S", "S", "C"))


def is_three_of_a_kind(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return (
        len(common_vals) > 1  # type: ignore
        and common_vals[0][1] == 3
        and common_vals[1][1] != 2
        and list(zip(*common_vals))[0]
    )


assert is_three_of_a_kind((2, 2, 2, 4, 5), ("H", "S", "S", "S", "C"))


def is_full_house(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return (
        len(common_vals) > 1  # type: ignore
        and common_vals[0][1] == 3
        and common_vals[1][1] == 2
        and list(zip(*common_vals))[0]
    )


assert is_full_house((2, 2, 2, 5, 5), ("H", "S", "S", "S", "C"))


def is_two_pair(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return (
        len(common_vals) > 1  # type: ignore
        and common_vals[0][1] == 2
        and common_vals[1][1] == 2
        and list(zip(*common_vals))[0]
    )


assert is_two_pair((2, 2, 3, 4, 3), ("H", "S", "S", "S", "C"))


def is_high_card(ranks, suits):
    # type: (RANK_TYPE, SUIT_TYPE) -> HAND_DETECTOR_RETURN_TYPE
    common_vals = sorted(Counter(ranks).items(), key=lambda pair: (-pair[1], -pair[0]))
    return (
        len(common_vals) > 1  # type: ignore
        and common_vals[0][1] == 1
        and list(zip(*common_vals))[0]
    )


assert is_high_card((1, 2, 3, 4, 6), ("H", "S", "S", "S", "C"))

hands_dict = dict(
    high_card=is_high_card,
    pair=is_pair,
    two_pair=is_two_pair,
    three_of_a_kind=is_three_of_a_kind,
    straight=is_straight,
    flush=is_flush,
    full_house=is_full_house,
    four_of_a_kind=is_four_of_a_kind,
    straight_flush=is_straight_flush,
)


def tiebreaker(x: RANK_TYPE, y: RANK_TYPE) -> int:
    return (x > y) - (x < y)


hand_rankings = dict(zip(hands_dict.values(), range(len(hands_dict))))


def get_hand_rank(
    ranks: RANK_TYPE, suits: SUIT_TYPE
) -> Tuple[
    int, Callable[[Tuple[int, ...], Tuple[str, ...]], Union[bool, Tuple[int, ...]]]
]:
    return next(
        (hand_rankings[f], f)
        for f in reversed(list(hands_dict.values()))
        if f(ranks, suits)
    )


# RUNTIME CODE

with open("./resources/poker.txt") as f:
    hands_list = [line_processor(line) for line in f.readlines()]

first_player_wins = 0

for first_player, second_player in hands_list:
    (first_rank, first_func), (second_rank, second_func) = (
        get_hand_rank(*first_player),
        get_hand_rank(*second_player),
    )

    if first_rank > second_rank:
        first_player_wins += 1
    elif first_rank == second_rank:
        if tiebreaker(first_func(*first_player), second_func(*second_player)) > 0:  # type: ignore
            # print(first_player, second_player, first_func)
            first_player_wins += 1

print(first_player_wins)

