# CISC121_002_Project_Nguyen_Jimmy
## Python App - Insertion Sort Demo


I chose insertion sort because it is a great way to introduce sorting to a beginner. This was the first sorting method I learned and the first we saw in class (likely for the same reason) so in the "teaching mindset" this was my first choice. This sorting algorithm is also a cool one to see visually seeing the shifts and insertions happening at each step. 

### Screenshots of Test

##### Working Cases
Here I tested the two edge cases for the array size and a random example as well. 

<img width="2880" height="1622" alt="edge_case(btm)" src="https://github.com/user-attachments/assets/2124c53d-0e59-494f-b478-516990c85bb3" />
<img width="2880" height="1620" alt="edge_case(top)" src="https://github.com/user-attachments/assets/fe686229-7a65-401b-85e1-a71cfc06e828" />
<img width="2880" height="1622" alt="example" src="https://github.com/user-attachments/assets/32f88a9b-f0f9-4596-8a50-3d12e9c5e937" />

#### User Error Messages
**Early Sort:** If the user presses the "*Run Insertion Sort*" button before doing anything else
<img width="2880" height="1624" alt="early_sort" src="https://github.com/user-attachments/assets/b390be8a-4c5d-437c-9a8a-0fad181b8206" />

**Non-Integer Size or Max:** If the user inputs anything other than an integer
<img width="2880" height="1606" alt="non-integer_size" src="https://github.com/user-attachments/assets/465e1f94-40fb-4137-ab33-b9739afdedaa" />
<img width="2880" height="1620" alt="non-integer_max" src="https://github.com/user-attachments/assets/fcf3c1de-99a6-46be-be64-8389d716a09a" />

**Invalid Size or Max:** If an integer is inputted by the user, but it is outside of the constrictions I set within the code (to limit the number of steps)
<img width="2880" height="1624" alt="invalid_size" src="https://github.com/user-attachments/assets/049258f7-0f50-42e8-9258-25a4a85941e8" />
<img width="2880" height="1622" alt="invalid_max" src="https://github.com/user-attachments/assets/811630c9-d353-44cc-8032-4244790a6d24" />


### Computational Thinking
**Decompostion**: What smaller steps form your chosen algorithm? 
- For each element in the list (from left to right):
    - check if it is smaller than the elements to its left
    - if it is; shift the 'larger' elements to the right
    - continue left until a smaller element (say *A*) is reached (smaller than our current)
    - "insert" the element to the right of *A*
 
**Pattern Recognition**: How does it repeatedly reach, compare, or swap values? 
- We will repeatedly be taking each element and comparing it to the elements to the left of it in the array
- While it is smaller (during these comparisons), we repeatedly shift the larger elements to the right until a smaller element is hit

**Abstraction**: Which details of the process should be shown to the user and how to show it, and which details should be discarded? 
- We should show the comparison of the current element vs. the elements to its left
- We should also show the 'shifting' of larger elements and 'insertion' of the current element once the smaller element is hit
  - My plan to show these details is to output every step to the user so they can see every update happening to the array
- We don't have to show the increase of the index on our element at the 'insertion' part to our user since this is not a main feature of insertion sort (although this could be a very good debugging problem for someone first learning this algorithm)

**Algorithm Design**: How will input $\to$ processing $\to$ output flow to and from the user? Including the use of the graphical user interface (GUI). 
- Ask the user to input an array size and maximum allowed value for the array to hold
- User will press a button to generate the (unsorted) list (GUI)
- A function creating a random list will run in the backround created using the two parameters the user inputed in the previous step
- Unsorted list is displayed to the user
- User will press a button to sort the list that was generated (GUI)
- Insertion sort will run in the backround displaying the array at each step (comparisons, shifts, insertions) to the user
- Output will be the now sorted list (which is displayed to the user)

Note: By construction, the only datatypes allowed will be integers and the structure into the insertion sort will always be a list of integers. 

#### Flowchart

<img width="980" height="1068" alt="Project_Flowchart" src="https://github.com/user-attachments/assets/d0e14943-afd6-4a26-be2f-e13c9262ccd3" />

### Steps to Run
1. Input an integer for the array size (between 1 and 10)
2. Input an integer for the maximum allowed value in the array (greater than 0)
3. Press *Generate Array* button 
4. Press *Run Insertion Sort* button (if an array is generated in the last step)

### Hugging Face Link:
https://huggingface.co/spaces/20jmdn/CISC121-Project

### Author & Acknowledgement
Author: Jimmy Nguyen

Section: 002

ID: 2027 1459

Acknowledgements: I used ChatGPT level 4 to help me display the outputs to the user in a more visually pleasing way.
