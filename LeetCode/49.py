"""
49. Group Anagrams
Medium
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    
    IMPLEMENTATION
    - make a dictionary while traversing through list 
    - make a string into a set
    - for the strings that map into the same set,
      - append the string into the list that is saved as a value 
      - key would be the set 
    - iterate the dictionary and append only the items of the dictionary
    : time complexity: O(N*MlogM)
      - N: number of words
      - M: length of strings 
    : space complexity: O(N + M + K) 
      - N: tmp_set: sorted array of chars in each string
      - M: tmp_key: hashable string to save as a key in the hash map 
      - K: output 
    """
    
    dictionary = {}
    for item in strs:
      tmp_set = sorted([char for char in item])
      tmp_key = ''
      for char in tmp_set:
        tmp_key += char 
        
      if tmp_key not in dictionary.keys():
        dictionary[tmp_key] = [item]
      else: 
        # if tmp_set in keys()
        dictionary[tmp_key].append(item)
      
    output = [ x[1] for x in dictionary.items()]
    
    return output
