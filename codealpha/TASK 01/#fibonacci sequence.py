# Fibonacci Sequence Generator

def fibonacci_series(n):
    if n <= 0:
        return []

    series = [0, 1]

    for _ in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)

    return series[:n]  


try:
    terms = int(input("Enter the number of Fibonacci terms: "))
    result = fibonacci_series(terms)
    print("Fibonacci Series:")
    print(result)
except ValueError:
    print("Please enter a valid integer.")
