"""EP11 練習題答案：好習慣的盲點與長久之道。
CBE =（得分+籃板+助攻+抄截+無名英雄−失誤）/上場分鐘 ×1000；
自動駕駛退化 (1−δ)^n；效果量 d 換成百分位 Φ(d)；解釋變異量 R² → r = √R²；
四大法則串聯：習慣發生機率 = p1·p2·p3·p4，找出瓶頸。"""
from statistics import NormalDist
import math
cbe = (11 + 8 + 12 + 2 + 1 - 5) / 33
print("Q1 Magic 的 CBE =", round(cbe * 1000, 1), "→ 提升 1% 目標", round(cbe * 1000 * 1.01, 1))
print("Q2 每週退化 0.2%，52 週後剩 =", round(0.998**52, 4))
print("Q3 d=0.67 的百分位 Φ(0.67) =", round(NormalDist().cdf(0.67), 4))
print("Q4 音樂 R²=21% → r =", round(math.sqrt(0.21), 3), "；專業 R²<1% → r <", round(math.sqrt(0.01), 2))
p = [0.9, 0.8, 0.5, 0.9]
P0 = math.prod(p)
p2 = [0.9, 0.8, 0.7, 0.9]
p3 = [0.95, 0.8, 0.5, 0.9]
print("Q5 四環節串聯 =", round(P0, 3), "→ 瓶頸 0.5→0.7 =", round(math.prod(p2), 3), "；改善非瓶頸 0.9→0.95 =", round(math.prod(p3), 3))
