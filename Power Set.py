def pwset(v):
    finRes = []
    def helper(ind, subRes):
        if(ind == len(v)):
            finRes.append(subRes[:])
            return
        helper(ind+1, subRes)
        subRes.append(v[ind])
        helper(ind+1, subRes)
        subRes.pop()
        
    helper(0, [])
    return finRes
