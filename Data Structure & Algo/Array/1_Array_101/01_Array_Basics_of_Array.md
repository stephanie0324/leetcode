
# 1. Info
> An array is a collection of similar data elements stored at contiguous memory locations. It is the simplest data structure **where each data element can be accessed directly by only using its index number.**  

<p align="center">
    <img width="500" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/array.png" alt>
    <br>
    <em>Array</em>
</p>

### Array consists of:
> * starting address
> * dimension
> * index upper and lower bound (len of the array)
> * num of the val
> * array type, e.g.: int ,string, float...

## 1.1 Multi-Dimension Array
The arrays mentioned above only have one dimension, and their data elements are also single subscript variables. However, in practical problems, a lot of information is two-dimensional or multi-dimensional, the one-dimensional arrays no longer meet our needs, hence the emergence of multi-dimensional arrays.  
<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/2d_array.png">
    <br>
    <em>2D Array</em>
</p>
Above is a two-dimensional array. Most of the cases are in 2-D, <mark> we could also see them as **matrices** </mark>, and apply functions on them, e,g, matrix addition, multiplication, division and subtraction.

# 2. Basic Operation on Array
> 📘 **Definitions**
> * **$i$ is valid** means that `0 <= i <= len(Arr)`
## 2.1 Visiting Elements
To access the i-th element in the array:
1. It is necessary to check whether the range of i is within the legal range, that is `0 ≤ i ≤ len(nums)−1`. *Accessing beyond this range is considered illegal access.*
2. When the position is legal, the value of the element is obtained from the given index.
> #### Time complexity: O(1).

```ruby
# get the value of the ith index
def value(nums, i):
    if 0 <= i <= len(nums) - 1:
        print(nums[i])
        
arr = [0, 5, 2, 3, 7, 1, 6]
value(arr, 3) # return 3
```
## 2.2 Finding Elements
Find $x$ in the list:
1. Check all the elements in the array one by one to find $x$.
2. Return the index of $x$
3. Return -1 if $x$ not found
> #### Time complexity:O(N).
```ruby
def find(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1

arr = [0, 5, 2, 3, 7, 1, 6]
print(find(arr, 5)) # return 1
```
## 2.3 Insert Element
We can divide this operation into 2 kinds:
- insert the val at the end of the array 
- insert the val at index $i$
### 2.3.1 Insert at end $\rightarrow$ `append`
1. if the array hasn't reach the end, we update the first empty spot to val
2. if the array is full, it will automatically create a spot and insert the val
> #### Time complexity : O(1)

<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/append.png">
    <br>
    <em>append</em>
</p>

### 2.3.2 Insert at $i$ $\rightarrow$ `insert`
1. normally there would be a val in index $i$, so we need to move i~n into i+1 ~n+1
2. than we insert the value at $i$
> #### Time complexity: O(N).
<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/insert.png">
    <br>
    <em>insert</em>
</p>


## 2.4 Changing the Value
We want to update the value of $i$ into $v'$
1. check if 0 <= i <= len(Arr)
2. update the value of $i$
> #### Time complexity: O(1).  
<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/change_val.png">
    <br>
    <em>change value</em>
</p>

## 2.5 Delete Element
We can divide this operation into 3 scenarios:
- delete the last element
- delete the $i$th element
- delete elements under certain condition
### 2.5.1 delete the last element $\rightarrow$ `pop`
> #### Time complexity: O(1).
<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/pop.png">
    <br>
    <em>pop</em>
</p>

### 2.5.2 delete element of $i$ th index
1. check if $i$ is valid
2. pop $i$ th val, and move the i+1 elements to the left
3. len(Arr) = len(Arr)-1
> #### Time complexity: O(N).  
<p align="center">
    <img width="300" src="https://github.com/stephanie0324/leetcode/blob/main/Data%20Structure%20%26%20Algo/Array/1_Array_101/delete.png">
    <br>
    <em>delete</em>
</p>

### 2.5.3 delete with condition $\rightarrow$ `remove`
We delete one or more elements by the given condition.
> #### Time complexity: O(N).
```ruby
arr = [0, 5, 2, 3, 7, 1, 6]
arr.remove(5) # remove element 5
print(arr)
```
# 3. Summary
Arrays are the most basic and simplest data structure. Arrays are the basis for implementing sequential storage of linear lists. They use a set of continuous memory spaces to store a group of data with the same type.

<mark>The biggest feature of arrays is their support for random access.</mark> Accessing and modifying array elements has a time complexity of O(1), and inserting or deleting elements at the end of the array also has a time complexity of O(1). Under ordinary circumstances, the time complexity for inserting or deleting elements is O(n).
