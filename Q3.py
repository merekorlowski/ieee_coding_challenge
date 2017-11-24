def find_number_of_repeats(a, b):

    count = 0

    while b not in a and len(a) < len(b) * 2:
        a += a
        count += 1

        if b in a:
            return count + 1

    return -1

if __name__ == "__main__":
    print str(find_number_of_repeats("abcd", "edabcdab"))
