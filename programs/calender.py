#Program to calculate and draw a year calender
# calendar function

year = 2021
def Generating_calendar(year):
      import calendar
      month = 1
      while month <= 12:
           cal = calendar.month(year, month)
           print(cal)
           month = month +1
  
# main program starts here        
Generating_calendar(year = 2018)


#Time module time.clock
import time
def procedure():
    time.sleep(2.5)
    
t0 = time.clock()
procedure()
print (time.clock() - t0, "seconds process time")

t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")


def change(list):
    print(list)
    list[0] = 10
    print(list)
    return

list = [20,20,30,40]
change(list)
#print(list)
