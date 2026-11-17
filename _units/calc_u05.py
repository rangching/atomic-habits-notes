"""EP5 練習題答案：環境與自制力。
選擇架構的 softmax 模型 P(水)=e^{s}/(e^{s}+1)、重複抵抗誘惑的機率、效果量 d 的「優勢機率」Φ(d/√2)。"""
import math
print("Q1 原本每季賣 1000 瓶水，增加 25.8% 後 =", round(1000 * 1.258))
print("Q2 效用相同，水的顯著度 s 從 0 提到 1：P(水) =", round(math.exp(1) / (math.exp(1) + 1), 3))
print("Q3 每次抵抗成功率 0.9，一天 5 次誘惑全守住 =", round(0.9**5, 3))
print("Q4 一週 35 次誘惑全守住 =", round(0.9**35, 3), "；只剩 7 次 =", round(0.9**7, 3))
print("Q5 一週預期失守次數：35 次誘惑 =", round(35 * 0.1, 2), "；7 次 =", round(7 * 0.1, 2))
Phi = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
print("Q6 d=0.45 的優勢機率 Φ(d/√2) =", round(Phi(0.45 / math.sqrt(2)), 3))
