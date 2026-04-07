class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # n=len(matrix)
        for i in matrix:
            for j in i:
                if j==target:
                    return True
        return False
