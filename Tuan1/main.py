from math import *


def cau1():
    a, b = map(int, input().split())

    max_num = (a + b + abs(a - b)) // 2
    min_num = (a + b - abs(a - b)) // 2

    print("max =", max_num)
    print("min =", min_num)
    return max_num, min_num


def cau2():
    a, b, c = map(float, input().split())
    x = a ** 5 - 2 * sqrt(abs(b)) + a * b * c
    print('{:0.2f}'.format(x))


def cau4():
    s = input()
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            cnt += 1
    if cnt % 2 == 0:
        print("Win")
    else:
        print("Lose")


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def cau7():
    x = int(input())
    if 1 <= x <= 30:
        result = fibonacci(x)
        print(result)
    else:
        print(f"So {x} khong nam trong khoang [1,30].")


def cau3():
    n = int(input())
    sum_divisors = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i == (n // i):
                sum_divisors += i
            else:
                sum_divisors += (i + n // i)
        i += 1
    if n > 1:
        sum_divisors += 1
    print(sum_divisors)


def cau18():
    n = int(input())
    kq = n
    for i in range(1, n):
        kq *= i
    if n < 0:
        print()
    elif n == 0:
        print(1)
    else:
        print(kq)


def cau11():
    n = int(input())
    if n % 2 == 0:
        print(0)
    else:
        print(1)


def cau13():
    matrix = []
    for _ in range(5):
        row = list(map(int, input().split()))
        matrix.append(row)

    row_1, col_1 = None, None

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                row_1, col_1 = i, j
                break

    steps = abs(2 - row_1) + abs(2 - col_1)

    print(steps)


def cau14():
    s = str(input())
    vowels = "AEIOUYaeiouy"
    s_process = ""
    for char in s:
        if char.isupper():
            char = char.lower()
        if char in vowels:
            continue
        elif char.isalpha():
            s_process += "." + char
        else:
            s_process += char
    print(s_process)


def cau16():
    N = int(input())
    Sum = 0
    for _ in range(N):
        command, amount = input().split()
        amount = int(amount)

        if command == 'D':
            Sum += amount
        elif command == 'W':
            Sum -= amount

    print(Sum)


def cau5():
    S = input()
    temp = str(S.count('4') + S.count('7'))
    dem = temp.count('4') + temp.count('7')
    if dem == len(temp):
        print('YES')
    else:
        print('NO')


def cau9():
    a = float(input())
    b = float(input())
    c = float(input())

    if a == 0:
        print("a phai khac 0")
    else:
        delta = b ** 2 - 4 * a * c

        if delta > 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            if x1 % 1 == 0: x1 = int(x1)
            if x2 % 1 == 0: x2 = int(x2)
            print(f"PT co hai nghiem phan biet:\n\nx1 = {x1}\nx2 = {x2}")
        elif delta == 0:
            x = -b / (2 * a)
            if x % 1 == 0: x = int(x)
            print(f"PT co nghiem kep: x1 = x2 = {x}")
        else:
            print("PTVN")


def cau6():
    n, m, h, w = map(int, input().split())

    def dem_sl_gap(N, M, H, W):
        dem = 0
        while N > H or M > W:
            if N > H:
                H *= 2
                dem += 1
            elif M > W:
                W *= 2
                dem += 1
        return dem

    print(min(dem_sl_gap(n, m, h, w), dem_sl_gap(m, n, h, w)))


def cau18():
    n, k = map(int, input().split())
    s = input()
    char = ""
    for j in range(k):
        char += chr(65 + j)
    c = [s.count(i) for i in char]
    print(k * min(c))


def cau12():
    n = int(input())
    s = ""
    for i in range(1, 1000 + 1):
        s += str(i)
    print(s[n - 1])
    # print(s)


def cau15():
    n, m = map(int, input().split())
    length = len(str(n))
    dem = m // 10 ** length
    if m % 10 ** length >= n:
        dem += 1
    print(dem)


def cau8():
    k, t = map(int, input().split())
    if (t // k) % 2 == 0:
        print(t % k)
    else:
        print(k - t % k)


def cau10():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    i = 0
    while i < n and arr[i] > i:
        i += 1
    print(i)


def main():
    # cau1()
    # cau4()
    # cau7()
    # cau2()
    # cau3()
    # cau18()
    # cau11()
    # cau13()
    # cau14()
    # cau16()
    # cau5()
    # cau9()
    # cau6()
    # cau18()
    # cau12()
    # cau15()
    # cau8()
    cau10()


if __name__ == "__main__":
    main()
