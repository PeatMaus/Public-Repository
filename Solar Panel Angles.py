import math
from datetime import datetime

current_date = input("Date: ")
current_latitude = int(input("Enter latitude: "))
#change

current_date = datetime.strptime(current_date, '%m-%d-%y')
julian_current_day = current_date.timetuple()
julian_current_day = julian_current_day.tm_yday

spring_equinox = "3-21-23"
spring_equinox_datetime = datetime.strptime(spring_equinox, '%m-%d-%y')
spring_equinox_datetime_tuple = spring_equinox_datetime.timetuple()
spring_equinox_datetime_julian = spring_equinox_datetime_tuple.tm_yday
if julian_current_day <= spring_equinox_datetime_julian:
    julian_spring_day = 365 - spring_equinox_datetime_julian + julian_current_day
else:
    julian_spring_day = julian_current_day - spring_equinox_datetime_julian

max_solar_degrees = 23 + 27/60
angle_of_sun = math.sin(math.radians((360*julian_spring_day)/365.25))
solar_declination = max_solar_degrees*angle_of_sun
angle_of_panel = current_latitude - solar_declination
print(f"\nAngle of solar panels should be {angle_of_panel} degrees.\n")