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




if __name__ == '__main__':
    a = [1,2,3]
    perm(a, 0, 2)
