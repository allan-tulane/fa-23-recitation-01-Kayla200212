[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11681113&assignment_repo_type=AssignmentRepo)
# CMPS 2200  Recitation 01

**Name (Team Member 1):**_Kayla Willis________________________  
**Name (Team Member 2):**_Cameron McLaren________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: The worst case input value that the key can be for a linear search would be the last or largest number in the sequence we are searching. Linear search checks the list from beginning (smallest) to end (largest), hence if our key was the largest number/last number, we would get the worst case runtime as the program would search every other possible number in the list before finding the key. In binary search, the worst case would be if the key was at the very beginning (lowest) or very end (biggest) of the list being searched. Binary search works to divide the list in half and constantly compare the numbers on either side of the middle number to the key in order to seek the key value. In both cases, though, if the key is a number not in the list, that case will have the longest runtime because the search will have to go through every possibility before exiting.**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: For linear search, the best case input key would be the lowest number that is in the list, because that would be the first number in the list. The key would be the first value found and the program would exit. The best case for binary search would be if the key was the number directly in the middle of the list. The closer the value is to the middle middle of the list, while still being a number that exists in the list, would be the fastest case for binary search.**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO
|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.005 |    0.005 |
|      100.000 |    0.012 |    0.006 |
|     1000.000 |    0.131 |    0.013 |
|    10000.000 |    1.837 |    0.021 |
|   100000.000 |   13.678 |    0.025 |
|  1000000.000 |  277.819 |    0.053 |
| 10000000.000 | 2289.167 |    0.042 |**

- [ ] 9. The theoretical worst-case running time of linear search is O(n) and binary search is O(log_2(n)). Do these theoretical running times match your empirical results? Why or why not?

**TODO: Roughly yes, because we know that the time complexity of O(n) is a worse runtime than log(n). The results show this because as the n increases, the time that a linear search takes increases by many magnitudes while binary increases at a much slower rate. **

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes Theta(n^2) time to sort a list of length n. Suppose you know ahead of time that you will search the same list k times. 
  + What is worst-case complexity of searching a list of n elements k times using linear search? **TODO: k*O(n) because the time complexity is O(n) for one list, so to search the list k times, you can multiply k times by searching it one time**
  + For binary search? **TODO: k * O(log(n)) because the same logic applies as above from linear search**
  + For what values of k is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: The time complexity for sorting the list then using binary search would be theta n^2 + k*log(n), basically adding together the time complexity of sorting then searching. The complexity for linear searching without sorting would be theta k * n because the time complexity is O(n) regularly and if unsorted, you would still have to multiply it by k searches. Because of this, binary searching should be more efficient. If you set up an inequality where the runtime of the binary search is less than the runtime of the linear search, you can solve it for k to get: k<-n^2/(log(n)-n). k must fall in this range**