# 증명: Leontief Theorem — 풀이

> 본문: [M7.3 Leontief input-output model](../MATLAB/M7.3_Leontief-input-output-model.md)

슬라이드는 증명을 생략합니다(강의: 증명할 필요는 없다). <sub>〔W10 18:00〕</sub> `보완`

1. 열 합의 최댓값을 s &lt; 1이라 둡니다. 음수 없는 행렬에서 이 값은 1-norm ‖C‖₁이고 ‖Cᵐ‖₁ ≤ sᵐ → 0입니다.
2. (I − C)(I + C + ⋯ + Cᵐ) = I − Cᵐ⁺¹ → I. 따라서 급수 S = ΣCᵏ가 수렴하고 (I − C)S = I, 즉 S = (I − C)⁻¹입니다.
3. C ≥ 0이면 모든 Cᵏ ≥ 0이므로 S ≥ 0이고, d ≥ 0이면 x = Sd ≥ 0입니다.
4. 역행렬이 있으므로 (I − C)x = d의 해는 하나뿐입니다.

---
[증명과 풀이 목록](README.md) · [과목 지도](../../README.md)
