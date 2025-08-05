# Number of terms
n = 5

# First two terms
a, b = 0, 1

print("Fibonacci series till 5th term:")

for i in range(n):
    print(a)
    a, b = b, a + b
