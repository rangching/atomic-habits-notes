"""EP10 練習題答案：天賦與動機。
體重比較；Falconer 遺傳度 h² = 2(r_MZ − r_DZ)；
成功機率 P = Φ((s−d)/σ)（能力 s、難度 d、表現波動 σ）；探索時間預算。"""
from statistics import NormalDist
N = NormalDist()
print("Q1 Phelps 194 lb 比 El Guerrouj 138 lb 重 =", round((194 / 138 - 1) * 100, 1), "%")
print("Q2 Falconer h² = 2(0.46−0.23) =", round(2 * (0.46 - 0.23), 2))
s, sig = 100, 10
print("Q3 難度 104（超出能力 4%）成功機率 =", round(N.cdf((s - 104) / sig), 4))
print("   難度 100 成功機率 =", N.cdf(0))
z = N.inv_cdf(0.85)
print("Q4 成功率 85% 的難度 d = s − σ·z =", round(s - sig * z, 2), "（z =", round(z, 4), "）")
print("   Wilson 等 2019 最佳錯誤率 Φ(−1) =", round(N.cdf(-1) * 100, 2), "%")
print("Q5 每週 40 小時、20% 探索、50 週 =", 40 * 0.2 * 50, "小時")
