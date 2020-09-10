class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        # set_list = {}            
        for string in strs:
            set_ = ''.join(sorted(string))
            if set_ not in result:
                # set_list.append(set_)
                result[set_] = []
                
            result[set_].append(string)
        return [val for val in result.values()]
    