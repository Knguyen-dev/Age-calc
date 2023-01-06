MONTHS = [
  {
    'name': 'January',
    'days': 31,
  },
  {
    'name': 'February',
    'days': 28,
  },
  {
    'name': 'March',
    'days': 31,
  },
  {
    'name': 'April',
    'days': 30,
  },
  {
    'name': 'May',
    'days': 31,
  },
  {
    'name': 'June',
    'days': 30,
  },
  {
    'name': 'July',
    'days': 31,
  },
  {
    'name': 'August',
    'days': 31,
  },
  {
    'name': 'September',
    'days': 30,
  },
  {
    'name': 'October',
    'days': 31,
  },
  {
    'name': 'November',
    'days': 30,
  },
  {
    'name': 'December',
    'days': 31,
  },
]
class Date:
  def __init__(self, m, d, y):
    self.m = int(m);
    self.d = int(d);
    self.y = int(y);
  def __repr__(self):
    return f"month: {self.m}\nday: {self.d}\nyear: {self.y}"
  @staticmethod
  def checkLeapYear(year):
    result = True;
    # If it's not evenly divisible by 4 then it's not a leap year
    if (year % 4 != 0):
      result = False;
    else:
      # If it is divisible by 4 then it may be a leap year
      # If it isn't evenly divisible by 100 then it is a leap year; boolean doesn't need to be changed since already true
      # However if it is evenly divisible by 100 and 400, then it is a leap year, else the other outcome means that though it is evenly divisible
      # by 100, since it isn't evenly divisible by 400, it is not a leap year.
      if (year % 100 == 0 and year % 400 != 0):
        result = False;
    return result

  @staticmethod
  def getDifferenceTime(startDate, endDate):
    endYear = endDate.y
    endMonth = endDate.m
    endDay = endDate.d
    currentDay = startDate.d
    currentMonth = startDate.m
    currentYear = startDate.y
    diff = 0 
    currentMonthIndex = currentMonth - 1
    endMonthIndex = endDate.m - 1