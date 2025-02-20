"""
2657. Find the Prefix Common Array of Two Arrays
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once."""
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seen = [0] * (n+1)
        common = 0
        result = []

        for i in range(n):
            if seen[A[i]] == 0:
                seen[A[i]] = 1
            elif seen[A[i]] == 1:
                common += 1
            if seen[B[i]] == 0:
                seen[B[i]] = 1
            elif seen[B[i]] == 1:
                common += 1
            
            result.append(common)
        return result