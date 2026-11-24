# Thm 3.3.3 순환 증명, Thm 3.3.8(b) — 증명

> 본문: [3.3 Elementary matrices와 A⁻¹ 구하기](../Ch3-1_Matrices-and-Matrix-Algebra/3.3_Elementary-matrices와-A⁻¹-구하기.md)

**(a)⇒(b)** Eₖ⋯E₁A = Iₙ의 양변 왼쪽에 E들의 역행렬을 곱해 A = E₁⁻¹E₂⁻¹⋯Eₖ⁻¹.

**(b)⇒(c)** Elementary matrix는 가역이고 가역 행렬들의 곱은 가역입니다.

**(c)⇒(a)** R = RREF(A) = Eₖ⋯E₁A는 가역 행렬들의 곱이라 가역입니다. 정사각 RREF는 Iₙ이거나 zero row를 갖는데 zero row가 있으면 가역이 아니므로 R = Iₙ. <sub>〔Ch3-1 p.34〕</sub>

**3.3.8(b)** I = (AB)(AB)⁻¹ = A(B(AB)⁻¹) → (a)에 의해 A 가역. I = (AB)⁻¹(AB) = ((AB)⁻¹A)B → B 가역. <sub>〔Ch3-1 p.43〕</sub>

`보완` (a)는 정사각에서만 성립합니다. 2×3 A와 3×2 B는 AB = I₂여도 BA ≠ I₃일 수 있습니다.

---
[증명과 풀이 목록](README.md) · [과목 지도](../../README.md)
