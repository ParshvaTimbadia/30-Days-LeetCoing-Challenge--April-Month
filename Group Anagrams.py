***
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
.
***




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result=[]
        list={}
        for word in strs:
            Sortedword= "".join(sorted(word))
            
            if Sortedword not in list:
                list[Sortedword]=[word]
            else:
                list[Sortedword].append(word)
                
                
        for i in list:
            result.append(list[i])
            
        return result    
