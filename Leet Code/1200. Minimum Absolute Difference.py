class Solution:
    def minimumAbsDifference(self, A):
        A.sort()
        D = [ A[i+1]-A[i] for i in range(len(A)-1) ]
        target = min(D)
        res    = []
        for i,d in enumerate(D):
            if d == target:
                res.append([ A[i],A[i+1] ])
        return res

    