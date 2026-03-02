from datetime import date, timedelta

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
  """Exception raised when the Meetup weekday and count do not result in a valid date.

  message: explanation of the error.

  """
  def __init__(self, message):
    self.message = message


DAY_EQUIVALENCE = {
  "Monday": 0,
  "Tuesday": 1,
  "Wednesday": 2,
  "Thursday": 3,
  "Friday": 4,
  "Saturday": 5,
  "Sunday": 6
}


LITERAL_EQUIVALENCE = {
  "last": 0,
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
  "fifth": 5
}


def get_days_of_month(year, month, day_of_week, day=1, end=32):
  days = []
  
  while True and day < end:
    try:
      d = date(year, month, day)
    except ValueError:
      break # Past the last day of the month
    
    if DAY_EQUIVALENCE[day_of_week] == d.weekday():
      days.append(d)
      
    day += 1
    
  return days


def meetup(year, month, week, day_of_week):
  d = date(2026, 3, 2)
  
  if week == "teenth":
    days = get_days_of_month(year, month, day_of_week, 13, 20)
    return days[0]
  else:
    days = get_days_of_month(year, month, day_of_week)
    
  if len(days) < LITERAL_EQUIVALENCE[week]:
    raise MeetupDayException("That day does not exist.")
  
  return days[LITERAL_EQUIVALENCE[week] - 1]