# -*- coding: utf-8 -*-
from datetime import datetime

# =====================================================================
# 1. Removed duplicate code for en_US and nl_NL entries
#    Header, date format, and currency formatter are determined upfront.
#
# 2. Sorted entries once using Python's sorted with a tuple key
#    Replace manually finding the minimum repeatedly.
#
# 3. Date formatting
#
# 4. Description formatting (truncating to 25 chars)
#
# 5. Change formatting (US vs NL, USD vs EUR)
#
# 6. Simplified currency formatting with helper functions format_us_currency and format_nl_currency.
#
# 7. Replaced manual string building with Python f-strings for clarity and maintainability.
#
# 8. Maintained right alignment for the "Change" column.
# =====================================================================


class LedgerEntry:
  def __init__(self, date, description, change):
    self.date = datetime.strptime(date, "%Y-%m-%d")
    self.description = description
    self.change = change


def create_entry(date, description, change):
  return LedgerEntry(date, description, change)


def format_entries(currency, locale, entries):
  if locale == "en_US":
    header = "Date       | Description               | Change       "
    date_fmt = "{:02d}/{:02d}/{:04d}"
    currency_fmt = format_us_currency

  elif locale == "nl_NL":
    header = "Datum      | Omschrijving              | Verandering  "
    date_fmt = "{:02d}-{:02d}-{:04d}"
    currency_fmt = format_nl_currency

  else:
    raise ValueError("Unsupported locale")

  # Sort entries by date, then change, then description
  entries_sorted = sorted(
    entries,
    key=lambda e: (e.date, e.change, e.description)
  )

  lines = [header]
  for e in entries_sorted:
    # Format date
    if locale == "en_US":
      date_str = date_fmt.format(e.date.month, e.date.day, e.date.year)
    else:
      date_str = date_fmt.format(e.date.day, e.date.month, e.date.year)

    # Format description
    if len(e.description) > 25:
      description_str = e.description[:22] + "..."
    else:
      description_str = e.description.ljust(25)

    # Format change
    change_str = currency_fmt(e.change, currency)

    lines.append(f"{date_str} | {description_str} | {change_str}")

  return "\n".join(lines)


def format_us_currency(change, currency):
  is_negative = change < 0
  amount = abs(change) / 100.0
  symbol = "$" if currency == "USD" else "€"

  if is_negative:
    result = f"({symbol}{amount:,.2f})"
  else:
    result = f"{symbol}{amount:,.2f} "

  return result.rjust(13)


def format_nl_currency(change, currency):
  is_negative = change < 0
  amount = abs(change) / 100.0
  symbol = "$" if currency == "USD" else "€"

  integer, cents = divmod(int(round(amount * 100)), 100)
  integer_str = f"{integer:,}".replace(",", ".")
  cents_str = f"{cents:02d}"

  result = f"{symbol} {('-' if is_negative else '')}{integer_str},{cents_str} "

  return result.rjust(13)
