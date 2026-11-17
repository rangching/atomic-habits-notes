"""EP1 練習題答案：每日固定比例變化的複利。
x_n = (1+r)^n；翻倍天數 n = ln2 / ln(1+r)；航向偏差 d·sinθ。"""
import math
print("Q1 1.01^365                 =", round(1.01**365, 2))
print("Q2 0.99^365                 =", round(0.99**365, 4))
print("Q3 1.001^365 (每天 0.1%)    =", round(1.001**365, 3))
print("Q4 1% 每天，幾天翻倍         =", round(math.log(2)/math.log(1.01), 2), "→ 第", math.ceil(math.log(2)/math.log(1.01)), "天")
print("Q5 0.99^n < 0.5 的最小 n     =", math.ceil(math.log(0.5)/math.log(0.99)))
print("Q6 3940 km × sin3.5° (km)    =", round(3940*math.sin(math.radians(3.5)), 1))
