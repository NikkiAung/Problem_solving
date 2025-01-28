# Problem Solving With Python

## Array Questions

1. containDuplicate 
   - Use set() 

2. ValidAnagram
    #### Solu1
    - Use Counter or deafault hashmap to get | 'd' : 1 | and check if they are equal

    #### Solu2
    - Take advatage of ord char to get unique index
    - | += 1 cancel wth -=1 |

3. Two Sum
    - Use Target-currNum formula recheck wth hashmap

4. GroupAnagrams
    - Take advatage of ord char to get unique index
    - Use Hashmap to store same index no. count str into list

5. Top K Frequent Elements
    - Purpose to elect the most frequent one at top of the level
    - Use Bucket Sort
    - Range for len of arr, cuz it is not beyond more than that