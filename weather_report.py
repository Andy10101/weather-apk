#!/usr/bin/python
import urllib2, json, getpass, time

'''
This program gets weather data from api.wunderground.com and tells you
the current temperature in F, what it feels like outside in F, and the
condition (i.e. overcast, snow, clear etc). It gets the time from your
computer using strftime().
By Sean McConnell.
'''



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
   Also please use your API, they're available from wunderground.com
   '''
   f = urllib2.urlopen('http://api.wunderground.com/api/3683c1e808f1d752/geolookup/conditions/q/Thailand/Bangkok.json')
   #print this to see all the information you could dispaly instead of just the 4 I did
   json_string = f.read()

   #json is basically a complex dictionary and commonly used when communicating with web servers
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
   print "The condition: \t\t %s"          %condition 


def main():
   greeting()
   get_weather()


if __name__ == "__main__":
   main()
