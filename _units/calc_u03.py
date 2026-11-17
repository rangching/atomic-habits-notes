"""EP3 練習題答案：桑代克 12 號貓的逃脫時間，以及 Rescorla–Wagner 式的獎賞預測更新
V_{t+1} = V_t + α (r - V_t)  →  V_n = r (1 - (1-α)^n)（V_0 = 0）。"""
import math
cat12 = [160, 30, 90, 60, 15, 28, 20, 30, 22, 11, 15, 20, 12, 10, 14, 10, 8, 8, 5, 10, 8, 6, 6, 7]
first3 = sum(cat12[:3]) / 3
last3 = sum(cat12[-3:]) / 3
print("試驗次數 =", len(cat12))
print("Q1 前三次平均（秒）=", round(first3, 1))
print("Q2 後三次平均（秒）=", round(last3, 2))
print("Q3 前三次 ÷ 後三次 =", round(first3 / last3, 1))
a = 0.3
print("Q4 α=0.3、r=1，第 5 次後 V5 =", round(1 - (1 - a)**5, 3))
n = math.ceil(math.log(0.05) / math.log(1 - a))
print("Q5 V_n ≥ 0.95 的最小 n =", n, "（ln0.05/ln0.7 =", round(math.log(0.05)/math.log(1-a), 2), "）")
