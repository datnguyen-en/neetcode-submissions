class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        countt = 0  
        n = len(temperatures)
        lst = []
        for i in range(0, n):
            countt = 0
            for j in range(i + 1, n):
                countt += 1
                if temperatures[i] < temperatures[j]:
                    lst.append(countt)
                    break
                elif j == n - 1:
                    lst.append(0)
                    break

        lst.append(0)

        return lst