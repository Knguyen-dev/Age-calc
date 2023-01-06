'''
Write a program that prompts the user for a date (mm/dd/yyyy) format, could be their birthday, and a second date,
assume the second date is chronologically later than the first date. Then have the program display the time difference
between these dates, in years (add floats), months (add floats), and days (add floats) individually for each.
It would be like: 3.54 years or something odd months, but it's only one type.

Then display them all together in total like e.g. 3 years 2 months and 16 days.
+ Year transition (assuming we need to go through years):
- Get our starting year, if it's a leap year, then check if the leap month of february is triggered. 
Outcome 1: Not triggered as July 5, 2004 - July 5, 2005; 365 days as 2004's february wasn't triggered; we started in a leap
year, but July 5 was before February 28. If the date starts any earlier than Feb 29, then you have 365. 


Outcome 2: Triggered as January 25, 2004 - January 25, 2005, since you started in a leap year and your month
is January, which is before February 28; 366 days


- Getting to the leap year: 
E.g. April 5, 2007 - April 5, 2008
Outcome 1: The year being transitioned into is a leap year, or a year after the starting year is a leap year. Then
check the month => April is AFTER February, so that means february leap will be triggered; 366 days

E.g. February 16, 2007 - February 16, 2008
Outcome 2: The year being transitioned into is a leap year, or a year after the starting is a leap year, same situation.
Let's check the month again, the month is February, which means it's before Feb 29 and months after; So in conclusion
since we are transitioning into leap year, and the month is before March or Feb 29; we only get 365 days

note: If we have February 29, 2004 and we plus one year, it need to be February 28, 2005; 365 days
'''
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
    print(f'Starting at: {currentMonth}:{currentDay}:{currentYear}')

    
    
    print(f"{currentMonth}:{currentDay}:{currentYear}")
    return diff
        
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



# FIRST_DATE = Date('07', '03', '2004');
# SECOND_DATE = Date('07', '03', '2009');
# FIRST_DATE = Date('02', '03', '2004');
# SECOND_DATE = Date('02', '03', '2010');
# FIRST_DATE = Date('02', '29', '2004');
# SECOND_DATE = Date('02', '28', '2010');
FIRST_DATE = Date('02', '29', '2004');
SECOND_DATE = Date('01', '29', '2010');

difference_in_days = Date.getDifferenceTime(FIRST_DATE, SECOND_DATE)
print(f"Difference: {difference_in_days} days ")





