import numpy as np


def cau1():
    n = int(input())
    A = np.array([input().strip().split() for _ in range(n)], dtype=int)
    if np.linalg.matrix_rank(A) == n:
        print("YES")
    else:
        print("NO")


def cau2():
    n = int(input())
    A = np.array([input().strip().split() for _ in range(n)], dtype=int)
    B = np.eye(n)
    if np.array_equal(A, B.astype(int)) or np.array_equal(A, np.rot90(B, k=1).astype(int)):
        print("YES")
    else:
        print("NO")


def cau3():
    r, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r)]

    # Find the maximum length of numbers in each column
    widths = [max(len(str(A[i][j])) for i in range(r)) for j in range(c)]

    for i in range(r):
        # Join the numbers with spaces and print the resulting string
        print(' '.join(f"{A[i][j]:>{widths[j]}}" for j in range(c)))


def cau4():
    n = int(input())
    A = np.array([input().strip().split() for _ in range(n)], dtype=int)
    B = np.array([input().strip().split() for _ in range(n)], dtype=int)
    flag = 0
    for i in range(1, 5):
        if np.array_equal(B, np.rot90(A, k=i).astype(int)):
            flag = 1
            break

    if flag == 1:
        print("YES")
    else:
        print("NO")


def cau6():
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    if n * m == r * c:
        arr = np.reshape(arr, (r, c)).tolist()

    print(str(arr).replace('], [', '\n').replace('[', '').replace(',', '').replace(']', ''))


def cau5():
    h, w = map(int, input().split())
    A = np.array([input().strip().split() for _ in range(h)], dtype=int)
    top, left, bottom, right = map(int, input().split())
    for j in range(h):
        for i in range(w):
            if i < left or i > right or j < top or j > bottom:
                A[j, i] = 0

    for row in A:
        print(*row)


def cau7():
    n = int(input())
    a = list(map(int, input().split()))

    max_sum = -1e10
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(n):
        current_sum += a[i]

        if max_sum < current_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    print(start + 1, end + 1, max_sum)


def main():
    cau7()


if __name__ == "__main__":
    main()
