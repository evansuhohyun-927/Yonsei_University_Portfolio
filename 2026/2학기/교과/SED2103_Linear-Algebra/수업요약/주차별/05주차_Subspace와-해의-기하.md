# 5주차 — Subspace와 해의 기하

> **이번 주 개념 노트** [3.4 Subspaces와 linear independence](../Ch3-2_Subspaces-Geometry-LU/3.4_Subspaces와-linear-independence.md) · [3.5 Geometry of linear systems](../Ch3-2_Subspaces-Geometry-LU/3.5_Geometry-of-linear-systems.md)  
> **MATLAB 노트** [M5](../MATLAB/M5_Matrix-tools-and-linear-systems.md)

## 이론: Ch3-2 §3.4–3.5 (p. 1–35)

Subspace는 덧셈과 스칼라배에 닫힌 집합이라 항상 0을 포함해요. Ax = 0의 해집합은 subspace이고, Ax = b의 해는 그것을 평행이동한 것이에요.

```math
x = x_0 + x_h, \qquad x_0:\ Ax_0 = b \text{ (particular)}, \qquad x_h \in \{x : Ax = 0\}
```

| 개념 | 핵심 |
|---|---|
| Span (Thm 3.4.2) | 항상 subspace. R³의 subspace는 {0}, 원점 직선, 원점 평면, R³ |
| Independence (Def 3.4.5) | c₁v₁ + ⋯ + cₛvₛ = 0의 해가 trivial뿐 |
| Thm 3.4.6 | dependent ⇔ 한 벡터가 나머지의 결합 |
| Thm 3.4.8 | Rn에서 n개보다 많은 벡터는 dependent |
| Thm 3.5.5 | Ax = b consistent ⇔ b ∈ column space |
| Thm 3.5.6 | Ax = 0의 해는 A의 모든 행과 직교 |

반례: 제1사분면은 덧셈에는 닫혀 있지만 (−1)배에 닫히지 않아 subspace가 아니에요 (p.5).

## MATLAB 세션: M5 Matrix tools and linear systems (5주차)

Ax = b를 세 방법으로 풀어요: `inv(A)*b`, `A\b`, `rref([A b])`. det = 0이면 해가 없는지 무한한지는 rref의 마지막 행으로 판단해요.

| 명령 | 동작 | 함정 |
|---|---|---|
| `diag(A)` / `diag(v)` | 대각 추출 / 대각행렬 생성 | 입력이 행렬이냐 벡터냐로 달라져요 |
| `eye(n)` | 단위행렬 | 3×4 M에서 M\*eye(4) = eye(3)\*M |
| `det([1 2; 2 4])` | 0 | "유일해 없음"만 알려줘요 |
| `[2 1; 1 -3]\[5; -1]` | \[2; 1\] | b는 열벡터, `b/A`와 방향 반대 |
| `rref([A eye(3)])` | \[I \| A⁻¹\] | 옆으로 붙이기는 공백, 아래로는 `;` |

---
[← 03-04주차](03-04주차_행렬-연산과-역행렬.md) · [주차별 목차](README.md) · [과목 지도](../../README.md) · [06-07주차 →](06-07주차_특수-행렬-LU-분할-행렬.md)
