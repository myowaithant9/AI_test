import datetime  
from datetime import date 
import calendar 

year = int ( input ("Year > ") )
month = int ( input ("Month > ") )
day = int ( input ("Day > ") )

date = datetime.date(year, month, day) 
print(date.strftime("%B") + " " + str(day) + ", " + str(year) + " is " + date.strftime("%A"))
