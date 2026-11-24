# M6 9주차 (MATLAB Week 6): LU decomposition과 계산량

A = LU로 한 번 분해해 두면 b가 바뀔 때마다 삼각 시스템 두 개로 빠르게 풉니다. 계산량은 n³으로 늘어납니다. <sub>〔W9〕</sub> <sub>〔31:10〕</sub>

| 명령 | 하는 일 | 예 → 결과 | 함정 |
|---|---|---|---|
| `[L,U,P] = lu(A)` | PA = LU, partial pivoting | P는 permutation matrix | 시험 출제 언급(W9 24:45) |
| `[L,U] = lu(A)` | A = LU, 이때 L = PᵀL | L이 삼각이 아닐 수 있음 | 출력 개수에 따라 L의 뜻이 다릅니다. |
| `y = L\(P*b)` | forward substitution | Ly = Pb | P를 빼먹지 않습니다. |
| `x = U\y` | back substitution | Ux = y |   |
| `U\(L\(P*e1))` | 역행렬의 열 하나 | e1 = \[1;0;0\] | A⁻¹ = U⁻¹L⁻¹P |
| `format rat` | 분수 표시 | L, U를 분수로 보기 | `format short`로 복원 |
| Flop | n³ 규모 | n 2배 → 8배 | LU ⅔n³, 이후 b마다 2n², 역행렬 2n³ |

```matlab
A = [2 6 2; -3 -8 0; 4 9 2]; b = [2; 2; 3];
format rat
[L,U,P] = lu(A)
y = L\(P*b);
x = U\y
x = A\b             % 같은 답
format short
```

LU 예시 행렬과 b는 학습용 값입니다. `보완`

<details>
<summary>📎 세션 시간표</summary>

9주차(LearnUs: MATLAB Week 6) · 9주차 강의 비디오.mp4 / 9주차.mp3 / WEEK 9 - MATLAB SESSION.txt

|   |   |
|---|---|
| 00:00 | Ax = b → LUx = b → Ly = b, Ux = y. 삼각 시스템은 대입으로 바로 풀립니다. |
| 04:57 | Example 1: 3×3 분해로 풀기. |
| 06:56 | 정의와 존재 조건: 정방, row interchange 없음. 조건은 invertibility와 직접 같지 않습니다. |
| 08:17 | L, U 구하는 절차. 교수님은 손계산을 줄이고 `lu`로 넘어갑니다. |
| 10:24 | Gaussian elimination과 LU는 같은 연산. 장점은 A⁻¹을 저렴하게 구하는 것입니다. |
| 11:42 | 실제 문제는 10⁴–10⁶ 차원. 알고리즘 선택이 결정적입니다. |
| 13:43 | O(n³): n 2배 → 8배. 10×10이 1분이면 10⁴×10⁴는 10⁹분 ≈ 1,903년. |
| 17:32 | forward phase n³, back substitution n², LU n³, 역행렬 2n³이 가장 비쌉니다. |
| 20:36 | Gauss–Jordan은 b가 필요합니다. LU는 b 없이 저장·재사용합니다. banded이면 훨씬 저렴합니다. |
| 22:16 | `help lu`. sparse matrix 설명, P는 permutation matrix. |
| 24:45 | Partial pivoting: 절댓값 최대 성분을 pivot으로. 시험 출제 언급. |
| 25:21 | `format rat`, `[L,U,P] = lu(A)`, `[L,U] = lu(A)`. |
| 27:41 | `y = L\(P*b)`, `x = U\y`, `c1 = U\(L\(P*[1;0;0]))`. |
| 30:31 | `x = A\b`는 같은 일을 하는 간편 풀이. `format short`로 복원. |

</details>

<details>
<summary>💡 W9 명령 표 설명</summary>

lu의 출력 개수에 따라 L의 의미가 바뀝니다. 계산량 줄은 W9 13:43–20:36 설명을 요약한 것입니다.

</details>

---
[← M5 Matrix tools and linear systems](M5_Matrix-tools-and-linear-systems.md) · [장 목차](README.md) · [과목 지도](../../README.md) · [M7 10주차 (MATLAB Week 7): Matrix Models →](M7_10주차-MATLAB-Week-7-Matrix-Models.md)
