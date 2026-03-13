import re


def parse_emphasis(text):
  # Bold
  text = re.sub(r"__(.*?)__", r"<strong>\1</strong>", text)
  # Italic
  text = re.sub(r"_(.*?)_", r"<em>\1</em>", text)

  return text


def parse_header(line):
  match = re.match(r"^(#{1,6}) (.*)", line)
  if match:
    level = len(match.group(1))
    content = match.group(2)

    return f"<h{level}>{parse_emphasis(content)}</h{level}>"

  return None


def parse_lists(lines):
  res = []
  in_list = False

  for line in lines:
    match = re.match(r"\* (.*)", line)
    # List item
    if match:
      if not in_list:   # Open list
        res.append("<ul>")
        in_list = True

      content = parse_emphasis(match.group(1))
      res.append(f"<li>{content}</li>")

    else:
      if in_list:    # Close list
        res.append("</ul>")
        in_list = False

      res.append(line)

  # Close open lists at the end
  if in_list:
    res.append("</ul>")

  return res


def parse(markdown):
  lines = markdown.split('\n')
  lines = parse_lists(lines)
  html = []

  for line in lines:
    if not line:
      continue

    # Headers
    header = parse_header(line)
    if header:
      html.append(header)

    elif line.startswith("<ul>") or line.startswith("<li>") or line.startswith("</ul>"):
      html.append(line)

    # Paragraph
    else:
      html.append(f"<p>{parse_emphasis(line)}</p>")

  return ''.join(html)
