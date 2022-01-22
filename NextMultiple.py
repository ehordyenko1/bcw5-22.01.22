if __name__ == '__main__':

    dividend = int(input())
    divisor = int(input())

    if divisor < 0:
        divisor *= -1

    multiple = dividend - dividend % divisor

    if multiple < dividend:
        multiple += divisor

    print(multiple)
