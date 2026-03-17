def simulate_game(player_a, player_b):
  # Map penalty values
  penalties = {"J": 1, "Q": 2, "K": 3, "A": 4}

  # Initialize state
  decks = [list(player_a), list(player_b)]
  pile = []
  history = set()

  total_cards_played = 0
  tricks = 0

  # 0 for player_a, 1 for player_b
  current_player = 0

  while True:
    # Check for loop
    state_a = "".join(c if c in penalties else "X" for c in decks[0])
    state_b = "".join(c if c in penalties else "X" for c in decks[1])
    current_state = (state_a, state_b, current_player)

    if current_state in history:
      return {"status": "loop", "cards": total_cards_played, "tricks": tricks}

    history.add(current_state)

    # Round
    penalty_due = 0
    last_payer = None

    while True:
      # If current player is empty, the other player wins the trick
      if not decks[current_player]:
        winner = 1 - current_player
        break

      # Play a card
      card = decks[current_player].pop(0)
      pile.append(card)
      total_cards_played += 1

      if card in penalties:
        # New penalty starts
        penalty_due = penalties[card]
        last_payer = current_player
        current_player = 1 - current_player

      else:
        if penalty_due > 0:
          penalty_due -= 1

          if penalty_due == 0:
            # Penalty paid in full, last_payer takes the pile
            winner = last_payer
            break

        else:
          # Normal play, switch turns
          current_player = 1 - current_player
          # Check if one player ran out after a normal card
          if not decks[current_player]:
            winner = 1 - current_player
            break

    # Conclude trick
    tricks += 1
    decks[winner].extend(pile)
    pile = []
    current_player = winner  # Winner starts the next round

    # Game end
    if not decks[0] or not decks[1]:
      return {"status": "finished", "cards": total_cards_played, "tricks": tricks}
