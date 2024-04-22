def fib_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_sequence(n-1) + fib_sequence(n-2)


def main():
    print(fib_sequence(4))


if __name__ == "__main__":
    main()
