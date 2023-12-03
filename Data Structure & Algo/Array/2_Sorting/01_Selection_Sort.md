# What is selection sort? 

> [!NOTE]
> For every spot we choose the smallest value from spot+1 to swap

<p align="center">
    <img width="300" src="https://tutorialhorizon.com/static/media/algorithms/2019/01/Selection-Sort-Gif.gif" alt>
    <br>
    <em>Bubble Sort</em>
</p>

# The Process
1. [Start with the entire array](): Initially, the sorted sublist is empty, and the unsorted sublist is the entire array.
2. [Find the minimum element in the unsorted sublist](): Scan the unsorted sublist to find the minimum (or maximum, depending on the desired sorting order) element.
3. [Swap with the first unsorted element](): Swap the found minimum element with the first element of the unsorted sublist.
4. [Expand the sorted sublist](): After the swap, the sorted sublist is expanded by one element, and the unsorted sublist is reduced by one element.
5. [Repeat the process](): Repeat the above steps for the remaining unsorted sublist (ignoring the elements already sorted).

# The Code
```python
def selection_sort(self, elements:[int])->[int]:
  min_ = float(inf)

  n = len(elements)
  for i in range(n-1)):
    min_ = i
    for j in range(i+1,n):
      if elements[j] < elements[min_]:
        min_ = j
    if i != min_:
      elements[i] , elements[min_] = elements[min_], elements[i]
  return elements
    

if __name__ =='main':
  elements = [5,9,2,1,67,34,88,34]

  selection_sort(elements)
  print(elements)

```
# Time Complexity / Space Complexity / Overall Analysis
* Time complexity : $O(n^2)$
* Space complexity : $O(1)$
* Use case: since bubble sorts repeatedly sort all the values, it would work better when you have a small set of data
* Sorting stability: **UNSTABLE**  
  The most pertinent example being: Given [2, 2, 1], the '2' values will not retain their initial order in the output sorted array.
  ```bash
  [2',2,1] -> [1,2,2']
  ```
