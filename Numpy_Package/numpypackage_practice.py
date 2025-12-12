#TODO: Import the NumPy package and abbreviate it as np


#TODO: Create the distance array, D, using NumPy


#TODO: Create a 1D array, x, that contains a random ordering of the 5 places
# Hint: Use a built-in NumPy function 


# Print the array x
print("The order in which each place is visited is:", x)

# Distance between consecutive places, excluding return trip to the origin place
itinerary = D[x[:-1], x[1:]]

# Print the array itinerary
print("The distances between consecutive places, excluding return trip to the origin place is:", itinerary)

#TODO: Compute the total distance traveled between consecutive places, excluding return trip to the origin place. 
# Hint: Use the .sum() method


# Print the total distance traveled, excluding return trip to the origin
print("The total distance traveled, excluding return trip to the origin is:", sum_of_itinerary)

#TODO: Compute the distance between the last place and the starting place


# Print the value of the return to origin
print("The distance between the last place and the starting place is:", return_to_origin )


#TODO: Compute the total distance traveled between places including the return to origin


# Print the value of the total distance
print("The total distance traveled between locations, including the return to origin is:", total_distance)
