# Application using NumPy Package
An individual is planning a driving trip to visit $n$ different locations exactly once. They want to drive the shortest distance possible to see all $n$ locations. The objective is to minimize the distance traveled between locations and then return to the origin.


- The variable, $x$, represents the order of all locations the individual must visit.

- The array, $D$, is of size `n × n` and represents the travel distance (in kilometers) between each location, including the starting location. 

    **Note:** 
    - The distance from location $a$ to location $b$ is the same as the distance from location $b$ to location $a$, therefore $D[a,b]=D[b,a]$.
    - $D[a,a]$ is the distance from location $a$ to location $a$, so $D[a,a]=0$.

- The objective function is:
    $$
    \min \left[
    \underbrace{(D[x[:-1], x[1:]])}_{\substack{
    \text{Distance between} \\
    \text{consecutive locations,} \\
    \text{excluding the return trip} \\
    \text{ to the origin.}
    }}.sum()
    +
    \underbrace{D[x[-1], x[0]]}_{\substack{
    \text{Return trip to the} \\
    \text{ origin.}
    }}
    \right]
    $$

    **Note:** 
    - The first portion, `D[x[:-1], x[1:]]`, calculates the distance from one location to the next, excluding the return trip to the origin. Then, the sum operation `D[x[:-1], x[1:]].sum()` adds all of these distances together.
    - The second portion, `D[x[-1], x[0]]`, adds the distance between the last location and the start.
    - Taking the minimum of this expression over all possible permutations of `x` yields the shortest itinerary.

For this assignment, the goal is to use `numpy` to create an `n × n` distance array and a `1-D` array with randomly ordered elements using common built-in functions. Then, compute a few values based on these arrays. Assume the total number of locations to visit is $n = 5$.	

## Exercise

The Python file you will be working with is named `numpypackage_practice.py`.  Open it and follow the instructions below:

1. Import the `numpy` package and abbreviate it as `np`.

2. Using `numpy`, create the following two arrays:

    - An `n × n` distance array named `D`. 

        This array represents the distance, in kilometers, between locations. Populate the array with values shown in the graph below, where each node $p_i$ corresponds to location $i$, and each edge represents the distance between two locations. Assume that the rows and columns are labeled in the order of $p_0$, $p_1$, $p_2$, $p_3$, then $p_4$.
        
        <img src=resources/numpymap.png width="400">
        
    - A `1-D` array named `x`, which contains a random ordering of the 5 locations.
    
        This array represents the order in which each location is visited. When submitting this problem to a D-Wave solver, the solver will determine the shortest itinerary from all possible permutations. For this assignment, however, you will work with a random order. 
        
        **Hint:** Use a built-in numpy function to generate the random order.

        **Example:** Assume the order in which each location is visited is returned as $x = [3 \ 0 \ 1 \ 4 \ 2]$, which means that your itinerary is: $ \text{location}_3 \to \text{location}_0 \to \text{location}_1 \to \text{location}_4 \to \text{location}_2
    $

3. Compute the total distance traveled between consecutive locations, excluding the return trip to the origin. Define this value as `sum_of_itinerary`. 
    
    **Hint:** Use the `.sum()` method.
    
4. Compute the distance between the last location and the starting location, and store it in a variable named `return_to_origin`.
   
5. Compute the total distance traveled between locations, including the return trip to the origin, and store it as `total_distance`.

