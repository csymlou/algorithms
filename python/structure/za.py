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



if __name__ == '__main__':
    a = [1,2,3]
    perm(a, 0, 2)
