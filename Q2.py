# a is a list of integers

def find_minimum_loss(a):
    a.sort()
    n = len(a)

    if n < 2:
        return 0

    aj = a[0]
    ai = a[1]
    current_min = ai - aj

    for i in range(len(a) - 1, 0, -1):
        diff = a[i] - a[i - 1]

        if diff > 0 and diff < current_min:
            current_min = diff
            aj = a[i - 1]
            ai = a[i]

    return current_min

if __name__ == "__main__":
    print find_minimum_loss([1,6,0,4,2])
