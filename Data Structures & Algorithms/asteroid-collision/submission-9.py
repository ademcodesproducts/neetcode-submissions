class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                alive = True
                while stack and stack[-1] > 0:
                    if -a > stack[-1]:
                        stack.pop()
                    elif -a == stack[-1]:
                        stack.pop()
                        alive = False
                        break
                    else:
                        alive = False
                        break # keep for invariant clarity
                if alive:
                    stack.append(a)
                    
        return stack