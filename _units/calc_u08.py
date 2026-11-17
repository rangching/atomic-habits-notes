"""EP8 練習題答案：準雙曲折現 U0 = u0 + β Σ δ^t u_t（取 δ=1）、承諾裝置的最低罰金、時間帳、雨果寫作天數。"""
from datetime import date
beta = 0.6
cost, benefit = 4, 6          # 今天付出 4，明天得到 6
plan = beta*(-cost) + beta*benefit   # 昨天看「今天做」：兩者都在未來
now = -cost + beta*benefit           # 今天當下：成本立即、好處在未來
print("Q1 前一天規劃時的淨值 β(-4)+β·6        =", round(plan, 3))
print("Q2 當天當下的淨值 -4+β·6               =", round(now, 3))
print("Q3 罰金明天才扣，最低罰金 P ≥ 0.4/β     =", round(-now/beta, 3))
print("Q4 每天 2 小時 × 365 天（小時）         =", 2*365)
print("Q5 1830-09-01 到 1831-01-15 天數        =", (date(1831,1,15)-date(1830,9,1)).days)
