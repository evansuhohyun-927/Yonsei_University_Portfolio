# A = QR 구성과 Thm 7.10.2 — 증명

> 본문: [7.10 QR-decomposition](../Ch7_Dimension-and-Structure/7.10_QR-decomposition.md)

**QR** Gram–Schmidt에서 w<sub>j</sub> ∈ span{q₁, …, q<sub>j</sub>}이므로 w<sub>j</sub> = Σ<sub>i≤j</sub>(w<sub>j</sub>·qᵢ)qᵢ. 이것을 열로 모으면 A = QR이고, rᵢᵢ = ‖vᵢ‖ > 0이라 R은 invertible입니다. <sub>〔Ch7-2 p.21–25〕</sub>

**7.10.2** AᵀAx = Aᵀb에 A = QR을 넣으면 RᵀQᵀQRx = RᵀQᵀb, QᵀQ = I이므로 RᵀRx = RᵀQᵀb. Rᵀ가 invertible이라 Rx = Qᵀb. <sub>〔Ch7-2 p.28–29〕</sub>

**검산** 7.10 Ex 2에서 AᵀA = \[4 8 10; 8 20 26; 10 26 38\], Aᵀb = (2, 0, −6)으로 풀어도 x̂ = (1/2, 5/2, −2). Ax̂ = (−2, 3, −1, 2) = b라 이 예제의 b는 col(A) 안에 있고 오차가 0입니다. 즉 least squares 해가 정확한 해와 같습니다. 오차가 있는 예는 위 계산기의 7.7 Ex 6 프리셋을 보세요. `보완`

---
[증명과 풀이 목록](README.md) · [과목 지도](../../README.md)
