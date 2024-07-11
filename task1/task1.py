def data_input():
    n, m = map(int, input().split())
    return n, m


def func(n, m):
    arr = list(range(1, n + 1))
    step = m - 1
    start = 1
    if m > n:
        end = 1 + (1 + step - 1) % n
    else:
        end = m
    res = list()

    while arr[end - 1] != 1:
        res.append(arr[start - 1])
        start = arr[end - 1]
        if m > n:
            end = 1 + (end + step - 1) % n
        else:
            if arr[end - 1] + step > n:
                end += (step - n)
            else:
                end += step

    res.append(start)

    return res


def main():
    n, m = data_input()
    print(''.join(map(str, func(n, m))))


if __name__ == "__main__":
    main()
