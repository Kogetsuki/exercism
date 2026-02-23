def tally(rows):
  teams = {}

  # Iterate over match results
  for row in rows:
    # Split with separator ';'
    team1, team2, result = row.split(';')

    # Init teams stats if not in dict
    for team in (team1, team2):
      if team not in teams:
        teams[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

    # Increment match play for every row
    teams[team1]["MP"] += 1
    teams[team2]["MP"] += 1

    # Update stats based on result
    if result == "win":
      teams[team1]["W"] += 1
      teams[team1]["P"] += 3
      teams[team2]["L"] += 1
      
    elif result == "loss":
      teams[team1]["L"] += 1
      teams[team2]["W"] += 1
      teams[team2]["P"] += 3
      
    else:
      teams[team1]["D"] += 1
      teams[team1]["P"] += 1
      teams[team2]["D"] += 1
      teams[team2]["P"] += 1
      
  # Sort by number of points, then alphabetically
  sorted_teams = sorted(
    teams.items(),
    key=lambda item: (-item[1]["P"], item[0])
  )
  
  # Format results
  header = "Team                           | MP |  W |  D |  L |  P"
  results = [header]

  # Iterate through sorted teams to format
  for team, stats in sorted_teams:
    # Team left-aligned in 30 chars
    # Stats right-aligned in 2 chars
    result = (
      f"{team:<30} | ",
      f"{stats["MP"]:>2} | "
      f"{stats["W"]:>2} | "
      f"{stats["D"]:>2} | "
      f"{stats["L"]:>2} | "
      f"{stats["P"]:>2}"
    )
    
    results.append(''.join(result))
    
  return results