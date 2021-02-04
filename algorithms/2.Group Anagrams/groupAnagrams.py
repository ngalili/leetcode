# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/


# Time complexity : O(N*M*log(M))
# N: length of the input array
# M: length of the biggest string in the array
# M*log(M) is due to the fact that we sort each string when we pass over it in the loop
# Space compexity: O(N)
# Due to the hash map we create to store our data 
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    answers = []
    hash_tbl = {}

    for string in strs:
        hashed = ''.join(sorted(string))
        if hashed not in hash_tbl:
            hash_tbl[hashed] = []
        hash_tbl[hashed].append(string)
    
    for value in hash_tbl.values():
        answers.append(value)
    return answers