from datetime import date, datetime, timedelta


MONTHS = {
  1: "January",
  2: "February",
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December"
}


QUARTERS = {
  1: ["January", "February", "March"],
  2: ["April", "May", "June"],
  3: ["July", "August", "September"],
  4: ["October", "November", "December"]
}


# Get the first working day of a month given a month and a year
def find_next_working_day(month, year):
  first_day = datetime(year, month, 1, 8)

  while first_day.weekday() > 4:   # Saturday or Sunday
    first_day += timedelta(days=1)

  return first_day


def find_last_working_day(quarter, year):
  # Last day of each month is not the same number
  day_number = (
    31      # March/December
    if quarter in [1, 4]
    else 30  # June/September
  )

  last_day = datetime(year, quarter * 3, day_number, 8)

  while last_day.weekday() > 4:   # Saturday or Sunday
    last_day -= timedelta(days=1)

  return last_day


# Get the quarter to which a month belongs
# Month is given as an integer here
def get_quarter(month):
  month_name = MONTHS[month]
  for k, v in QUARTERS.items():
    if month_name in v:
      return k


def delivery_date(start, description):
  # =====================================================================
  # Format date to manipulate
  # =====================================================================
  meeting = datetime.fromisoformat(start)

  # =====================================================================
  # Fixed description
  # =====================================================================
  if description == "NOW":
    delivery = meeting + timedelta(hours=2)   # Add 2 hours

  elif description == "ASAP":
    delivery = (
      meeting.replace(hour=17, minute=0, second=0)    # Today at 17:00
      if meeting.hour < 13
      else (meeting + timedelta(days=1)).replace(hour=13, minute=0, second=0)   # Tomorrow at 13:00
    )

  elif description == "EOW":
    week_day = meeting.weekday()
    days_to_friday = 4 - week_day
    days_to_sunday = 6 - week_day

    delivery = (
      (meeting + timedelta(days=days_to_friday)).replace(hour=17, minute=0, second=0)   # Friday at 17:00
      if week_day < 3   # Before Thursday
      else (meeting + timedelta(days=days_to_sunday)).replace(hour=20, minute=0, second=0)   # Sunday at 20:00
    )

  # =====================================================================
  # Variable description
  # =====================================================================
  # Month
  elif description.endswith('M'):
    meeting_month = meeting.month
    delivery_month = int(description[:-1])

    # Delivery year depends on the month of the meeting
    delivery_year = (
      meeting.year
      if meeting_month < delivery_month
      else meeting.year + 1
    )

    # First workday of delivery year's Nth month
    delivery = find_next_working_day(delivery_month, delivery_year)

  # Quarter
  elif description.startswith('Q'):
    meeting_quarter = get_quarter(meeting.month)
    delivery_quarter = int(description[1:])

    delivery_year = (
      meeting.year
      if meeting_quarter <= delivery_quarter
      else meeting.year + 1
    )

    # Last workday of delivery year's Nth quarter
    delivery = find_last_working_day(delivery_quarter, delivery_year)

  if not delivery:
    raise ValueError("Invalid input format")

  # Reformat
  return delivery.isoformat()
