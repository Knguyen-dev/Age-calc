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
  
  @staticmethod
  def getDifferenceTime(startDate, endDate):
    endDay = endDate.d
    currentDay = startDate.d
    currentYear = startDate.y
    diff = 0 
    currentMonthIndex = startDate.m - 1
    endMonthIndex = endDate.m - 1
    #The magical floating number is (365.25 / 12)
    AVERAGE_DAYS_PER_MONTH = 30.4375
    for year in range(startDate.y, endDate.y):
      next_leap = Date.checkLeapYear(year + 1)
      current_leap = Date.checkLeapYear(year)
      if (year == startDate.y):
        '''
        - If the first year is a leap year, then if the start date is after february 29th, then getting to the exact same day or time next year would be 365 days. For feb29th to feb28 next year would be 365 days
        - However, 365 days after feb 29th, would be feb 28th, which we would need to change on the startDay. This will be important later when we are exactly getting the days
        - Else if you are starting on Feb 28th or earlier on a leap year, then transitioning to the next year it would go through feb 29th, hence adding that extra day in the year
        '''
        if (current_leap): #if the starting year is a leap year
          if (currentMonthIndex > 1):
            days_added = 365
          elif (currentMonthIndex == 1 and currentDay == 29):
            days_added = 365
            currentDay = 28
          else:
            days_added = 366
        else:
          days_added = 365
      else:
        '''
        - For all years after the starting year
        - Check if the next year is a leap year, and if the current year is a leap year; only one of these will be true
        - If the next year is a leap year, then transitioning to the next year may have us pass feb 29th, hence adding the extra year
        - In these cases, again we check the months to see how many days we are adding 
        + Note: If we start feb 29th, it will be converted to feb 28th, and then if another leap occurs then it will transition to feb 29th
        '''
        if (next_leap):
          '''
          - when it's january/february, then it's  not going to pass leap month for the leap year because your max is feb 28
          - Example: january 16, 2007 => january 16, 2008 will only be 365 days passed
          - Example February 28, 2007 => February 29, 2008 will only be 366 days
          - This would mean it's february 28 2003 => february 29, 2004, so 366 days would pass
          - Like Feb 19, 2003 => Feb 19, 2004; the startDate wouldn't change here because again, adding 365 will leave you with the same thing
          '''
          if (currentMonthIndex <= 1): 
            if (currentMonthIndex == 1 and currentDay == 28): 
              days_added = 366
              currentDay = 29
            else:
              days_added = 365
          else: 
            #Else if we are transitioning into a leap year and the month is after February then the leap year will trigger
            # Example: April 3, 2007 => April 3, 2008 will take 366 days
            days_added = 366
        elif (current_leap):
          # If the next year isn't a leap year, then check if the current year is a leap year
          if (currentMonthIndex <= 1):          
            # Example: Feb 15, 2008 => Feb 15, 2009
            # 366 days because the leap month is activated in the months of january/february, except for february 29th as startDate
            # IF given is feb29 it should be already converted to 28th at this point
            # Example: February 29, 2004 => February 28, 2005; here the leap day isn't counted
            # However all dates before it, it will count because it passes that February 28 - February 29 barrier
            if (currentMonthIndex == 1 and currentDay == 29):
              days_added = 365
              currentDay = 28
            else: 
              days_added = 366
          else:
            # Else if the current year is a leap year, then and it's after February, then we are not triggering the leap day
            # Example: March 1, 2008 => March 1, 2009;
            days_added = 365
        else:
          # This means that the current year and the next year are not leap years
          # So the year in between is a normal year
          # Example: January 25, 2006 => January 25, 2007
          days_added = 365


      diff += days_added
      currentYear += 1
    '''
    - At this point year is finished    
    + Now let's transition the months
    - To transition the months we will need to use startMonthIndex again
    Example: May, 24, 2002 to October 15, 2010
    Step 1: Transition years => May 24, 2010
    Step 2: Transition months => October 24, 2010; an estimation
    Step 3: Transition days => October 15, 2010; 
    '''

    # Loop that adds transitions through the months; for each month we transition into we add an average amount of days to our difference, in order to approximate the actual amount of days being passed through
    # each month
    while (currentMonthIndex != endMonthIndex):
      if (currentMonthIndex > endMonthIndex):
        diff -= AVERAGE_DAYS_PER_MONTH
        currentMonthIndex -= 1
      else:
        if (currentMonthIndex < endMonthIndex):
          diff += AVERAGE_DAYS_PER_MONTH
          currentMonthIndex += 1

    # Loop to narrow down the days
    while (currentDay != endDay):
      if (currentDay > endDay):
        diff -= 1
        currentDay -= 1
      else:
        if (currentDay < endDay):
          diff += 1
          currentDay += 1
    
    return math.floor(diff)
        
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

FIRST_DATE = Date('03', '03', '1980');
SECOND_DATE = Date('12', '17', '2020');
difference_in_days = Date.getDifferenceTime(FIRST_DATE, SECOND_DATE)
print(f"Difference: {difference_in_days} days ")





