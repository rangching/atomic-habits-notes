"""EP7 練習題答案：Lally 自動化曲線 A(t)=a-b*exp(-c t)（設 b=a，從 0 開始）、摩擦玩具模型、稅務信函。"""
import math
c = 0.045
t95 = math.log(20)/c
print("Q1 c=0.045，到達 95% 平台的天數        =", round(t95, 2), "→ 第", math.ceil(t95), "天")
print("Q2 95% 天數=18 天時 c                  =", round(math.log(20)/18, 4))
print("Q3 改成隔天做一次（以次數計），約幾天   =", round(2*t95, 1))
print("Q4 19.2%→23.4% 相對提升 (%)            =", round((23.4-19.2)/19.2*100, 2))
print("Q5 每步完成率 0.8，5 步減到 2 步，倍數  =", round(0.8**2/0.8**5, 3))
