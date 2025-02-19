# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the 
# ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j 
# if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move 
# all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.
class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        lista = [int(digit) for digit in boxes]
        result = []
        for i in range(n):
            moves = 0
            for j in range(n):
                if i != j and lista[j] == 1:
                    moves += abs(i - j)
            result.append(moves)
        return result