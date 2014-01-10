#!/usr/local/bin/python
import urllib2, json, getpass, time, datetime
from datetime import date #not sure why I needed to do this but I did



'''
Name:       analyze_time()
Parameters: None
Return:     type_day
Purpose:    to figure out whether it's morning, evening, or afternoon
'''
def analyze_time():
   #lstrip() removes any whitespace in front
   hour = time.strftime("%l").lstrip()

   if time.strftime("%p") == "AM":
      type_day = "morning"
   elif (time.strftime("%p") == "PM") and (hour > 5):
      type_day = "evening"
   else:
      type_day = "afternoon"
   return type_day



'''
Name:       greeting()
Parameters: None
Return:     None
Purpose:    to greet the user, uses their username and the date and time
'''
def greeting():
   type_day = analyze_time()
   current_date = time.strftime("%l:%M%p on %h %d, %Y")
   username = getpass.getuser()
   print "Good %s %s! \nIt is currently%s.\n\n" %(type_day, username, current_date)



'''
Name:       get_weather()
Parameters: None
Return:     None
Purpose:    to get the weather from wunderground.com using their API, it
            gets the location, temperature, what it feels like (both in F),
            and the condition (i.e. snowing, overcast etc) and calls
            the weather_report function
'''
def get_weather():
   '''
   To change the location, change '22202' after the /q to whatever you want
   Also please use your API code not mine! They're free from wunderground.com
   '''
   f = urllib2.urlopen('http://api.wunderground.com/api/3683c1e808f1d752/geolookup/conditions/q/22202.json')
   json_string = f.read()

   parsed_json = json.loads(json_string)

   #these statements load our variables with the data from wunderground.com,
   #all the options if you would like to add to this can be found by printing
   #out <json_string>
   location    = parsed_json['location']['city']
   temp_f      = parsed_json['current_observation']['temp_f']
   feelslike_f = parsed_json['current_observation']['feelslike_f']
   condition   = parsed_json['current_observation']['weather']
   weather_report(location, temp_f, feelslike_f, condition)



'''
Name:       weather_report()
Parameters: location, temp_f, feelslike_f, condition
Return:     None
Purpose:    prints out the weather in a formatted manner
'''
def weather_report(location, temp_f, feelslike_f, condition):
   print "-------The Weather in %s-------" %location
   print "Temperature: \t\t %sF"           %temp_f
   print "What it feels like: \t %sF"      %feelslike_f
   print "The condition: \t\t %s\n\n"      %condition 


greeting()
get_weather()

#-------------non weather features below this point-------------------

#this function calcs the days until an event, in this case 2
def days_until():
   #couldn't get it to work without assiging them like this
   year = time.strftime("%Y")
   month = time.strftime("%m")
   day = time.strftime("%d")

   print "-------Days Until Fun Things----------"
   
   #----------------spring break----------------------------
   current_date_ymd = date(int(year), int(month), int(day))
   spring_break_date = date(2014, 03, 24)

   delta = spring_break_date - current_date_ymd
   if(delta != 0):
      print "Spring break: \t\t %s"    %delta.days
      
   #-----------------anniversary----------------------------
   if int(month) == 12:
      year = int(year) + 1
      month = 1

   if int(day) > 9:
      month = int(month) + 1
      
   anniversary_date = date(int(year), int(month), 9)
   
   delta = anniversary_date - current_date_ymd
   print "Monthly Anniversary: \t %s"        %delta.days

   #-----------------birthday-------------------------------
   if int(month) == 12 and int(day) >= 24:
      year = int(year) + 1
   birthday_date = date(int(year), 12, 23)

   delta = birthday_date - current_date_ymd
   print "Your Birthday: \t\t %s"        %delta.days   




   
days_until()

















