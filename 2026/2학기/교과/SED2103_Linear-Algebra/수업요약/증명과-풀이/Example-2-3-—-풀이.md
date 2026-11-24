# Example 2, 3 — 풀이

> 본문: [4.4 Eigenvalues와 eigenvectors](../Ch4_Determinants-and-Eigenvalues/4.4_Eigenvalues와-eigenvectors.md)

1. Ex 2: det(λI − A) = (λ−1)(λ−2) − 12 = λ² − 3λ − 10 = (λ−5)(λ+2)
2. λ = 5: \[4 −3; −4 3\] → 4x − 3y = 0 → eigenvector (3, 4)
3. λ = −2: \[−3 −3; −4 −4\] → x + y = 0 → eigenvector (−1, 1)
4. Ex 3: λI − A = \[λ 1 0; 0 λ −1; 4 17 λ−8\]
5. 1행 전개: λ(λ² − 8λ + 17) − 4 = λ³ − 8λ² + 17λ − 4 = (λ−4)(λ² − 4λ + 1)
6. λ = 4, 2 ± √3. 검산: 합 8 = tr(A), 곱 4 = det(A)

λ = 4 찾는 요령: 상수항 −4의 약수를 대입해 0이 되는 값을 찾은 뒤 나눕니다.

---
[증명과 풀이 목록](README.md) · [과목 지도](../../README.md)
