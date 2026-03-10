from enum import IntEnum
from collections import Counter

class HandRank(IntEnum):
  HIGH_CARD = 1
  ONE_PAIR = 2
  TWO_PAIR = 3
  THREE_OF_A_KIND = 4
  STRAIGHT = 5
  FLUSH = 6
  FULL_HOUSE = 7
  FOUR_OF_A_KIND = 8
  STRAIGHT_FLUSH = 9
  ROYAL_FLUSH = 10
  FIVE_OF_A_KIND = 11

CARD_VALUE = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}


def identify_hand(hand):
  cards = hand.split()
  colors = [card[-1] for card in cards]
  values = [card[:-1] for card in cards]
  vals = sorted(CARD_VALUE[v] for v in values)
  counts = Counter(vals)
    
  # Tiebreaker helper: sorts first by count (high to low), then by value (high to low)
  def tiebreaker():
    return sorted(counts.keys(), key=lambda x: (counts[x], x), reverse=True)
    
  is_flush = len(set(colors)) == 1
  is_straight = len(counts) == 5 and (vals[-1] - vals[0] == 4 or set(vals) == {2, 3, 4, 5, 14})

  # Adjust values for Ace-low straights
  straight_vals = vals[:]
  if set(vals) == {2, 3, 4, 5, 14}:
    straight_vals = [1, 2, 3, 4, 5]

  # FIVE OF A KIND
  if 5 in counts.values():
    return (HandRank.FIVE_OF_A_KIND, tiebreaker())
    
  # STRAIGHT FLUSH or ROYAL FLUSH
  if is_straight and is_flush:
    if set(vals) == {10, 11, 12, 13, 14}:
      return (HandRank.ROYAL_FLUSH, tiebreaker())
    return (HandRank.STRAIGHT_FLUSH, sorted(straight_vals, reverse=True))
    
  # FOUR OF A KIND
  if 4 in counts.values():
    return (HandRank.FOUR_OF_A_KIND, tiebreaker())
    
  # FULL HOUSE
  if 3 in counts.values() and 2 in counts.values():
    return (HandRank.FULL_HOUSE, tiebreaker())
    
  # FLUSH (use high cards for tie-breaker)
  if is_flush:
    return (HandRank.FLUSH, sorted(vals, reverse=True))
    
  # STRAIGHT
  if is_straight:
    return (HandRank.STRAIGHT, sorted(straight_vals, reverse=True))
    
  # THREE OF A KIND
  if 3 in counts.values():
    return (HandRank.THREE_OF_A_KIND, tiebreaker())
    
  # TWO PAIR
  if list(counts.values()).count(2) == 2:
    return (HandRank.TWO_PAIR, tiebreaker())
    
  # ONE PAIR
  if 2 in counts.values():
    return (HandRank.ONE_PAIR, tiebreaker())
    
  # HIGH CARD
  return (HandRank.HIGH_CARD, sorted(vals, reverse=True))


def best_hands(hands):
  # Pair each hand with its rank and tiebreaker
  hands_with_ranks = [(hand, identify_hand(hand)) for hand in hands]
  # Find max rank (HandRank and tiebreaker)
  max_rank = max(rank for _, rank in hands_with_ranks)
  # Return all hands that match the top rank/tiebreaker
  return [hand for hand, rank in hands_with_ranks if rank == max_rank]