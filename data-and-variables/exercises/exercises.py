# 1. Declare and assign the variables here:
space_shuttle = 'Determination'
shuttle_speed_mph = 17500
dist_to_mars_km = 225000000
dist_to_moon_km = 384400
miles_per_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(space_shuttle))
print(type(shuttle_speed_mph))
print(type(dist_to_mars_km))
print(type(dist_to_moon_km))
print(type(miles_per_km))

# Code your solution to exercises 3 and 4 here:
miles_to_mars = dist_to_mars_km * miles_per_km
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24

print(space_shuttle +' will take ' + str(days_to_mars) +' days to reach Mars.')

# Code your solution to exercise 5 here
miles_to_moon = dist_to_moon_km * miles_per_km
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(space_shuttle +' will take ' + str(days_to_moon) +' days to reach the Moon.')
