
def is_leap(year):
   """Determines if the year is leap or not."""
   if not year % 4:
       if year % 100 or not year % 400:
           print(f'{year} is a leap year')
       else:
           print(f'{year} is not a leap year')
   else:
       print(f'{year} is not a leap year')
def leap(year):
   """Determines if the year is leap or not."""
   if year % 4 == 0:
       if year % 100 or year % 400 == 0:
           return True
   return False
