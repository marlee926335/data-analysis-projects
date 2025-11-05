# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
starting_fuel_level = 0
astronauts_aboard = 0
shuttle_altitude = 0


# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 


'''while starting_fuel_level < 5000 or starting_fuel_level > 30000:
    starting_fuel_level = int(input('Enter fuel level (must be positive)'))
    if starting_fuel_level < 5000 or starting_fuel_level > 30000:
        print("Please enter a diffeerent number.")
    else:
        print("Confirming level: ", str(starting_fuel_level))'''


# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
  
'''while astronauts_aboard <= 0:
      astronauts_aboard = int(input('How many astronauts are on board?'))
      if astronauts_aboard <= 0 or astronauts_aboard > 7:
         print("Invalid entry, please enter astronauts aboard (max 7).")
      else:
         print("Confirmed astronauts onboard: ", str(astronauts_aboard))'''
    
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle.
#Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

while starting_fuel_level - 100 * astronauts_aboard >= 0:
    fuel_level -= 100*astronauts_aboard
    altitude += 50


# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

print('The shuttle gained an altitude of ', shuttle_altitude, 'km and has ', starting_fuel_level, 'kg of fuel left')
if shuttle_altitude >= 2000:
    print('Orbit achieved!')
else:
    print('Failed to reach orbit.')

