def transpose(text):
  if text == "":
    return ""

  rows = text.split("\n")
  max_len = max(len(r) for r in rows)

  result = []

  for i in range(max_len):
    line_chars = []

    for j, row in enumerate(rows):
      if i < len(row):
        line_chars.append(row[i])
      else:
        if any(len(r) > i for r in rows[j+1:]):
          line_chars.append(" ")
        else:
          break

    result.append("".join(line_chars))

  return "\n".join(result)