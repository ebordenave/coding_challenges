# FizzBuzz is a childhood game that iterates over a range of numbers and uses simple logic to decide whether to say a
# "Fizz," "Buzz," or a number. Through this problem, you will learn to convert that logic into code, and you will be
# introduced to frequently used operations like modulo and string concatenation. We encourage you to try solving 412.
# Fizz Buzz on your own first, then return here to watch the video solution.


def fizzBuzz(self, n: int) -> List[str]:
    ls = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            ls.append("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            ls.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            ls.append("FizzBuzz")
        else:
            ls.append(str(i))
    return ls
