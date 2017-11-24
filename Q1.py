class Fibonacci:
    def get_nth_fibonacci(self, n):
        fib = [0, 1]

        if n == 0:
            return fib[0]
        if n == 1:
            return fib[1]

        i = 2
        while i < n:
            fib.append(fib[i - 1] + fib[i - 2])
            i += 1

        return fib[n - 1]

if __name__ == "__main__":
    f = Fibonacci()
    print f.get_nth_fibonacci(4)
