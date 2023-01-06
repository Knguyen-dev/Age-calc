import math
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

  # Used when you have the same months situation
  @staticmethod
  def find_days(startDay, endDay):
    if (startDay > endDay):
      days = -1 * (endDay - startDay)
    else:
      # startDay <= endDay
      days = (endDay - startDay)
    return days
        

  @staticmethod
  def find_month_gaps(startMonthIndex, endMonthIndex, cross_years = True):
    # turn the years into days; now find num months in between September 2021, [month] [last completed year] and June 2022 [end month] [end year]
    # Start at [start month] [last completed year] to the end of the year or [current year]
    numDays = 0
    numMonths = 0
    if (cross_years):
      while (startMonthIndex < 11):
        numMonths += 1
        startMonthIndex += 1
      # Gets amount of months from January to the [end month] [current year]
      while (endMonthIndex >= 0):
        numMonths += 1
        endMonthIndex -= 1
    else:
      # Well what if there is no month gap?, then we need to just find the amount of days
      for month in range(startMonthIndex, endMonthIndex):
        numMonths += 1
    # Average number of days in the gap of the months 
    numDays = (365.25 / 12) * numMonths
    return numDays

  @staticmethod
  def getDifferenceTime(startDate, endDate):
    startDay = startDate.d
    endDay = endDate.d
    diff_years = 0 
    diff_days = 0
    startMonthIndex = startDate.m - 1
    endMonthIndex = endDate.m - 1
    # If it crosses over different years, then subtract the number of complete years
    # Example: Sept 15, 1970 => June 15th 2022
    # Example: October 7 2003 => December 15, 2009
    # Check the month (using indices) to see the amount of complete years; September 15, 2022 isn't there, so 2022 isn't a complete year
    # For the second one, you know October 7, 2009 exists, so 2009 - 2003 is 6 years 
    # If it crosses over years then, let's calculate the difference in years
    if (endDate.y > startDate.y):
      if (startMonthIndex < endMonthIndex):
        # Find full difference in years
        # Find approximate amount of days in those complete years
        # Then add the amount of days in the month gaps 
        diff_years = endDate.y - startDate.y
        diff_days = 365.25 * diff_years
        diff_days += Date.find_month_gaps(startMonthIndex, endMonthIndex)
      elif (startMonthIndex > endMonthIndex):
        diff_years = (endDate.y - 1) - startDate.y #Minus 1 year when calculating difference because the year hasn't been reached yet
        diff_days = 365.25 * diff_years
        diff_days += Date.find_month_gaps(startMonthIndex, endMonthIndex)
      else:
        '''
        - this means they are different years, but the same months
        - Like October 4, 2004 to October 16, 2011; since end day is bigger than start day, we can subtract directly 2011 - 2005; then directly doing the days is possible
        - Like october 16, 2004 to October 3, 2007; since start day is bigger than end day, then (2011 - 2005) to get => October 16, 2007 (then you would get the difference 13 days and subtract 16 - 13 to get final);
        '''
        # Get the difference in years, but then adjust the amount of days
        diff_years = endDate.y - startDate.y
        diff_days += Date.find_days(startDay, endDay)        
      # Find average number of days in a month (365.25 / 12)
      # Multiply that by the gaps of the months so that we get the number of days in the month gap
      # Then round 
    else:
      # This would mean the years are the same so you would have to find months and days 
      # Almost, but this function only calculates the number of months across years, so we need something to calculate months across the same years
      diff_days = Date.find_month_gaps(startMonthIndex, endMonthIndex, False) 
      diff_days += Date.find_days(startDay, endDay)

    diff_days = math.floor(diff_days)
    return diff_days
        
def getDate():
  date = input('Enter first date in mm/dd/yyyy: ');
  dateComponents = []
  position = 0;
  for i in range(len(date)):
    if (date[i] == '/'):
      dateComponents.append(date[position:i]);
      position = i + 1;
    elif (i == len(date) - 1):
      dateComponents.append(date[position:]);
  month, day, year = dateComponents
  return Date(month, day, year);



a = Date('09', '5', '1970')
b = Date('06', '22', '2022')
c = Date('01', '4', '2004')
d = Date('03', '15', '2004')
e = Date('07', '03', '2004');
f = Date('07', '03', '2009');
g = Date('02', '03', '2004');
h = Date('02', '03', '2010');
i = Date('02', '29', '2004');
j = Date('02', '28', '2010');
k = Date('01', '15', '2002');
l = Date('12', '28', '2021');

print(Date.getDifferenceTime(a, b))
print(Date.getDifferenceTime(c, d))
print(Date.getDifferenceTime(e, f))
print(Date.getDifferenceTime(g, h))
print(Date.getDifferenceTime(i, j))
print(Date.getDifferenceTime(k, l))