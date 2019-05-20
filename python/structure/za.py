def swap(a, m, n):
    a[m], a[n] = a[n], a[m]

'''

perm(a, i, j) 是 [i-j] 的所有排列
for k = i->j : 将第i个与第k个交换，交换后找 [i+1,j] 的所有排列，找完之后ik交换回来

'''
def perm(a, i, j):
    if i < j:
        for k in range(i, j+1):
            swap(a, i, k)
            perm(a, i+1, j)
            swap(a, k, i)
    else:
        print(a)



'''
组合 选或者不选
combine(a, n, slted, k ) : 第k步，选中的放在slted中
对于a[k]，要么选择，要么不选择
选：combine(a, n, slted.append(a[k]), k+1 )
不选：combine(a, n, slted, k+1 )

'''
def combine(a, n, slted, k):
    if len(slted) == n:
        print(slted)
        return
    if k > n:
        return
    
    # 选
    slted.append(a[k])
    combine(a, n, slted, k+1)
    
    #不选
    slted.pop()
    combine(a, n, slted, k+1)

def comb(a, n):
    combine(a, n, [], 0)




"""
01背包
wi:vi  初始容量U
v=f[i][u], 0<=u<=U, f[0][U]=0, f[i][0]=0

f[i][u] = max{f[i-1][u], f[i-1][u-wi]+vi}  st. wi<=u

"""
def bag01(stones, U):
    N = len(stones)
    dp = [[0] * (U + 1) for _ in range(N)] # dp[N][U+1]
    for i in range(N):
        w = stones[i][0] # 第i个石头的重量
        v = stones[i][1] # 第i个石头的价值
        for u in range(1, U + 1):
            if u >= w:
                dp[i][u] = max(dp[i-1][u], dp[i-1][u-w]+v) if i > 0 else v
            else:
                dp[i][u] = dp[i-1][u] if i > 0 else 0
    return dp[-1][-1]


"""
完全背包

f[i][u] = max{ f[i-1][u-k*wi] + k*vi }, st. 0 <= k*wi <= u

"""
def bag_full(stones, U):
    N = len(stones)
    dp = [[0] * (U + 1) for _ in range(N)] # dp[N][U+1]
    for i in range(N):
        w = stones[i][0] # 第i个石头的重量
        v = stones[i][1] # 第i个石头的价值
        for u in range(1, U+1):
            k = 0
            while k * w <= u:
                dp[i][u] = max(dp[i][u], dp[i-1][u-k*w]+k*v if i > 0 else k*v)
                k += 1
    return dp[-1][-1]




"""
最少硬币

dp[u] = min{ dp[u - vi] + 1 }, dp[0]=0,  vi<=u<=U

"""
MX = float('inf')

def min_coins(A, U):
    dp = [0] + [MX] * U
    for u in range(1, U + 1):
        mi = MX
        for a in A:
            if u >= a:
                mi = min(mi, dp[u - a] + 1)
        dp[u] = mi
    print(dp)




"""
八皇后

"""
N = 8
A = [a for a in range(1, N + 1)] # 数字1~N 代表皇后
def queen(rst, i):
    if i == N:
        print(rst)
        return

    for a in A:
        rst[i] = a

        ok = True
        for j in range(i):
            if rst[j] == rst[i] or i - j == abs(rst[i] - rst[j]):
                ok = False
                break

        if ok:
            queen(rst, i + 1)


"""
1~n 中1的个数

"""


def get_high(n):
    t = 1
    while n > 10:
        t *= 10
        n //= 10
    return n * t


def count_high(n):
    digits = [int(d) for d in list(str(n))]
    N = len(digits)
    if N < 2:
        return 0

    # 第一位
    cnt = 0
    first = digits[0]
    if first == 1:
        hi = get_high(n)
        cnt += n - hi + 1
    else:
        cnt += 10 ** (N - 1)

    # 第二位及以后
    cnt += first * (N - 1) * 10 ** (N - 2)

    return cnt


def count1(n):
    if n == 0:
        return 0
    elif n < 10:
        return 1
    n1 = get_high(n)
    n2 = n - n1

    c1 = count_high(n)
    c2 = count1(n2)
    return c1 + c2





"""
str2float()

"""

def is_blank(c):
    return c in ' \t\n\r'

def char2digit(c):
    d = ord(c) - ord('0')
    if d < 0 or d > 9:
        raise ValueError(c)
    return d

def str2float(s):

    h, t = 0, len(s) - 1
    while is_blank(s[h]):
        h += 1
    while is_blank(s[t]):
        t -= 1

    i = h

    # sign
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1

    # 整数部分
    r1 = 0
    while i <= t and s[i] not in '.eE':
        d = char2digit(s[i])
        r1 = 10 * r1 + d
        i += 1
    if i == t + 1:
        return sign * r1

    # 小数部分
    r2 = 0
    dot = 0.1
    if s[i] == '.':
        i += 1
        while i <= t and s[i] not in 'eE':
            r2 += char2digit(s[i]) * dot
            dot *= 0.1
            i += 1
    if i == t + 1:
        return sign * (r1 + r2)

    # 指数部分
    exp = 0
    if s[i] in 'eE':
        i += 1
        exp_sign = 1
        if s[i] == '+':
            i += 1
        if s[i] == '-':
            exp_sign = -1
            i += 1
        while i <= t:
            d = char2digit(s[i])
            exp = 10 * exp + d
            i += 1
        exp = 10 ** (exp_sign * exp)

    if i == t + 1:
        return sign * (r1 + r2) * exp
    else:
        raise ValueError()





if __name__ == '__main__':
    a = [1,2,3]
    perm(a, 0, 2)
