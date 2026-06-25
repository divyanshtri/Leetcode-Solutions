class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        j = 0

        for i in range(1, n + 1):
            if i == target[j]:
                ops.append("Push")
                j += 1

                if j == len(target):
                    break
            else:
                ops.append("Push")
                ops.append("Pop")

        return ops   
    