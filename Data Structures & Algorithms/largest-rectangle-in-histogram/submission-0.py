class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                    width = i -stack[-1]-1
                else:
                    width = i
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
            height=heights[stack.pop()]
            if stack:
                width = n -stack[-1]-1
            else:
                width = n
            max_area = max(max_area, height * width)
        return max_area
   
        