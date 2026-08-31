def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    sum = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = sum
    return sum


print(fibonacci(6, {0: 0, 1: 1}))
