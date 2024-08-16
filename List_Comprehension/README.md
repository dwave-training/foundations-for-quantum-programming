# Use List Comprehension
A business wants to pack a shipping container. The objective is to maximize the total value, in dollars, of $N$ total objects that can fit in the container. 

- The binary variable, $x_i $, represents whether the object is in the shipping container. If $x_i = 1$, item $i$ is in the container. If $x_i = 0$, item $i$ is not in the container.
  
- The coefficient $c_i$ represents the cost of each item $i$.
  
- The optimization objective is: 

$$ \min - \sum_{i=1}^N c_i x_i $$


For this assignment, the goal is to create a list comprehension that only returns the negative of the cost for each of the selected items. Assume:

- The total number of items to select from is $N = 4$.	

- The cost of the items are $5, $10, $3, and $4, respectively. 

- Items 2 and 4 are packed in the container. 


## Exercise

The Python file that you will work on is named ``listcomprehension_practice.py``.  Open it, then follow the instructions below:

1. Create two new lists:

- Name the first list ``costs``. Add the following values, in order, to the list: 5, 10, 3, 4. This list represents the cost of each item.

- Name the second list ``items``. Add the following values, in order, to the list: 0,1,0,1. This list represents if the item is packed in the shipping container. When the value is equal to 1, it is included in the container; if it is equal to 0, it is not in the container.
  
2. On a separate line, use list comprehension to create a new list and name it ``values``.
    
3. The ``values`` list should contain $- \texttt{costs}_i * \texttt{items}_i$ if the items are in the container. 
Hint: Use an if statement to provide a condition.  
   
4. Print the ``values`` list to your terminal.

**Note that if you add the elements in the ``values`` list, you will get the same output as the For Loop assignment!**
