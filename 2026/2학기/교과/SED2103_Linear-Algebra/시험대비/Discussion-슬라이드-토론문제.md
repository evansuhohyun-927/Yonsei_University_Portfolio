# Slide Discussion 문제 전체

강의 슬라이드의 Discussion 문항입니다. 정답을 펼치기 전에 먼저 답과 근거를 적어 보세요. 슬라이드에 답이 없는 문항은 직접 풀어 확인한 답입니다.

**목차** [Ch1 Vectors](#ch1-vectors) (13) · [Ch2 Systems of Linear Equations](#ch2-systems-of-linear-equations) (11) · [Ch3-1 Matrices and Matrix Algebra (1)](#ch3-1-matrices-and-matrix-algebra-1) (12) · [Ch3-2 Subspaces, Geometry, Special Matrices, LU](#ch3-2-subspaces-geometry-special-matrices-lu) (16) · [Ch4 Determinants and Eigenvalues](#ch4-determinants-and-eigenvalues) (10) · [Ch6 Linear Transformations](#ch6-linear-transformations) (18) · [Ch7 Dimension and Structure](#ch7-dimension-and-structure) (36)

## Ch1 Vectors

> 개념 노트: [Ch1 Vectors 목차](../수업요약/Ch1_Vectors/README.md)

**1.** Time은 vector인가 scalar인가? <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**Scalar**

방향 없이 크기만으로 기술됩니다. 슬라이드에 답은 없습니다.

</details>

**2.** R³의 세 벡터 합이 0이면 같은 평면에 있어야 하는가? <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**예**

w = −(u+v)이므로 w는 span{u, v} 안에 있습니다.

</details>

**3.** x + y = x + z이면 y = z <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**T**

양변에 −x를 더합니다.

</details>

**4.** x + y = 0이면 모든 a, b에 ax + by = 0 <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**F**

y = −x이면 ax + by = (a−b)x입니다.

</details>

**5.** 평행하고 길이가 같은 벡터는 같다 <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**F**

방향이 반대일 수 있습니다.

</details>

**6.** ax = 0이면 a = 0 또는 x = 0 <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**T**

‖ax‖ = |a|‖x‖ = 0입니다.

</details>

**7.** au + bv = 0이면 u, v는 평행 <sub>〔Ch1 p.14〕</sub>

<details>
<summary>정답 보기</summary>

**F**

a = b = 0이면 아무 벡터나 성립합니다.

</details>

**8.** u·(v+w), u·v + u·w, (u·v)+w 중 잘못된 식은? <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**(u·v) + w**

스칼라와 벡터는 더할 수 없습니다.

</details>

**9.** ‖u‖ = ‖v‖ = 1이고 u ⊥ v이면 d(u,v) = ? <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**√2**

d² = ‖u‖² + ‖v‖² = 2. 직각이등변삼각형의 빗변입니다.

</details>

**10.** ‖u+v‖² = ‖u‖²+‖v‖²이면 orthogonal <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**T**

전개하면 2u·v = 0입니다.

</details>

**11.** u ⊥ v, u ⊥ w이면 u ⊥ (v+w) <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**T**

분배법칙입니다.

</details>

**12.** u ⊥ (v+w)이면 u ⊥ v, u ⊥ w <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**F**

u·v = 1, u·w = −1이어도 합은 0입니다.

</details>

**13.** ‖u+v‖ = 0이면 u = −v <sub>〔Ch1 p.21〕</sub>

<details>
<summary>정답 보기</summary>

**T**

u + v = 0입니다.

</details>

## Ch2 Systems of Linear Equations

> 개념 노트: [Ch2 Systems of Linear Equations 목차](../수업요약/Ch2_Systems-of-Linear-Equations/README.md)

**14.** 세 직선 ax+by=k, cx+dy=l, ex+fy=m의 위치 관계 <sub>〔Ch2 p.11〕</sub>

<details>
<summary>정답 보기</summary>

**해 없음: 공통점 없음 / 해 1개: 적어도 두 직선이 다르고 모두 한 점 통과 / 해 무한: 세 직선 일치**

교점의 공통 여부로 분류합니다.

</details>

**15.** 두 열 이상의 행렬은 어떤 시스템의 augmented matrix이다 <sub>〔Ch2 p.11〕</sub>

<details>
<summary>정답 보기</summary>

**T**

마지막 열을 상수항으로 봅니다.

</details>

**16.** 해가 같은 두 시스템은 augmented matrix가 같다 <sub>〔Ch2 p.11〕</sub>

<details>
<summary>정답 보기</summary>

**F**

x = 1과 2x = 2는 해가 같습니다.

</details>

**17.** 행에 0을 곱해도 해 집합이 변하지 않는다 <sub>〔Ch2 p.11〕</sub>

<details>
<summary>정답 보기</summary>

**F**

식 하나가 사라집니다. row operation은 0이 아닌 상수만 허용합니다.

</details>

**18.** 3×5 행렬 RREF의 leading 1 최대 개수 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**3**

행 수를 넘을 수 없습니다.

</details>

**19.** 3×5 행렬 REF의 leading 1 최대 개수 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**3**

같은 이유입니다.

</details>

**20.** 5×3 행렬 RREF의 leading 1 최대 개수 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**3**

열 수를 넘을 수 없습니다.

</details>

**21.** 미지수가 식보다 많으면 consistent <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**F**

x+y=1, x+y=2는 해가 없습니다.

</details>

**22.** linear system이 정확히 2개의 해를 가질 수 있다 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**F**

[Thm 2.1.1](../수업요약/Ch2_Systems-of-Linear-Equations/2.1_Linear-systems.md#thm-211).

</details>

**23.** 식 2개, 미지수 3개의 시스템이 유일해를 가질 수 있다 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**F**

free variable이 생깁니다.

</details>

**24.** 행렬이 둘 이상의 RREF로 줄어들 수 있다 <sub>〔Ch2 p.29〕</sub>

<details>
<summary>정답 보기</summary>

**F**

RREF는 유일합니다.

</details>

## Ch3-1 Matrices and Matrix Algebra (1)

> 개념 노트: [Ch3-1 Matrices and Matrix Algebra (1) 목차](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/README.md)

**25.** AB, BA가 모두 정의되면 A, B는 정방행렬 <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A가 2×3, B가 3×2일 수 있습니다.

</details>

**26.** AB + BA가 정의되면 A, B는 같은 크기의 정방행렬 <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**T**

AB는 m×m, BA는 n×n이므로 m = n입니다.

</details>

**27.** B에 영열이 있으면 AB에도 있다 <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**T**

AB의 j열 = A(j열).

</details>

**28.** B에 영열이 있으면 BA에도 있다 <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**F**

BA의 열은 B의 열들의 조합입니다.

</details>

**29.** tr(AᵀA), tr(AAᵀ)는 모든 A에 정의 <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**T**

둘 다 정방입니다.

</details>

**30.** u, v가 행벡터이면 uᵀv = u·v <sub>〔Ch3-1 p.16〕</sub>

<details>
<summary>정답 보기</summary>

**F**

uᵀv는 n×n 행렬입니다. uvᵀ가 스칼라입니다.

</details>

**31.** (AB)² = A²B² <sub>〔Ch3-1 p.30〕</sub>

<details>
<summary>정답 보기</summary>

**F**

교환법칙이 없습니다.

</details>

**32.** (A−B)² = (B−A)² <sub>〔Ch3-1 p.30〕</sub>

<details>
<summary>정답 보기</summary>

**T**

A−B = −(B−A).

</details>

**33.** (A⁻ⁿ)ᵀ = (Aᵀ)⁻ⁿ <sub>〔Ch3-1 p.30〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 3.2.10](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.2_Inverses와-대수-성질.md#thm-3210-transpose), 3.2.11.

</details>

**34.** tr(AB) = tr(A)tr(B) <sub>〔Ch3-1 p.30〕</sub>

<details>
<summary>정답 보기</summary>

**F**

일반적으로 tr(AB) ≠ tr(A)tr(B)이고, 성립하는 것은 tr(AB) = tr(BA)입니다.

</details>

**35.** A, B가 invertible이면 A+B도 invertible <sub>〔Ch3-1 p.30〕</sub>

<details>
<summary>정답 보기</summary>

**F**

B = −A이면 합이 0입니다.

</details>

**36.** Ax = b가 consistent인 b가 항상 존재하는 이유 <sub>〔Ch3-1 p.45〕</sub>

<details>
<summary>정답 보기</summary>

**b = 0**

x = 0이 해이므로, 또는 임의의 x에 b = Ax로 둡니다.

</details>

## Ch3-2 Subspaces, Geometry, Special Matrices, LU

> 개념 노트: [Ch3-2 Subspaces, Geometry, Special Matrices, LU 목차](../수업요약/Ch3-2_Subspaces-Geometry-LU/README.md)

**37.** 모든 subspace가 0을 포함하는 이유 <sub>〔Ch3-2 p.4〕</sub>

<details>
<summary>정답 보기</summary>

**0·v = 0**

scalar multiplication에 닫혀 있기 때문입니다.

</details>

**38.** 제1사분면은 왜 subspace가 아닌가 <sub>〔Ch3-2 p.5〕</sub>

<details>
<summary>정답 보기</summary>

**음수배에 닫혀 있지 않음**

양수끼리의 합은 양수이지만 (−1)v는 벗어납니다.

</details>

**39.** 0이 아닌 세 벡터가 dependent이면 각 벡터는 나머지 둘의 결합 <sub>〔Ch3-2 p.22〕</sub>

<details>
<summary>정답 보기</summary>

**F**

v₁, 2v₁, v₃(v₃은 다른 방향)에서 v₃은 표현되지 않습니다.

</details>

**40.** Rⁿ의 두 벡터의 모든 결합은 평면 <sub>〔Ch3-2 p.22〕</sub>

<details>
<summary>정답 보기</summary>

**F**

평행하면 직선입니다.

</details>

**41.** u가 v, w의 결합이 아니면 세 벡터는 independent <sub>〔Ch3-2 p.22〕</sub>

<details>
<summary>정답 보기</summary>

**F**

v, w가 평행할 수 있습니다.

</details>

**42.** 0을 포함한 집합은 dependent <sub>〔Ch3-2 p.22〕</sub>

<details>
<summary>정답 보기</summary>

**T**

1·0 = 0입니다.

</details>

**43.** {v₁,v₂,v₃}가 independent이면 {kv₁,kv₂,kv₃}도 (k≠0) <sub>〔Ch3-2 p.22〕</sub>

<details>
<summary>정답 보기</summary>

**T**

k를 묶어 나눕니다.

</details>

**44.** Ax = b의 해가 무한이면 Ax = 0도 무한 <sub>〔Ch3-2 p.35〕</sub>

<details>
<summary>정답 보기</summary>

**T**

해 집합이 x₀ + W이므로 W가 무한입니다.

</details>

**45.** Ax = b가 inconsistent이면 Ax = 0은 trivial만 <sub>〔Ch3-2 p.35〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = \[1 1; 1 1\], b = (1,2).

</details>

**46.** Ax = b의 모든 해는 A의 행벡터와 orthogonal <sub>〔Ch3-2 p.35〕</sub>

<details>
<summary>정답 보기</summary>

**F**

b = 0일 때만 성립합니다.

</details>

**47.** AAᵀ가 invertible이면 A도 <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = \[1 0\]이면 AAᵀ = \[1\]. A가 정방이면 Thm 3.6.5로 참입니다.

</details>

**48.** A+B가 대칭이면 A, B도 대칭 <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**F**

\[0 1; −1 0\] + \[0 −1; 1 0\] = 0.

</details>

**49.** Ax = 0이 trivial만이면 Aᵀx = 0도 <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**T**

A invertible ⇒ Aᵀ invertible.

</details>

**50.** A²이 대칭이면 A도 <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = \[0 1; −1 0\]이면 A² = −I.

</details>

**51.** A invertible이면 (A⁻¹)ᵀ = (Aᵀ)⁻¹ <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 3.2.11](../수업요약/Ch3-1_Matrices-and-Matrix-Algebra/3.2_Inverses와-대수-성질.md#thm-3211).

</details>

**52.** A invertible이면 I−A도 <sub>〔Ch3-2 p.50〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = I.

</details>

## Ch4 Determinants and Eigenvalues

> 개념 노트: [Ch4 Determinants and Eigenvalues 목차](../수업요약/Ch4_Determinants-and-Eigenvalues/README.md)

**53.** 정수 행렬의 det는 왜 정수인가 <sub>〔Ch4 p.10〕</sub>

<details>
<summary>정답 보기</summary>

**정수의 곱과 합**

det는 성분의 곱의 합과 차입니다.

</details>

**54.** 3×3에서 det ≠ 0일 때 0의 최대 개수 <sub>〔Ch4 p.10〕</sub>

<details>
<summary>정답 보기</summary>

**6**

각 행·열에 0 아닌 수가 하나씩 있는 permutation 형태입니다. 7개면 행이나 열 하나가 0이 됩니다.

</details>

**55.** det\[x y 1; a₁ b₁ 1; a₂ b₂ 1\] = 0의 그래프 <sub>〔Ch4 p.10〕</sub>

<details>
<summary>정답 보기</summary>

**(a₁,b₁), (a₂,b₂)를 지나는 직선**

x, y의 일차식이고 두 점을 넣으면 같은 행이 생겨 0입니다. 두 점이 다를 때입니다.

</details>

**56.** det(I+A) = 1 + det(A) <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = I이면 4 ≠ 2 (2×2).

</details>

**57.** det(A⁴) = (det A)⁴ <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 4.2.5](../수업요약/Ch4_Determinants-and-Eigenvalues/4.2_Properties-of-determinants.md#thm-425).

</details>

**58.** det(3A) = 3 det A <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**F**

3ⁿ det A.

</details>

**59.** det A = 0이면 Ax = 0의 해는 무한 <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**T**

A singular ⇒ nontrivial solution ⇒ 무한.

</details>

**60.** A = A⁻¹이면 det A = ±1 <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**T**

(det A)² = 1.

</details>

**61.** RREF에 영행이 있으면 det A = 0 <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**T**

A가 singular입니다.

</details>

**62.** det A ≠ 0이면 A는 elementary의 곱 <sub>〔Ch4 p.20〕</sub>

<details>
<summary>정답 보기</summary>

**T**

Unifying theorem.

</details>

## Ch6 Linear Transformations

> 개념 노트: [Ch6 Linear Transformations 목차](../수업요약/Ch6_Linear-Transformations/README.md)

**63.** T: Rⁿ → Rᵐ이고 T(0) = 0이면 T는 linear <sub>〔Ch6 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**F**

T(x₁,x₂,x₃) = (x₁²,x₂²,x₃²)는 T(0) = 0이지만 linear가 아닙니다.

</details>

**64.** 모든 c₁, c₂, u, v에 T(c₁u + c₂v) = c₁T(u) + c₂T(v)이면 T는 linear <sub>〔Ch6 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

c₁ = c₂ = 1이면 additivity, c₂ = 0이면 homogeneity입니다.

</details>

**65.** T(−v) = −T(v)인 linear T: Rⁿ → Rⁿ은 하나뿐 <sub>〔Ch6 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**F**

모든 linear T가 만족합니다. T₀와 T<sub>I</sub>가 서로 다른 예입니다.

</details>

**66.** T(u + v) = T(u − v)인 linear T: Rⁿ → Rⁿ은 하나뿐 <sub>〔Ch6 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

T(u) + T(v) = T(u) − T(v) → 2T(v) = 0 → T는 zero transformation뿐입니다.

</details>

**67.** v₀ ≠ 0이면 T(v) = v₀ + v는 linear operator <sub>〔Ch6 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**F**

T(0) = v₀ ≠ 0입니다.

</details>

**68.** A = \[2 0; 0 0\]이 unit square에 주는 효과 <sub>〔Ch6 p.40〕</sub>

<details>
<summary>정답 보기</summary>

**(0,0)–(2,0) 선분으로 납작해짐**

x축으로 정사영한 뒤 x 방향으로 2배 늘립니다. 넓이 0.

</details>

**69.** A = \[0 0; 0 3\]이 unit square에 주는 효과 <sub>〔Ch6 p.40〕</sub>

<details>
<summary>정답 보기</summary>

**(0,0)–(0,3) 선분으로 납작해짐**

y축으로 정사영한 뒤 y 방향으로 3배 늘립니다. 넓이 0.

</details>

**70.** A = \[2 0; 0 3\]이 unit square에 주는 효과 <sub>〔Ch6 p.40〕</sub>

<details>
<summary>정답 보기</summary>

**2×3 직사각형**

x 방향 2배, y 방향 3배. 넓이 6.

</details>

**71.** A = \[√3/2 1/2; −1/2 √3/2\]가 unit square에 주는 효과 <sub>〔Ch6 p.40〕</sub>

<details>
<summary>정답 보기</summary>

**시계 방향 30° 회전**

R<sub>−30°</sub>입니다. det = 1, 모양과 넓이를 유지합니다.

</details>

**72.** T: Rⁿ → Rⁿ이 one-to-one이고 T(u − v) = 0이면 u = v <sub>〔Ch6-2 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

ker(T) = {0}이므로 u − v = 0입니다.

</details>

**73.** T: Rⁿ → Rⁿ이 onto이고 T(u − v) = 0이면 u = v <sub>〔Ch6-2 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

Rⁿ 위의 operator이므로 onto ⇒ one-to-one ([Thm 6.3.14](../수업요약/Ch6_Linear-Transformations/6.3_Kernel-and-range.md#thm-6314)).

</details>

**74.** det(A) = 0이면 T<sub>A</sub>는 onto도 one-to-one도 아니다 <sub>〔Ch6-2 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 6.3.15](../수업요약/Ch6_Linear-Transformations/6.3_Kernel-and-range.md#thm-6315): det ≠ 0이 (k), (l)과 동치이므로 둘 다 거짓입니다.

</details>

**75.** T: Rⁿ → Rᵐ이 one-to-one이 아니면 ker(T)는 무한히 많은 벡터를 가진다 <sub>〔Ch6-2 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

ker(T) ≠ {0}인 subspace이므로 0이 아닌 v와 그 배수 tv를 모두 포함합니다.

</details>

**76.** R²의 shear는 one-to-one linear operator이다 <sub>〔Ch6-2 p.23〕</sub>

<details>
<summary>정답 보기</summary>

**T**

\[1 k; 0 1\]의 det = 1 ≠ 0이므로 invertible입니다.

</details>

**77.** T₁이 one-to-one이 아니면 T₂ ∘ T₁도 아니다 <sub>〔Ch6-2 p.37〕</sub>

<details>
<summary>정답 보기</summary>

**T**

T₁(u) = T₁(v), u ≠ v이면 T₂(T₁(u)) = T₂(T₁(v))입니다.

</details>

**78.** T₁이 onto가 아니면 T₂ ∘ T₁도 onto가 아니다 <sub>〔Ch6-2 p.37〕</sub>

<details>
<summary>정답 보기</summary>

**F**

반례: T₁: R → R², x ↦ (x, 0)은 onto가 아님. T₂: R² → R, (a, b) ↦ a. T₂ ∘ T₁ = 항등이라 onto입니다.

</details>

**79.** T₂가 one-to-one이 아니면 T₂ ∘ T₁도 아니다 <sub>〔Ch6-2 p.37〕</sub>

<details>
<summary>정답 보기</summary>

**F**

같은 반례: T₂는 one-to-one이 아니지만 T₂ ∘ T₁ = 항등은 one-to-one입니다.

</details>

**80.** T₂가 onto가 아니면 T₂ ∘ T₁도 onto가 아니다 <sub>〔Ch6-2 p.37〕</sub>

<details>
<summary>정답 보기</summary>

**T**

ran(T₂ ∘ T₁) ⊆ ran(T₂) ≠ Rᵏ.

</details>

## Ch7 Dimension and Structure

> 개념 노트: [Ch7 Dimension and Structure 목차](../수업요약/Ch7_Dimension-and-Structure/README.md)

**81.** m×n 동차계 Ax = 0의 해공간 차원의 최댓값 <sub>〔Ch7 p.15〕</sub>

<details>
<summary>정답 보기</summary>

**n**

해공간은 Rⁿ의 subspace입니다. A = 0이면 n이 됩니다. 또 nullity = n − rank ≥ n − m.

</details>

**82.** Rⁿ의 subspace가 가질 수 있는 dimension <sub>〔Ch7 p.15〕</sub>

<details>
<summary>정답 보기</summary>

**0, 1, …, n**

{0}이 0, Rⁿ이 n입니다([Thm 7.2.4](../수업요약/Ch7_Dimension-and-Structure/7.2_Properties-of-bases.md#thm-724)).

</details>

**83.** span{(1,0,1,0), (1,1,0,0), (1,1,1,0)} ⊆ R⁴의 dimension <sub>〔Ch7 p.15〕</sub>

<details>
<summary>정답 보기</summary>

**3**

세 벡터를 행으로 한 행렬의 rank = 3.

</details>

**84.** S = {v₁, …, v<sub>k</sub>}가 Rⁿ에서 independent이면 k ≤ n <sub>〔Ch7 p.26 (a)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 7.2.3](../수업요약/Ch7_Dimension-and-Structure/7.2_Properties-of-bases.md#thm-723): independent 벡터 수 ≤ dim Rⁿ = n.

</details>

**85.** S가 Rⁿ을 span하면 k ≥ n <sub>〔Ch7 p.26 (b)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

k &lt; n개로 span하면 그 안에서 고른 basis가 n개보다 적어 [Thm 7.1.4](../수업요약/Ch7_Dimension-and-Structure/7.1_Basis-and-dimension.md#thm-714)에 모순.

</details>

**86.** Rⁿ의 모든 벡터가 S로 정확히 한 가지로 표현되면 k = n <sub>〔Ch7 p.26 (c)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

유일 표현 ⇒ independent(0의 표현이 하나) + span ⇒ basis ⇒ k = n.

</details>

**87.** n×n 동차계가 해를 무한히 가지면 A의 행은 Rⁿ의 basis가 아니다 <sub>〔Ch7 p.26 (d)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

A가 singular → [Thm 7.2.7](../수업요약/Ch7_Dimension-and-Structure/7.2_Properties-of-bases.md#thm-727) (p) 거짓.

</details>

**88.** dim이 같은 서로 다른 subspace V, W는 어느 쪽도 다른 쪽의 subspace가 아니다 <sub>〔Ch7 p.26 (e)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

V ⊆ W이고 dim이 같으면 V = W([Thm 7.2.4](../수업요약/Ch7_Dimension-and-Structure/7.2_Properties-of-bases.md#thm-724)(b))이므로 서로 다르다는 가정에 모순.

</details>

**89.** A의 0 아닌 행은 row space의 basis이다 <sub>〔Ch7 p.41 (a)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

REF가 아니면 dependent일 수 있습니다. 예: \[1 1; 2 2\].

</details>

**90.** E가 elementary matrix이면 A와 EA의 null space가 같다 <sub>〔Ch7 p.41 (b)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

E는 가역: Ax = 0 ⇔ EAx = 0.

</details>

**91.** rank n인 n×n A는 invertible <sub>〔Ch7 p.41 (c)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 7.4.4](../수업요약/Ch7_Dimension-and-Structure/7.4_The-dimension-theorem-and-its-implications.md#thm-744) (q).

</details>

**92.** 0이 아닌 A에서 null(A) ∩ row(A)는 0이 아닌 벡터를 포함한다 <sub>〔Ch7 p.41 (d)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

x가 둘 다에 있으면 x·x = 0 → x = 0. 교집합은 {0}뿐입니다.

</details>

**93.** S⊥ 벡터들의 linear combination은 S⊥에 있다 <sub>〔Ch7 p.41 (e)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

S⊥은 subspace([Thm 7.3.3](../수업요약/Ch7_Dimension-and-Structure/7.3_The-fundamental-spaces-of-a-matrix.md#thm-733)).

</details>

**94.** 가역행렬의 row space와 column space는 같다 <sub>〔Ch7 p.42 (a)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

둘 다 Rⁿ 전체입니다.

</details>

**95.** W ⊆ V이면 W⊥은 V⊥의 subspace이다 <sub>〔Ch7 p.42 (b)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

포함이 뒤집힙니다: V⊥ ⊆ W⊥. 예: W = x축, V = R²이면 V⊥ = {0}, W⊥ = y축.

</details>

**96.** A의 각 행이 B의 행들의 결합이면 A와 B의 null space가 같다 <sub>〔Ch7 p.42 (c)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

row(A) ⊆ row(B) ⇒ null(B) ⊆ null(A)만 성립. 예: A = 0.

</details>

**97.** row space가 같은 n×n A, B는 column space도 같다 <sub>〔Ch7 p.42 (d)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

A = \[1 0; 0 0\], B = \[0 0; 1 0\]: row 둘 다 span(e₁), col은 span(e₁)과 span(e₂).

</details>

**98.** E가 elementary이면 A와 EA의 row space가 같다 <sub>〔Ch7 p.42 (e)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

[Thm 7.3.7](../수업요약/Ch7_Dimension-and-Structure/7.3_The-fundamental-spaces-of-a-matrix.md#thm-737)(a).

</details>

**99.** A가 정방이 아니면 행벡터 또는 열벡터가 dependent <sub>〔Ch7 p.52 (a)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

rank ≤ min(m, n) &lt; max(m, n)이라 더 많은 쪽은 dependent입니다.

</details>

**100.** 0 아닌 행을 하나 추가하면 rank가 1 늘어난다 <sub>〔Ch7 p.52 (b)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

추가한 행이 기존 row space 안에 있으면 rank는 그대로입니다.

</details>

**101.** 0이 아닌 m×n A의 nullity는 m 이하 <sub>〔Ch7 p.52 (c)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

nullity ≤ n − 1입니다. 예: 1×3 \[1 0 0\]은 nullity 2 > m = 1.

</details>

**102.** 행이 dependent인 정방행렬의 nullity는 1 이상 <sub>〔Ch7 p.52 (d)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

rank &lt; n ⇒ nullity = n − rank ≥ 1.

</details>

**103.** 정방 A에서 Ax = b가 어떤 b에서 inconsistent이면 nullity(A) = 0 <sub>〔Ch7 p.52 (e)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

모든 b에서 consistent가 아니므로 singular → nullity ≥ 1.

</details>

**104.** row space와 null space가 모두 원점 직선인 3×3 행렬은 없다 <sub>〔Ch7 p.52 (f)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

rank + nullity = 3인데 1 + 1 = 2입니다.

</details>

**105.** m×n A에서 rank(Aᵀ) + nullity(Aᵀ) = ? <sub>〔Ch7 p.52 D2〕</sub>

<details>
<summary>정답 보기</summary>

**m**

Aᵀ는 n×m이므로 열 수 m([Thm 7.4.1](../수업요약/Ch7_Dimension-and-Structure/7.4_The-dimension-theorem-and-its-implications.md#thm-741)).

</details>

**106.** 행이 열보다 많으면 row space 차원이 column space 차원보다 크다 <sub>〔Ch7 p.64 (a)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

Rank theorem: 항상 같습니다.

</details>

**107.** rank(A) = rank(Aᵀ)이면 A는 정방 <sub>〔Ch7 p.64 (b)〕</sub>

<details>
<summary>정답 보기</summary>

**F**

모든 행렬에서 성립합니다([Thm 7.5.2](../수업요약/Ch7_Dimension-and-Structure/7.5_The-rank-theorem-and-its-implications.md#thm-752)).

</details>

**108.** A가 n×n 가역이면 A와 \[A | b\]의 rank가 같다 <sub>〔Ch7 p.64 (c)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

둘 다 n. rank\[A | b\] ≤ n(행 수)이고 ≥ rank(A) = n.

</details>

**109.** full row rank이면서 full column rank이면 A는 정방 <sub>〔Ch7 p.64 (d)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

rank = m이고 rank = n이므로 m = n.

</details>

**110.** R²의 원점 직선 W 위 정사영 행렬의 rank, R³의 원점 평면 위 정사영 행렬의 rank <sub>〔Ch7-2 p.12 (1)〕</sub>

<details>
<summary>정답 보기</summary>

**1, 2**

P의 column space가 W입니다. 일반적으로 rank P = dim W. 직선은 1, 평면은 2.

</details>

**111.** n×n 정사영 행렬 P(W 위)의 nullity <sub>〔Ch7-2 p.12 (2)〕</sub>

<details>
<summary>정답 보기</summary>

**n − dim W**

null(P) = W⊥, dim W⊥ = n − dim W. 직선이면 n − 1, 평면이면 n − 2.

</details>

**112.** 정사영 행렬 P는 P² = P를 만족한다 <sub>〔Ch7-2 p.12 (3)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

이미 W 안의 벡터는 다시 정사영해도 그대로입니다. M(MᵀM)⁻¹MᵀM(MᵀM)⁻¹Mᵀ = M(MᵀM)⁻¹Mᵀ.

</details>

**113.** Ax = b가 consistent이면 x의 row(A) 위 정사영도 해이다 <sub>〔Ch7-2 p.12 (4)〕</sub>

<details>
<summary>정답 보기</summary>

**T**

x − proj<sub>row</sub>x ∈ row(A)⊥ = null(A)이므로 A·proj<sub>row</sub>x = Ax = b ([Thm 7.7.7](../수업요약/Ch7_Dimension-and-Structure/7.7_The-projection-theorem.md#thm-777)).

</details>

**114.** Gram–Schmidt 각 단계에서 span{v₁, …, v<sub>j</sub>}와 span{w₁, …, w<sub>j</sub>}의 관계 <sub>〔Ch7-2 p.20 (1)〕</sub>

<details>
<summary>정답 보기</summary>

**같다**

v<sub>j</sub>는 w<sub>j</sub>와 앞 v들의 결합이고, 거꾸로 w<sub>j</sub>도 v들의 결합입니다.

</details>

**115.** v₃는 어떤 subspace와 직교하는가 <sub>〔Ch7-2 p.20 (2)〕</sub>

<details>
<summary>정답 보기</summary>

**span{w₁, w₂} = span{v₁, v₂}**

v₃ = w₃ − proj<sub>span{v₁,v₂}</sub>w₃는 그 span의 ⊥ 성분입니다.

</details>

**116.** 입력 벡터가 linearly dependent이면 Gram–Schmidt에서 생기는 일 <sub>〔Ch7-2 p.20 (3)〕</sub>

<details>
<summary>정답 보기</summary>

**어떤 v<sub>k</sub> = 0**

w<sub>k</sub>가 앞 벡터들의 span 안에 있으면 정사영이 자기 자신이라 빼면 0입니다. 정규화가 불가능합니다.

</details>

---
[과목 지도](../README.md)
