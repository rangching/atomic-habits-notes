"""EP6 練習題答案：獎勵預測誤差（Rescorla–Wagner 式學習）。
delta = r - r_hat；r_hat <- r_hat + alpha*delta。"""
import math
a = 0.3
rh = 0.0
for t in range(5):
    rh += a*(1 - rh)
print("Q1 r_hat 第 5 次後（α=0.3，每次 r=1）   =", round(rh, 3))
print("Q2 第 6 次預測誤差 δ=1-r_hat            =", round(1 - rh, 3))
rh6 = rh + a*(0 - rh)
print("Q3 第 6 次獎勵落空後 r_hat              =", round(rh6, 3), "（δ =", round(-rh, 3), "）")
n = math.log(0.05)/math.log(1 - a)
print("Q4 r_hat≥0.95 需要幾次                  =", round(n, 2), "→", math.ceil(n), "次")
print("Q5 對照組每週 0.9 次，+51% 後          =", round(0.9*1.51, 3))
