# Application using NumPy Package
An individual is planning a driving trip to visit $n$ different locations exactly once. They want to drive the shortest distance possible to see all $n$ locations. The objective is to minimize the distance traveled between locations and then return to the origin.


- The variable, $x$, represents the order of all locations the individual must visit.

- The array, $D$, represents the travel distance between each location (in kilometers), including the starting location. It is of size `n × n` . 

    **Note:** 
    - The distance from location $a$ to location $b$ is the same as the distance from location $b$ to location $a$, therefore $D[a,b]=D[b,a]$.
    - $D[a,a]$ is the distance from location $a$ to location $a$, so $D[a,a]=0$.

- The objective function is:
    $$
    \min \left[
    \underbrace{(D[x[:-1], x[1:]])}_{\substack{
    \text{Distance between} \\
    \text{consecutive locations,} \\
    \text{excluding return trip} \\
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
    - The first portion, `D[x[:-1], x[1:]]`, calculates the distance between one location to the next, excluding the return trip to the origin. Then, the sum operation `D[x[:-1], x[1:]].sum()` sums the distances.
    - The second portion, `D[x[-1], x[0]]` adds the distance between the last place and the starting place.
    - Taking the minimum of this expression over all possible permutations of `x` yields the shortest itinerary.

For this assignment, the goal is to use `numpy` to create a `n × n` distance array and a `1-D` array with randomly ordered elements using common built-in functions. Then, compute a few values based on these arrays. Assume:

- The total number of places to visit is $n = 5$.	

- The distance, in kilometers, between the places is represented as a graph,
where each node $p_i$ corresponds to the location of place $i$, and each edge represents the distance between two places.

## Exercise

The Python file you will be working with is named `numpypackage_practice.py`.  Open it and follow the instructions below:

1. Import the `numpy` package and abbreviate it as `np`.

2. Using `numpy`, create the following two arrays:

    - An `n × n` distance array, and name it `D`. 

        This array represents the distance, in kilometers, between the places. Fill the array using the values shown in the graph below (assume the rows and columns are labeled in the order of $p_0$, $p_1$, $p_2$, $p_3$, then $p_4$):
        
        <img src=resources/numpymap.png width="400">
        
    - A `1-D` array, and name it `x`, that contains a random ordering of the 5 places.
    
        This array represents the order in which each place is visited. When submitting this problem to a D-Wave solver, the solver will determine the shortest itinerary from all possible permutations. For this assignment, however, you will work with a random order. 
        
        **Hint:** Use a built-in numpy function to generate the random order.

        **Example:** Assume the order in which each place is visited is returned as the following $x = [3 \ 0 \ 1 \ 4 \ 2]$, this means that your itinerary is: $ \text{place}_3 \to \text{place}_0 \to \text{place}_1 \to \text{place}_4 \to \text{place}_2
    $

3. Compute the total distance traveled between consecutive places, excluding the return trip to the origin place. Define this value as `sum_of_itinerary`. 
    
    **Hint:** Use the `.sum()` method.
    
4. Compute the distance between the last place and the starting place, and store it in a variable named `return_to_origin`.
   
5. Compute the total distance traveled between places, including the return to origin, and store it as `total_distance`.

