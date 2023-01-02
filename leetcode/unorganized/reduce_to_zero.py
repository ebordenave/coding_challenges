# This is a simulation problem; all we have to do to arrive at the correct result is follow the instructions. Through
# this problem, you will learn how to identify if a number is even or odd (hint, think about the modulo operator from
# the previous problem). For those who are looking for an added challenge, you can try solving this problem using
# bitwise operations. Both methods are introduced in the video solution. We encourage you to try solving 1342. Number
# of Steps to Reduce a Number to Zero on your own first, then return here to watch the video solution.

def numberOfSteps (self, num):
    steps = 0 # We need to keep track of how many steps this takes.
    while num > 0: # Remember, we're taking steps until num is 0.
        if num % 2 == 0: # Modulus operator tells us num is *even*.
            num = num // 2 # So we divide num by 2.
        else: # Otherwise, num must be *odd*.
            num = num - 1 # So we subtract 1 from num.
        steps = steps + 1 # We *always* increment steps by 1.
    return steps # And at the end, the answer is in steps so we return it.

