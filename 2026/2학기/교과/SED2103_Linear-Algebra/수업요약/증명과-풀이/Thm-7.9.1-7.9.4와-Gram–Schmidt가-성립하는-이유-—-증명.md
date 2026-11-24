# Thm 7.9.1, 7.9.4와 Gram–Schmidt가 성립하는 이유 — 증명

> 본문: [7.9 Orthonormal bases and the Gram–Schmidt process](../Ch7_Dimension-and-Structure/7.9_Orthonormal-bases-and-the-Gram–Schmidt-process.md)

**7.9.1** c₁v₁ + ⋯ + c<sub>k</sub>v<sub>k</sub> = 0에 vᵢ를 내적하면 다른 항은 0이라 cᵢ‖vᵢ‖² = 0, vᵢ ≠ 0이므로 cᵢ = 0. `보완`

**7.9.4** w = Σ c<sub>j</sub>v<sub>j</sub>에 vᵢ를 내적하면 w·vᵢ = cᵢ‖vᵢ‖². `보완`

**Gram–Schmidt** v<sub>j</sub> = w<sub>j</sub> − proj<sub>span{v₁,…,v<sub>j−1</sub>}</sub>w<sub>j</sub>는 [Thm 7.7.4](../Ch7_Dimension-and-Structure/7.7_The-projection-theorem.md#thm-774)의 W⊥ 성분이라 앞 vᵢ와 직교합니다. w<sub>j</sub>가 앞 벡터와 independent이므로 v<sub>j</sub> ≠ 0이고, span{v₁, …, v<sub>j</sub>} = span{w₁, …, w<sub>j</sub>}. `보완`

---
[증명과 풀이 목록](README.md) · [과목 지도](../../README.md)
