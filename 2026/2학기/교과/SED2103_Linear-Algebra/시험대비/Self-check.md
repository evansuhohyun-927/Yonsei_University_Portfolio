# Self-check

개념 확인용 자가 점검 문항입니다(직접 만든 문항). 장별로 끝까지 풀어 본 뒤 틀린 문항의 개념 노트로 돌아가세요.

**목차** [Ch1 Vectors](#ch1-vectors) (6) · [Ch2 Systems of Linear Equations](#ch2-systems-of-linear-equations) (11) · [Ch3-1 Matrices and Matrix Algebra (1)](#ch3-1-matrices-and-matrix-algebra-1) (21) · [Ch3-2 Subspaces, Geometry, Special Matrices, LU](#ch3-2-subspaces-geometry-special-matrices-lu) (24) · [Ch4 Determinants and Eigenvalues](#ch4-determinants-and-eigenvalues) (11) · [Ch6 Linear Transformations](#ch6-linear-transformations) (21) · [Ch7 Dimension and Structure](#ch7-dimension-and-structure) (17) · [W10 Matrix Models](#w10-matrix-models) (21)

## Ch1 Vectors

> 개념 노트: [Ch1 Vectors 목차](../수업요약/Ch1_Vectors/README.md)

**1.** speed 20 m/s와 "동쪽으로 20 m/s" 중 vector는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**동쪽으로 20 m/s**

방향이 있어야 vector입니다.

</details>

**2.** A = (2,−1), B = (−3,4)일 때 AB는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**(−5, 5)**

끝점 − 시작점입니다.

</details>

**3.** v = (3,4)의 norm은? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**5**

√(9 + 16).

</details>

**4.** u = (1,2), v = (3,−1)의 u·v는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**1**

3 − 2. 결과는 scalar입니다.

</details>

**5.** orthonormal의 두 조건은? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**서로 orthogonal, 각 norm 1**

Def 1.2.10.

</details>

**6.** 점 (1,0,0), normal (2,1,−1)인 평면은? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**2x + y − z = 2**

n·(x − x₀) = 0.

</details>

## Ch2 Systems of Linear Equations

> 개념 노트: [Ch2 Systems of Linear Equations 목차](../수업요약/Ch2_Systems-of-Linear-Equations/README.md)

**7.** x² + y = 1은 linear equation인가? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**아님**

x가 2차입니다.

</details>

**8.** RREF에 \[0 0 0 | 5\] 행이 있으면? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**해 없음**

0 = 5입니다.

</details>

**9.** Homogeneous system에서 n = 7, r = 4이면 free variable 수는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**3**

n − r.

</details>

**10.** Gaussian과 Gauss–Jordan의 차이는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**REF + back substitution vs RREF까지**

</details>

**11.** 행에 0을 곱하면 안 되는 이유는? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**되돌릴 수 없고 식 하나의 정보가 사라짐**

</details>

**12.** 서로 다른 x값 4개를 지나는 다항식의 계수는 몇 개? <sub>〔SED 1–2〕</sub>

<details>
<summary>정답 보기</summary>

**4개**

차수 ≤ 3, a₀–a₃.

</details>

**13.** Underdetermined system이 consistent일 때 해의 개수는? <sub>〔SED Midterm〕 · 연결: Ch3-1 Matrices and Matrix Algebra (1)</sub>

<details>
<summary>정답 보기</summary>

**무한**

free variable이 반드시 생깁니다 (Q2).

</details>

**14.** Overdetermined system이 가질 수 있는 해의 개수는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**0, 1, ∞ 모두 가능**

Q3.

</details>

**15.** Partial pivoting은 무엇을 하나? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**|pivot|이 가장 큰 아래 행과 교환해 multiplier를 작게 유지**

Q4.

</details>

**16.** n + 1개 점을 지나는 n차 다항식이 유일한 이유는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**Vandermonde 계수행렬이 가역 (서로 다른 x값)**

</details>

**17.** sin α, cos β, tan γ 시스템이 18개의 해를 가져도 모순이 아닌 이유는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**α, β, γ에 대해 비선형**

치환한 u, v, w에서는 해가 1개입니다 (Q10).

</details>

## Ch3-1 Matrices and Matrix Algebra (1)

> 개념 노트: [Ch3-1 Matrices and Matrix Algebra (1) 목차](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/README.md)

**18.** A가 2×3, B가 3×4일 때 AB와 BA는? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**AB는 2×4, BA는 정의 안 됨**

BA는 안쪽 (4, 2)가 다릅니다.

</details>

**19.** Ax를 column 관점으로 쓰면? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**x₁a₁ + x₂a₂ + ⋯ + xₙaₙ**

예: \[1 −3 2; 4 0 5\](3,1,2) = (4,22).

</details>

**20.** AB의 i번째 행은 무엇의 결합인가? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**B의 row들의 결합, 계수는 A의 i행**

[Thm 3.1.8](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.1_Operations-on-matrices.md#thm-318)(b).

</details>

**21.** (AB)⁻¹와 (AB)ᵀ는? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**B⁻¹A⁻¹, BᵀAᵀ**

둘 다 역순입니다.

</details>

**22.** \[a b; c d\]의 가역 조건과 역행렬은? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**ad − bc ≠ 0, (1/(ad−bc))\[d −b; −c a\]**

[Thm 3.2.7](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.2_Inverses와-대수-성질.md#thm-327).

</details>

**23.** "r₃에 4·r₁을 더함"의 E와 E⁻¹은? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**E = \[1 0 0; 0 1 0; 4 0 1\], E⁻¹ = \[1 0 0; 0 1 0; −4 0 1\]**

[Thm 3.3.2](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.3_Elementary-matrices와-A⁻¹-구하기.md#thm-332): 역연산.

</details>

**24.** \[A | I\]를 줄이다 왼쪽에 zero row가 생기면? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**A는 singular, 계산 중단**

Slide 39 Example 4.

</details>

**25.** Ax = 0이 trivial solution만 가질 조건은? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**A가 가역일 때, 그리고 그때만**

[Thm 3.3.6](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.3_Elementary-matrices와-A⁻¹-구하기.md#thm-336).

</details>

**26.** A가 가역이면 Ax = b의 해는? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**모든 b에 대해 유일해 x = A⁻¹b**

[Thm 3.3.5](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.3_Elementary-matrices와-A⁻¹-구하기.md#thm-335).

</details>

**27.** Ax = b는 왜 적어도 하나의 b에 대해서는 항상 consistent인가? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**b = 0이면 x = 0이 해**

Slide 45.

</details>

**28.** AX = C에서 X = CA⁻¹로 쓰면 안 되는 이유는? <sub>〔SED 3-1〕</sub>

<details>
<summary>정답 보기</summary>

**왼쪽에 A⁻¹를 곱해야 하므로 X = A⁻¹C**

곱셈 교환법칙이 없습니다.

</details>

**29.** A가 2×3, B가 3×4일 때 (AB)₂₁은? (Example 5) <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**8**

2·4 + 6·0 + 0·2.

</details>

**30.** \[k 2; 3 6\]이 singular가 되는 k? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**k = 1**

6k − 6 = 0.

</details>

**31.** (2A)⁻¹을 A⁻¹로 표현하면? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**½A⁻¹**

(kA)⁻¹ = k⁻¹A⁻¹.

</details>

**32.** I₃의 1행과 3행을 바꾼 E로 EA를 계산하면? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**A의 1행과 3행이 바뀜**

AE로 쓰면 column이 바뀝니다.

</details>

**33.** Example 5의 해 x? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**(1, −1, 2)**

x = A⁻¹b = \[−40 16 9; 13 −5 −3; 5 −2 −1\](5,3,17).

</details>

**34.** n×n A에서 Ax = 0이 nontrivial 해를 가지면 Ax = b는? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**어떤 b에서는 해가 없음**

A가 비가역이므로 "모든 b에서 consistent"가 거짓입니다.

</details>

**35.** Example 8에서 b = (1,2,3), (1,1,1)은 consistent? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**(1,2,3)은 consistent, (1,1,1)은 inconsistent**

조건 b₃ = b₁ + b₂.

</details>

**36.** 정사각 A, B에서 AB = I를 확인했다. BA = I도 따로 확인해야 하나? <sub>〔Ch3-1 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**필요 없음**

[Thm 3.3.8](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.3_Elementary-matrices와-A⁻¹-구하기.md#thm-338). 정사각이 아니면 성립하지 않습니다.

</details>

**37.** Adjacency matrix A에서 (A³)ᵢⱼ의 의미는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**i에서 j로 정확히 3번 이동하는 경로 수**

Q16.

</details>

**38.** Hilbert matrix의 수치 역행렬이 부정확한 이유는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**거의 singular라 역행렬 성분이 커서 오차를 증폭**

Q20.

</details>

## Ch3-2 Subspaces, Geometry, Special Matrices, LU

> 개념 노트: [Ch3-2 Subspaces, Geometry, Special Matrices, LU 목차](../수업요약/Ch3-2_Subspaces-Geometry-LU/README.md)

**39.** R³의 subspace 네 종류는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**{0}, 원점 지나는 직선, 원점 지나는 평면, R³**

</details>

**40.** Ax = 0의 해집합이 subspace인 이유는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**A(kx₀) = 0, A(x₁ + x₂) = 0**

[Thm 3.4.3](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.4_Subspaces와-linear-independence.md#thm-343).

</details>

**41.** v₁, …, vₛ의 independence를 행렬로 판정하는 법은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**\[v₁ ⋯ vₛ\]c = 0이 trivial만이면 independent**

[Thm 3.4.7](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.4_Subspaces와-linear-independence.md#thm-347).

</details>

**42.** R⁴에서 벡터 5개는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**항상 dependent**

[Thm 3.4.8](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.4_Subspaces와-linear-independence.md#thm-348).

</details>

**43.** Ax = b의 일반해 구조는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**특수해 x₀ + Ax = 0의 일반해**

[Thm 3.5.2](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.5_Geometry-of-linear-systems.md#thm-352).

</details>

**44.** Ax = 0이 무한해일 때 Ax = b는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**해가 없거나 무한**

[Thm 3.5.3](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.5_Geometry-of-linear-systems.md#thm-353). 딱 1개는 불가능합니다.

</details>

**45.** Ax = b가 consistent일 조건은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**b가 column space에 있을 것**

[Thm 3.5.5](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.5_Geometry-of-linear-systems.md#thm-355).

</details>

**46.** Ax = 0의 해와 A의 row vectors의 관계는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**모든 row vector와 orthogonal**

[Thm 3.5.6](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.5_Geometry-of-linear-systems.md#thm-356).

</details>

**47.** Triangular matrix가 가역일 조건은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**대각 성분이 모두 0이 아님**

Thm 3.6.1.

</details>

**48.** 두 symmetric matrix의 곱 AB가 symmetric일 조건은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**AB = BA**

Thm 3.6.3.

</details>

**49.** A의 fixed point를 구하는 식은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**(I − A)x = 0**

예: A = \[1 0; 2 1\] → x = (0, t).

</details>

**50.** A³ = 0이면 (I − A)⁻¹은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**I + A + A²**

Thm 3.6.6.

</details>

**51.** LU가 존재하는 조건과 Ax = b 푸는 순서는? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**행 교환 없이 소거 가능, Ly = b → Ux = y**

[Thm 3.7.2](../수업요약/Ch3-2_Subspaces-Geometry-LU/3.7_LU-decomposition.md#thm-372).

</details>

**52.** LU에서 L의 대각과 대각 아래에는 무엇을 넣나? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**대각: leading 1을 만든 multiplier의 역수, 아래: 0을 만든 multiplier의 부호 반대**

Slide 56.

</details>

**53.** Block diagonal matrix의 역행렬은? <sub>〔SED 3-2〕</sub>

<details>
<summary>정답 보기</summary>

**각 대각 블록의 역행렬을 같은 위치에**

모든 블록이 가역이어야 합니다.

</details>

**54.** {(x, y) : y = 2x + 1}은 R²의 subspace인가? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

0을 포함하지 않습니다.

</details>

**55.** (1,2,1), (2,5,0), (3,3,8)은 independent인가? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**independent**

열로 세운 행렬의 det = −1 ≠ 0.

</details>

**56.** w = (9,1,0)을 v₁ = (1,2,3), v₂ = (1,4,6), v₃ = (2,−3,−5)의 결합으로? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**w = v₁ + 2v₂ + 3v₃**

Slide 30 Example 2.

</details>

**57.** 미지수 3개 동차계에서 free variable이 2개이면 해공간은? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**원점 지나는 평면**

Slide 34.

</details>

**58.** 같은 A에 b가 100개면 LU가 유리한 이유는? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**분해 ⅔n³은 한 번, 이후 b마다 ≈2n²**

Gaussian을 매번 하면 100·⅔n³입니다.

</details>

**59.** A = \[6 −2 0; 9 −1 1; 3 7 5\]의 L은? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**\[6 0 0; 9 2 0; 3 8 1\]**

Slide 57 Example 2.

</details>

**60.** 블록 곱을 row–column rule로 계산할 수 있는 조건은? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**A의 열 분할 = B의 행 분할**

블록 곱 AᵢₖBₖⱼ가 모두 정의되어야 합니다.

</details>

**61.** \[3 1; 5 2\]의 역행렬은? <sub>〔Ch3-2 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**\[2 −1; −5 3\]**

ad − bc = 1.

</details>

**62.** 서로 직교인 0이 아닌 벡터들이 independent인 이유는? <sub>〔SED Midterm〕</sub>

<details>
<summary>정답 보기</summary>

**결합 = 0에 vᵢ를 dot하면 kᵢ‖vᵢ‖² = 0**

Q7.

</details>

## Ch4 Determinants and Eigenvalues

> 개념 노트: [Ch4 Determinants and Eigenvalues 목차](../수업요약/Ch4_Determinants-and-Eigenvalues/README.md)

**63.** |−2 5 7; 0 3 8; 0 0 5| = ? <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**−30**

upper triangular입니다.

</details>

**64.** A = \[3 1 −4; 2 5 6; 1 4 8\]에서 C₃₂는? <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**−26**

M₃₂ = 26, 3 + 2는 홀수.

</details>

**65.** 3×3 A에서 det(A) = 5이면 det(2A), det(A⁻¹), det(Aᵀ)는? <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**40, 1/5, 5**

2³·5, 1/5, 그대로.

</details>

**66.** R₁ ↔ R₂ 후 R₃를 2배, 그다음 R₁ ← R₁ + 4R₃. det(A) = −3이면 최종 det는? <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**6**

(−3)(−1)(2). 배수 더하기는 불변입니다.

</details>

**67.** \[c c c; 1 c c; 1 1 c\]가 invertible인 조건 <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**c ≠ 0, 1**

det = c(c−1)². HW 3-1 Q6과 일치합니다.

</details>

**68.** A = \[1 3; 4 2\]의 eigenvalue와 eigenvector <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**λ = 5: (3,4), λ = −2: (−1,1)**

λ² − 3λ − 10 = (λ−5)(λ+2).

</details>

**69.** \[2 0; 5 3\]의 eigenvalue <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**2, 3**

lower triangular.

</details>

**70.** eigenvalue가 2, 3, −1인 3×3 행렬의 det와 trace <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**det = −6, tr = 4**

곱과 합.

</details>

**71.** singular 행렬은 반드시 λ = 0을 eigenvalue로 가진다 <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**True**

det(0I − A) = (−1)ⁿdet(A) = 0.

</details>

**72.** \[3 2; 2 3\]의 두 eigenspace는 서로 수직인가? <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**True**

y = −x, y = x.

</details>

**73.** Ax = λx에서 x = 0을 eigenvector로 인정하지 않는 이유 <sub>〔Det Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**모든 λ가 eigenvalue가 되어 정의가 무의미해지기 때문**

A0 = λ0은 항상 성립합니다.

</details>

## Ch6 Linear Transformations

> 개념 노트: [Ch6 Linear Transformations 목차](../수업요약/Ch6_Linear-Transformations/README.md)

**74.** T\_A의 A가 3×2이면 정의역과 공역은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**R² → R³**

Ax가 정의되려면 x는 2×1입니다.

</details>

**75.** A = \[1 −1; 2 5; 3 4\]일 때 T\_A(−1,3)은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**(−4, 13, 9)**

Example 3.

</details>

**76.** Linear transformation의 두 조건은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**T(cu) = cT(u), T(u + v) = T(u) + T(v)**

[Def 6.1.2](../수업요약/Ch6_Linear-Transformations/6.1_Matrices-as-transformations.md#def-612).

</details>

**77.** T(x,y) = (x+1, y)는 linear인가? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

T(0,0) = (1,0) ≠ 0.

</details>

**78.** T(x₁,x₂,x₃) = (x₁+x₂, x₂−x₃)의 standard matrix는? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**\[1 1 0; 0 1 −1\]**

Example 11.

</details>

**79.** 90° 회전 행렬은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**\[0 −1; 1 0\]**

R₉₀°.

</details>

**80.** y = x 반사의 standard matrix는? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**\[0 1; 1 0\]**

Table 6.1.1.

</details>

**81.** x 방향 shear, k = 2가 (1,1)을 보내는 곳은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**(3, 1)**

T(x,y) = (x + ky, y).

</details>

**82.** Contraction과 dilation의 차이는? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**0 ≤ k &lt; 1이면 contraction, k > 1이면 dilation**

Table 6.2.1.

</details>

**83.** A가 orthogonal임을 가장 쉽게 보이는 방법은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**AᵀA = I 또는 AAᵀ = I 하나를 확인**

[Def 6.2.2](../수업요약/Ch6_Linear-Transformations/6.2_Geometry-of-linear-operators.md#def-622) Remark.

</details>

**84.** Orthogonal matrix의 det는? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**±1**

[Thm 6.2.3](../수업요약/Ch6_Linear-Transformations/6.2_Geometry-of-linear-operators.md#thm-623)(d).

</details>

**85.** det(A) = 1이면 A는 orthogonal인가? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

\[1 2; 0 1\]이 반례입니다.

</details>

**86.** R²에서 orthogonal operator의 두 종류와 구분법은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**회전(det = 1), 반사(det = −1)**

[Thm 6.2.7](../수업요약/Ch6_Linear-Transformations/6.2_Geometry-of-linear-operators.md#thm-627), Example 4.

</details>

**87.** Orthogonal matrix의 열과 행은? <sub>〔Ch6〕</sub>

<details>
<summary>정답 보기</summary>

**둘 다 orthonormal**

[Thm 6.2.5](../수업요약/Ch6_Linear-Transformations/6.2_Geometry-of-linear-operators.md#thm-625).

</details>

**88.** 4×6 A의 RREF pivot이 3개면 null(A)의 차원은? <sub>〔Ch6-2 p.10〕</sub>

<details>
<summary>정답 보기</summary>

**3**

free variable = 6 − 3 = 3개.

</details>

**89.** R³에서 xy평면 정사영의 kernel과 range는? <sub>〔Ch6-2 p.12〕</sub>

<details>
<summary>정답 보기</summary>

**z축, xy평면**

차원 1 + 2 = 3.

</details>

**90.** 3×2 행렬 T<sub>A</sub>: R² → R³은 onto일 수 있나? <sub>〔Ch6-2 p.17〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

열 2개로 R³을 span할 수 없습니다(rank ≤ 2 &lt; 3).

</details>

**91.** T<sub>A</sub>를 먼저, T<sub>B</sub>를 나중에 적용한 합성의 행렬은? <sub>〔Ch6-2 p.27〕</sub>

<details>
<summary>정답 보기</summary>

**BA**

나중 것이 왼쪽입니다.

</details>

**92.** 반사 H<sub>θ</sub>의 역변환은? <sub>〔Ch6-2 p.34〕</sub>

<details>
<summary>정답 보기</summary>

**H<sub>θ</sub> 자신**

H² = I. 행렬로도 H⁻¹ = H = Hᵀ.

</details>

**93.** Translation이 linear가 아닌 이유는? <sub>〔Ch6-2 p.43〕</sub>

<details>
<summary>정답 보기</summary>

**T(0) = x₀ ≠ 0**

[Thm 6.1.3](../수업요약/Ch6_Linear-Transformations/6.1_Matrices-as-transformations.md#thm-613): linear이면 T(0) = 0.

</details>

**94.** 회전 후 이동을 homogeneous로 쓴 행렬은 TR′인가 R′T인가? <sub>〔Ch6-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**TR′**

먼저 적용하는 R′이 오른쪽.

</details>

## Ch7 Dimension and Structure

> 개념 노트: [Ch7 Dimension and Structure 목차](../수업요약/Ch7_Dimension-and-Structure/README.md)

**95.** R³ 안의 원점 평면의 dimension은? <sub>〔Ch7 p.12〕</sub>

<details>
<summary>정답 보기</summary>

**2**

성분 수(3)가 아니라 basis 개수입니다.

</details>

**96.** Ax = 0의 RREF에 free 변수가 3개이면 해공간 차원은? <sub>〔Ch7 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**3**

Canonical basis 벡터가 free 변수마다 하나.

</details>

**97.** R⁴에서 벡터 5개는 independent일 수 있나? <sub>〔Ch7 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

dim R⁴ = 4가 independent 벡터의 최대 개수([Thm 7.2.3](../수업요약/Ch7_Dimension-and-Structure/7.2_Properties-of-bases.md#thm-723)).

</details>

**98.** 4×6 A의 null(Aᵀ)는 어느 공간의 subspace인가? <sub>〔Ch7 p.27〕</sub>

<details>
<summary>정답 보기</summary>

**R⁴**

Aᵀ는 6×4이므로 Aᵀy = 0의 y는 R⁴(행 수 m)입니다.

</details>

**99.** x ∈ null(A)이면 x와 A의 각 행의 내적은? <sub>〔Ch7 p.34〕</sub>

<details>
<summary>정답 보기</summary>

**0**

Ax의 각 성분이 행과 x의 내적입니다.

</details>

**100.** 행 연산으로 바뀌는 fundamental space는? <sub>〔Ch7 p.37〕</sub>

<details>
<summary>정답 보기</summary>

**col(A) (그리고 null(Aᵀ))**

Row space와 null space만 보존됩니다. `보완`

</details>

**101.** 5×8 A의 rank가 3이면 nullity는? <sub>〔Ch7 p.44〕</sub>

<details>
<summary>정답 보기</summary>

**5**

8 − 3. 열 수를 씁니다.

</details>

**102.** 3×5 A, rank 2에서 dim null(Aᵀ)는? <sub>〔Ch7 p.58〕</sub>

<details>
<summary>정답 보기</summary>

**1**

m − k = 3 − 2.

</details>

**103.** rank(A) = 2, rank\[A | b\] = 3이면? <sub>〔Ch7 p.60〕</sub>

<details>
<summary>정답 보기</summary>

**inconsistent**

b ∉ col(A).

</details>

**104.** 2×3 A에서 Ax = b의 해가 정확히 하나일 수 있나? <sub>〔Ch7 p.63〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

nullity ≥ 1이라 해가 있으면 무한히 많습니다.

</details>

**105.** proj<sub>a</sub>x의 분모는 ‖a‖인가 ‖a‖²인가? <sub>〔Ch7-2 p.4〕</sub>

<details>
<summary>정답 보기</summary>

**‖a‖²**

a가 단위벡터일 때만 분모가 1입니다.

</details>

**106.** W 위 정사영 행렬 P의 역행렬이 있나 (W ≠ Rⁿ)? <sub>〔Ch7-2 p.9〕</sub>

<details>
<summary>정답 보기</summary>

**없다**

W⊥의 0 아닌 벡터가 0으로 갑니다. det P = 0.

</details>

**107.** (1, 2, 0), (−2, 1, 0), (0, 0, 3)은 R³의 basis인가? <sub>〔Ch7-2 p.13〕</sub>

<details>
<summary>정답 보기</summary>

**예**

서로 내적 0, 0 벡터 없음 → independent 3개 ([Thm 7.9.1](../수업요약/Ch7_Dimension-and-Structure/7.9_Orthonormal-bases-and-the-Gram–Schmidt-process.md#thm-791)).

</details>

**108.** Orthonormal basis에서 w의 i번째 좌표는? <sub>〔Ch7-2 p.15〕</sub>

<details>
<summary>정답 보기</summary>

**w·vᵢ**

연립방정식 없이 내적 한 번.

</details>

**109.** Gram–Schmidt v₂ = w₂ − ? <sub>〔Ch7-2 p.17〕</sub>

<details>
<summary>정답 보기</summary>

**(w₂·v₁/‖v₁‖²)v₁**

v₁ 방향 정사영을 뺍니다.

</details>

**110.** A = QR에서 R은 어떤 행렬인가? <sub>〔Ch7-2 p.25〕</sub>

<details>
<summary>정답 보기</summary>

**invertible upper triangular**

대각 성분 ‖vᵢ‖ > 0.

</details>

**111.** QR로 least squares를 풀 때 푸는 식은? <sub>〔Ch7-2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**Rx = Qᵀb**

R이 삼각이라 back substitution.

</details>

## W10 Matrix Models

> 개념 노트: [MATLAB 목차](../수업요약/MATLAB/README.md)

**112.** xₖ가 숫자 하나가 아니라 벡터인 이유는? <sub>〔W10 00:45〕</sub>

<details>
<summary>정답 보기</summary>

**여러 값을 같은 시점에 함께 측정하기 때문**

예: (도시 인구, 교외 인구). <sub>〔W10 Atlas〕</sub>

</details>

**113.** x₃를 x₀와 A로만 나타내면? <sub>〔W10 08:30〕</sub>

<details>
<summary>정답 보기</summary>

**x₃ = A³x₀**

A를 세 번 곱합니다. 결합법칙으로 A³을 먼저 계산해도 같습니다.

</details>

**114.** difference equation과 differential equation의 차이는? <sub>〔W10 00:45〕</sub>

<details>
<summary>정답 보기</summary>

**difference는 이산 단계 사이, differential은 연속 시간의 변화율**

이번 주는 difference입니다. 강의 음성의 "differential"은 정정 대상입니다.

</details>

**115.** 이주 행렬의 열 합이 1인 이유는? <sub>〔W10 06:30〕</sub>

<details>
<summary>정답 보기</summary>

**한 지역 사람은 남거나 떠나므로 비율 합이 100%**

그래서 총인구가 보존됩니다.

</details>

**116.** M = \[0.95 0.03; 0.05 0.97\]에서 0.03의 뜻은? <sub>〔W10 06:30〕</sub>

<details>
<summary>정답 보기</summary>

**교외(2열) → 도시(1행) 이동 비율 3%**

열 = 출발, 행 = 도착.

</details>

**117.** x₀ = (600, 400)이면 1년 뒤 교외 인구는? <sub>〔W10 Atlas〕</sub>

<details>
<summary>정답 보기</summary>

**418**

0.05 × 600 + 0.97 × 400 = 30 + 388. 학습용 예시입니다.

</details>

**118.** Practice 1(7%/5%)의 M은? <sub>〔W10 21:45〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**\[0.93 0.05; 0.07 0.95\]**

1열 = 도시 출발(93% 잔류, 7% 교외), 2열 = 교외 출발(5% 도시, 95% 잔류).

</details>

**119.** 이동 인원 수만 주어질 때 비율은 어떻게 구하나? <sub>〔W10 25:00〕</sub>

<details>
<summary>정답 보기</summary>

**이동 인원 ÷ 출발 지역 인구**

유출은 California 인구로, 유입은 California 밖 인구로 나눕니다. 잔류 = 1 − 비율.

</details>

**120.** x, Cx, d는 각각 무엇인가? <sub>〔W10 09:00〕</sub>

<details>
<summary>정답 보기</summary>

**총생산, 중간 수요, 최종 수요**

</details>

**121.** x = Cx + d를 Ax = b 꼴로 바꾸면? <sub>〔W10 16:00〕</sub>

<details>
<summary>정답 보기</summary>

**(I − C)x = d**

x = Ix로 써서 묶습니다.

</details>

**122.** c₂ = (0.4, 0.3, 0.1)일 때 농업 200단위에 드는 재료는? <sub>〔W10 12:15〕</sub>

<details>
<summary>정답 보기</summary>

**(80, 60, 20)**

200c₂. 학습용 예시입니다.

</details>

**123.** x ≈ (226, 119, 78)이 d = (50, 30, 20)보다 훨씬 큰 이유는? <sub>〔W10 17:45〕</sub>

<details>
<summary>정답 보기</summary>

**재료를 만드는 데도 재료가 들어 중간 수요가 쌓이므로**

(I − C)⁻¹ = I + C + C² + ⋯로 볼 수 있습니다(열 합 &lt; 1일 때). `보완`

</details>

**124.** 열 합 &lt; 1의 경제적 의미는? <sub>〔W10 19:30〕</sub>

<details>
<summary>정답 보기</summary>

**1단위를 만드는 재료 가치가 1단위보다 작음**

손해 보며 생산하지 않는다는 뜻입니다.

</details>

**125.** `M^10`과 `M.^10`의 차이는? <sub>〔W10 25:00〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**M^10은 행렬 거듭제곱, M.^10은 원소별 10제곱**

10년 뒤 예측에는 M^10을 씁니다.

</details>

**126.** (I − C)x = d를 푸는 세 방법과 강의 권장은? <sub>〔W10 26:45〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**`(I-C)\d`, `inv(I-C)*d`, `rref([I-C d])`; 권장은 backslash**

큰 행렬에서 빠르고 정확합니다.

</details>

**127.** `eye(3)`은? <sub>〔W10 26:45〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**3×3 단위행렬**

I − C를 만들 때 씁니다.

</details>

**128.** Leontief Theorem의 가정을 모두 말하면? <sub>〔W10 18:00〕</sub>

<details>
<summary>정답 보기</summary>

**C와 d의 성분이 음수 없음, C의 각 열 합 &lt; 1**

결론: (I − C)⁻¹ 존재, x ≥ 0 유일.

</details>

**129.** 열 합이 1 이상이면 해가 절대 없는가? <sub>〔W10 Models〕</sub>

<details>
<summary>정답 보기</summary>

**아니다**

정리는 충분조건입니다. 역행렬은 있을 수 있지만 음수 해가 나올 수 있습니다(계산기의 c₁₁ = 0.85 프리셋).

</details>

**130.** Example 2에서 (I − C)⁻¹의 (1,1) 성분 80/27 ≈ 2.963의 뜻은? <sub>〔W10 Models〕</sub>

<details>
<summary>정답 보기</summary>

**제조 최종 수요가 1 늘 때 제조 생산이 약 2.96 늘어야 함**

직접 + 간접 투입을 모두 더한 multiplier입니다.

</details>

**131.** MATLAB `sum(C)`는 행 합인가 열 합인가? <sub>〔W10 26:45〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**열 합**

기본 dimension 1. 정리 조건을 바로 확인합니다.

</details>

**132.** Practice 4에서 계산 전에 확인할 것은? <sub>〔W10 30:45〕 · 연결: MATLAB</sub>

<details>
<summary>정답 보기</summary>

**`sum(C)`의 최댓값 0.9293 &lt; 1**

정리 조건이 맞으면 음수 없는 유일해가 보장됩니다.

</details>

---
[과목 지도](../README.md)
