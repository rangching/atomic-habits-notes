"""EP2 練習題答案：把每次行動當成一張「身分選票」。
信念模型：Beta(α, β) 先驗；做了 k 次、共 n 天 → 後驗平均 (α+k)/(α+β+n)。
過半門檻與「不需要全勝」用二項分布計算。"""
import math

def post(a, b, k, n):
    return (a + k) / (a + b + n)

print("Q1 先驗 Beta(1,4)，30 天跑了 20 天，後驗平均 =", round(post(1, 4, 20, 30), 3))
print("Q2 30 天要過半，至少幾票 =", 30 // 2 + 1)
p, n = 0.6, 30
tail = sum(math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(16, n+1))
print("Q3 每天 60% 機率做到，30 天中 ≥16 天的機率 =", round(tail, 3))
k = 0
while post(2, 18, k, k) < 0.5:
    k += 1
print("Q4 先驗 Beta(2,18)（約 10%），連續做幾天後驗 ≥ 0.5 =", k)
print("Q5 每週一、四各一篇，3 年共幾篇 =", 2 * 52 * 3)
