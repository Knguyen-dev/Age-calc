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
MONHTS = [
  {
    '01': 'January',
    'days': 31,
  },
  {
    '02': 'February',
    'days': 28,
  },
  {
    '03': 'March',
    'days': 31,
  },
  {
    '04': 'April',
    'days': 30,
  },
  {
    '05': 'May',
    'days': 31,
  },
  {
    '06': 'June',
    'days': 30,
  },
  {
    '07': 'July',
    'days': 31,
  },
  {
    '08': 'August',
    'days': 31,
  },
  {
    '09': 'September',
    'days': 30,
  },
  {
    '10': 'October',
    'days': 31,
  },
  {
    '11': 'November',
    'days': 30,
  },
  {
    '12': 'December',
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
    startYear = startDate.y
    startMonth = startDate.m
    
    startDay = startDate.d 
    # Will change actually 
    # Example February 29, 2004 => February 28, 2005; so when calculating the days we will check if February 29th is valid, if it isn't then put it to Feb 28 because that's 365 days passed
    # We'd need to do this to calculate the days, however once you change Feb 29 => Feb 28, you don't need to manipulate it again
    '''
    if target is Feb 29th, 2008, and we're given Feb28th, 2007, we add 365 days to get Feb 28th, 2008. At this point the year is done and we leave the calculations to the days 
    '''

    endYear = endDate.y
    endMonth = endDate.m
    endDay = endDate.d
    # Counts the difference in days
    diff = 0 
    monthIndex = startMonth - 1

    # May need to do range(startYear, endYear), as year would representing the completion of the year
    for year in range(startYear, endYear):
      # Deal with the first year
      if (year == startYear):
        is_leap_year = Date.checkLeapYear(year)
        '''
        - If the first year is a leap year, then if the start date is after february 29th, then getting to the exact same day or time next year would be 365 days. For feb29th to feb28 next year would be 365 days
        - However, 365 days after feb 29th, would be feb 28th, which we would need to change on the startDay. This will be important later when we are exactly getting the days
        - Else if you are starting on Feb 28th or earlier on a leap year, then transitioning to the next year it would go through feb 29th, hence adding that extra day in the year
        '''
        if (is_leap_year): #if the starting year is a leap year
          print("Leap year Detected as the starting year")
          if (monthIndex > 1):
            days_added = 365
          elif (monthIndex == 1 and startDay == 29):
            print('Starting year transition: February not triggered, so going to the next year is 365 days only')
            days_added = 365
            startDay = 28
          else:
            print('Starting year transition: February not triggered, so going to the next year is 365 days only')
            days_added = 366
        # if the starting year is a leap year, then we only need to add 365 days to get to the same date
        else:
          print("Starting year is not a leap year")
          days_added = 365

      elif (year > startYear):
        '''
        - For all years after the starting year
        - Check if the next year is a leap year, and if the current year is a leap year; only one of these will be true
        - If the next year is a leap year, then transitioning to the next year may have us pass feb 29th, hence adding the extra year
        - In these cases, again we check the months to see how many days we are adding 
        + Note: If we start feb 29th, it will be converted to feb 28th, and then if another leap occurs then it will transition to feb 29th
        '''
        next_leap = Date.checkLeapYear(year + 1) 
        current_leap = Date.checkLeapYear(year);
        if (next_leap):
          # when it's january/february, then it's  not going to pass leap month for the leap year because your max is feb 28
          # Example: january 16, 2007 => january 16, 2008 will only be 365 days passed
          # Example February 28, 2007 => February 29, 2008 will only be 366 days
          print(f"Year is {year}, the next year is detected leap year")
          if (monthIndex <= 1): 
            print(f"Not after february, so February leap is not triggered")

            if (monthIndex == 1 and startDate == 28): #This would mean it's february 28 2003 => february 29, 2004, so 366 days would pass
              days_added = 366;
              startDate = 29;
            else:
              days_added = 365; #Like Feb 19, 2003 => Feb 19, 2004; the startDate wouldn't change here because again, adding 365 will leave you with the same thing

          else: 
            #Else if we are transitioning into a leap year and the month is after February then the leap year will trigger
            # Example: April 3, 2007 => April 3, 2008 will take 366 days
            print(f"After february, so transitioning years will make the leap february trigger")
            days_added = 366;
        elif (current_leap):
          # If the next year isn't a leap year, then check if the current year is a leap year
          # Now, it can be feb 29, 2004 => feb 28, 2005
          print(f"Current year ({year}) is detected as leap year")
          if (monthIndex <= 1):          
            # Example: Feb 15, 2008 => Feb 15, 2009
            # 366 days because the leap month is activated in the months of january/february, except for february 29th as startDate
            # IF given is feb29 it should be already converted to 28th at this point
            # Example: February 29, 2004 => February 28, 2005; here the leap day isn't counted
            # However all dates before it, it will count because it passes that February 28 - February 29 barrier
            if (monthIndex == 1 and startDate == 29):
              days_added = 365
              startDate = 28
            else: 
              days_added = 366
          else:
            # Else if the current year is a leap year, then and it's after February, then we are not triggering the leap day
            # Example: March 1, 2008 => March 1, 2009;
            days_added = 365
            print(f"Started after february, so leap february was not triggered")
        else:
          # This means that the current year and the next year are not leap years
          # So the year in between is a normal year
          # January 25, 2006 => January 25, 2007
          days_added = 365
          print("Current year isn't a leap year and the next year (transition) isn't a leap year either")

      # Don't forget to check for date correction, like February 29, 2010 is not a correct one
      # now we have to check the last transition, if we transition last into a leap year
      # Check the year before the endYear; so like the shift from 2007 => 2008 or 2002 => 2004  
      print(f"{year} completed, year is now {year + 1}")
      diff += days_added


    print(f"Months diff: {diff}")
    # Now let's check the months
    
    return diff;
        
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

'''
- Right now it seems very good at transitioning to different years
- Now we'll need it to be able to transition to months; also take into account of the value of the object during leap years, when month transitions

'''

# FIRST_DATE = Date('07', '03', '2004');
# SECOND_DATE = Date('07', '03', '2009');
# FIRST_DATE = Date('02', '03', '2004');
# SECOND_DATE = Date('02', '03', '2010');
# FIRST_DATE = Date('02', '29', '2004');
# SECOND_DATE = Date('02', '28', '2010');
# FIRST_DATE = Date('05', '29', '2002');
# SECOND_DATE = Date('05', '29', '2010');



difference_in_days = Date.getDifferenceTime(FIRST_DATE, SECOND_DATE)
print(f"Difference: {difference_in_days} days ")





