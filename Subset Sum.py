

from typing import List

def subsetSum(num: List[int]) -> List[int]:
    finRes = []
    def helper(ind, currSum, subRes):
        if(ind >= len(num)):
            finRes.append(currSum)
            return
        helper(ind+1, currSum, subRes)
        subRes.append(num[ind])
        helper(ind+1, currSum+num[ind], subRes)
        subRes.pop()
        
    helper(0, 0, [])
    
    return sorted(finRes)
