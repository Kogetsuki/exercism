def grep(pattern, flags, files):
  result = []
  flags_set = set(flags.split())

  for file in files:
    with open(file) as f:
      lines = f.readlines()

    matches = []
    file_has_matches = False

    for i, line in enumerate(lines, start=1):
      text = line.rstrip("\n")

      search_pattern = pattern
      search_text = text

      # Case-insensitive
      if "-i" in flags_set:
        search_pattern = pattern.lower()
        search_text = text.lower()

      # Match logic
      # Whole line matches
      if "-x" in flags_set:
        match = search_pattern == search_text
      else:
        match = search_pattern in search_text

      # Invert search
      if "-v" in flags_set:
        match = not match

      if match:
        file_has_matches = True

        # Only filename
        if "-l" in flags_set:
          break

        prefix = ""
        if len(files) > 1:
          prefix += f"{file}:"
        if "-n" in flags_set:
          prefix += f"{i}:"

        matches.append(prefix + text)

    if "-l" in flags_set:
      if file_has_matches:
        result.append(file)

    else:
      result.extend(matches)

  return "\n".join(result) + ("\n" if result else "")
