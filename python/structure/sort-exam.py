# 快排
def partition(A, p, r): # 分区
    x = A[r] # 最后一个为基准，分开小于和大于这个元素的界限
    i = p - 1
    for j in range(p, r):
        if A[j] <= x: # 正序和倒序在这里可以控制
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


# 堆排序
# 堆排序
def heap_sort(A):
    N = len(A)
    build_max_heap(A) # 建大堆
    for i in range(N - 1, -1, -1):
        A[0], A[-1] = A[-1], A[0]  # 头最大，放末尾；首尾交换
        print(A.pop()) # 末尾是最大值
        max_heapify(A, 0) # 位置0被破坏，重新整理


# 建堆
def build_max_heap(A):
    N = len(A)
    for i in range(N // 2, -1, -1):  # 从中间到位置0，每个点往下整理堆
        max_heapify(A, i)


# 从坐标i开始向下整理堆
def max_heapify(A, i):
    N = len(A)
    l = left(i)
    r = right(i)
    m = i
    if l < N and A[l] > A[i]:
        m = l
    if r < N and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        max_heapify(A, m)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


if __name__ == '__main__':
    a = [4, 3, 5, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    print(a)
