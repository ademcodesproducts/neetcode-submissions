class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # bottom up dp approach
        # first loop for base case
        # second pass for 1 dp array
        # left all the balls to the left, right all the balls to the right of i

        n = len(boxes)
        answer = [0] * n

        left, right = 0, 0

        for i in range(n):
            if boxes[i] == "1":
                answer[0] += i
                right += 1
        
        for i in range(n - 1):
            if boxes[i] == "1":
                left += 1
                right -= 1

            answer[i + 1] = answer[i] + left - right

        return answer