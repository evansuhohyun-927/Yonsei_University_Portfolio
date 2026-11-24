# 10주차 — 선형변환과 matrix models

> **이번 주 개념 노트** [6.1 Matrices as transformations](../Ch6_Linear-Transformations/6.1_Matrices-as-transformations.md) · [6.2 Geometry of linear operators](../Ch6_Linear-Transformations/6.2_Geometry-of-linear-operators.md)  
> **MATLAB 노트** [M7](../MATLAB/M7_10주차-MATLAB-Week-7-Matrix-Models.md) · [M7.1](../MATLAB/M7.1_Linear-difference-equation.md) · [M7.2](../MATLAB/M7.2_Population-migration.md) · [M7.3](../MATLAB/M7.3_Leontief-input-output-model.md) · [M7.4](../MATLAB/M7.4_MATLAB-Week7_practice.m.md)

## 이론: Ch6-1 §6.1–6.2 (p. 1–40)

모든 linear transformation T: Rn → Rm은 행렬곱 T(x) = Ax이고, standard matrix의 열은 T(e₁), …, T(eₙ)예요 (Thm 6.1.4).

```math
[T] = \begin{bmatrix} T(e_1) & \cdots & T(e_n) \end{bmatrix}, \qquad R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \qquad H_\theta = \begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}
```

| 개념 | 핵심 |
|---|---|
| Linearity | T(u + v) = T(u) + T(v), T(cu) = cT(u). T(0) ≠ 0이면 linear 아님 |
| Orthogonal matrix (§6.2) | AᵀA = I, A⁻¹ = Aᵀ, 길이·내적 보존 |
| det = 1 / −1 | R²에서 rotation / line에 대한 reflection |
| 표 6.2.1–6.2.3 | contraction·dilation kI, compression·expansion diag(k, 1), shear \[1 k; 0 1\] |

## MATLAB 세션: M7 Matrix models (MATLAB Week 7)

이주 모델은 xₖ₊₁ = Mxₖ를 반복하고, Leontief 모델은 (I − C)x = d를 한 번 풀어요 (Lay §1.10, §2.6 보완).

```math
x_k = M^k x_0, \qquad x = Cx + d \iff (I - C)x = d
```

- M의 열 합이 1이라 총인구 1300이 보존돼요. 보기 검산에 쓸 수 있어요.
- `M^10*x0`와 `M.^10*x0`는 다르고, Leontief는 `(eye(n)-C)\d`가 권장 풀이예요.

---
[← 09주차](09주차_행렬식과-고유값.md) · [주차별 목차](README.md) · [과목 지도](../../README.md) · [11주차 →](11주차_Kernel-range-합성-그래픽스.md)
