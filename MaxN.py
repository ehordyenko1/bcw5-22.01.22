if __name__ == '__main__':
    counter = int(input())
    array = []
    i = 0

    while i < counter:
        current = int(input())
        array.append(current)
        i += 1

    print(f'Max number in array : {max(array)}')