class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        # Generate hash maps
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0) #.get en hash me retorna el valor o si no existe el segundo valor
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        #iterate through the keys
        for i in hashS:
            if hashS[i] != hashT.get(i, 0):
                return False
        return True