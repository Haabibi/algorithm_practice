
Array questions & string questions are interchangeable! 

### Hash Tables
**Maps keys to values for highly efficient lookup**
#### Implementation 
* an array of linked lists 
* a hash code function

To insert a key and a value, which can be any type, do the following:
1. compute key's hash code (type: int/ long), and there might be conflicts in hash codes


2. map the hash code to an index in the array by hash(key) % array_length. This can also cause conflicts as two different hash codes can be mapped  to the same index


3. use a linked list when collision happens


* The worst case runtime: O(N), where N is the # of keys
* In general, the lookup time is O(1), assuming a good implementation keeps collisions to a minimum
* O(logN): a hash table with a balanced search tree / less space as we don't allocate a large array 

### ArrayList and Resizable Arrays
**ArrayList** is an array that resizes itself. 
* O(1) accsess

### StringBuilder
Simply creates a resizable array of all the strings, copying them back to a string only when necessary 

**Try building my own version of *StringBuilder, HashTable & ArrayList***

