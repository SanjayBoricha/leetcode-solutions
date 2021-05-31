class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        right = 0
        left = 0

        combinations = []

        currentSum = candidates[0]

        while(left < len(candidates) and right < len(candidates)):

            print(currentSum)

            if(currentSum == target):
                print({'right': right, 'left': left})
                combinations.append(candidates[right:left + 1])

            if(currentSum > target):
                print('greater')
                currentSum = currentSum - candidates[right]
                right += 1

            else:
                left += 1

                if(left < len(candidates)):
                    currentSum += candidates[left]

            # if(currentSum < target):
            #     left += 1

        return combinations


print(Solution().combinationSum([2, 3, 5], 8))
