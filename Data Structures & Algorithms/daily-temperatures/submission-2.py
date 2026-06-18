class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        lst = [0] * n
        stack = [] 
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                lst[stack_idx] = i - stack_idx
            
            stack.append((temp, i))

        return lst
        