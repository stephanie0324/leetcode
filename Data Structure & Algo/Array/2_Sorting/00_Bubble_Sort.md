# What is bubble sort? 

> [!NOTE]
> **Moving the value one by one, making the small to the front, and large value to the end of the array**

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. 

<p align="center">
    <img width="300" src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif?20131109191607" alt>
    <br>
    <em>Bubble Sort</em>
</p>

# The Process
1. [**Starting from the first element**](): Begin at the first element of the array.
2. [**Compare adjacent elements**](): Compare the current element with the next element in the array.
3. [**Swap if necessary**](): If the current element is greater than the next element, swap them.
4. [**Move to the next element**](): Move to the next pair of elements and repeat the comparison and swap if needed.
5. [**Complete a pass**](): Continue this process until the end of the array is reached. This completes one full pass.
6. [**Repeat the process**](): Start again with the first element of the array for the next pass.

# The Code
```python
def bubble_sort(elements):

  n = len(elements)

  for i in range(n-1): # we only have to run n-1 time for all the elements to be in the right spot
    for j in range(n-1-i): # since every i loop, only n-1 elements need to be sort
      if elements[j] > elements[j+1]: #swap
        tmp = elements[j+1]
        elements[j+1] = elements[j]
        elements[j] = tmp
  return elements

if __name__ =='main':
  elements = [5,9,2,1,67,34,88,34]

  bubble_sort(elements)
  print(elements)

```
# Time Complexity / Space Complexity / Overall Analysis
* The best scenario : $O(n)$
* The worst scenario : $O(n^2)$
* Space complexity : $O(1)$
* Use case: since bubble sorts repeatedly sort all the values, it would work better when you have a small set of data
* Sorting stability: it doesn't change the position of two equal value => **STABLE**
