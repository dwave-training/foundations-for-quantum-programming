# Use a For Loop
A business wants to pack a shipping container. The objective is to maximize the total value, in dollars, of $N$ total objects that can fit in the container. 

- The binary variable, $x_i $, represents whether the object is in the shipping container. If $x_i = 1$, item $i$ is in the container. If $x_i = 0$, item $i$ is not in the container.
  
- The coefficient $c_i$ represents the cost of each item.
  
- The optimization objective is: 

$$ \min - \sum_{i=1}^N c_i x_i $$


For this assignment, you will use a for loop to return the value of the optimization objective when:

- The total number of items to select from is $N = 4$.	

- The cost of the items are $5, $10, $3, and $4, respectively. 

- Items 2 and 4 are packed in the container. 


## Exercise

The Python file that you will work on is named ``forloop_practice.py``.  Open it, then follow the instructions below:

1. Create two new lists:

- Name the first list ``costs``. Add the following values, in order, to the list: 5, 10, 3. This list represents the cost of each item.

- Name the second list ``items``. Add the following values, in order, to the list: 0,1,0,1. This list represents if the item is packed in the shipping container. When the value is equal to 1, it is included in the container; if it is equal to 0, it is not in the container.
  
2. Your final answer will be stored in ``value``. To begin, set ``value = 0``. This will change as the program runs.
   
3. On a separate line, use a for loop to calculate the following:
   
$$ - \sum_{i=1}^4 \texttt{costs}_i * \texttt{items}_i $$

 and then store the sum in ``value``.
   
4. Print the ``value`` of the optimization objective to your terminal.
