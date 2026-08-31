# the iterative method
def iterative_sum(start, end):
    result = 0
    for n in range(start, end+1):
        result += n
    return result

# the recursive method
def recursive_sum(start, end):
    if start == end:
        return start
    return start + recursive_sum(start+1, end)

def factorial(n, res):
    if n==1:
        return res
    return factorial(n-1, res*n)

if __name__ == "__main__":
    print(iterative_sum(5, 10))
    print(recursive_sum(5, 10))
    print(factorial(5, 1))