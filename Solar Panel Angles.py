import math
from datetime import datetime

#User entered data
current_date = input("Date, e.g. (2-14-24): ")
current_latitude = int(input("Enter latitude: "))
length_of_solar_panel = int(input("Enter length of pivot point to connection of support on panel in inches: "))

#To resolve date into Julien date
current_date = datetime.strptime(current_date, '%m-%d-%y')
julian_current_day = current_date.timetuple()
julian_current_day = julian_current_day.tm_yday

#To resolve Spring Equinox into Julien date
spring_equinox = "3-21-23"
spring_equinox_datetime = datetime.strptime(spring_equinox, '%m-%d-%y')
spring_equinox_datetime_tuple = spring_equinox_datetime.timetuple()
spring_equinox_datetime_julian = spring_equinox_datetime_tuple.tm_yday

#To resolve Julien day for correct calulation - Spring equinox + date entered
if julian_current_day <= spring_equinox_datetime_julian:
    julian_spring_day = 365 - spring_equinox_datetime_julian + julian_current_day
else:
    julian_spring_day = julian_current_day - spring_equinox_datetime_julian

#To resolve the position of sun in relation to the equator
max_solar_degrees = 23 + 27/60
angle_of_sun = math.sin(math.radians((360*julian_spring_day)/365.25))
solar_declination = max_solar_degrees*angle_of_sun

#To obtain the angle of the solar panel in relation to latitude
angle_of_panel = round(current_latitude - solar_declination)

#figure length of support in inches
length_of_support = round(length_of_solar_panel * math.tan(math.radians(angle_of_panel)))

#print answers
print(f"\nAngle of solar panels should be {angle_of_panel} degrees.\n")
print(f"length of support for {length_of_solar_panel} inch solar panel: {length_of_support} inches.")
