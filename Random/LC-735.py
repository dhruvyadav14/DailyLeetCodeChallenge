class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        some observations:
        if there's a positive after a negative, those two will never collide
        i'm thinking stacks?
        keep a stack of positive and negative values
        loop through array, adding to that stack
        if num is positive, add to Pstack and add None to Nstack
        if the num is negative, add to Nstack and None to Pstack
        loop through len of asteroids, start from top of stacks

        if i encounter a negative number and i have a positive in my stack, have them collide. if i encounter a negative number and i dont have a positive in my stack, this asteroid will never collide with anybody.

        if i encounter a positive number, add it to positive stack. are there any other cases for a positive? i dont think so...if its positive, im not making collision decisions. only if its negative am i doing that.

        the only time collisions can happen is IF its a negative asteroid and we have seen a positive asteroid. oh dip. need to cover if the weights are the same

        we know we are done when all negative elements come before all positive elements 
        when we encounter a negative number, lets collide them with allll the positive numbers that came before it. if the negative number keeps winning, keep colliding. if eventually a positive number wins, thats where we stop and move on to the next
        """
                    

        PS=[]
        mylen = len(asteroids)
        for i in range(mylen):
            asteroid = asteroids[i]
            if asteroid < 0:
                while len(PS)>0 and abs(asteroid) > PS[-1][0]:
                    asteroids[PS[-1][1]] = None
                    PS.pop()
                if len(PS)>0:
                    if abs(asteroid) < PS[-1][0]:
                        asteroids[i] = None    
                    else:
                        asteroids[i] = None
                        asteroids[PS[-1][1]] = None
                        PS.pop()
            else:
                PS.append([asteroid,i])
        filtered_array = [value for value in asteroids if value is not None]
        return filtered_array

